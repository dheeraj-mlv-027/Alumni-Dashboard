import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os
from datetime import datetime
import hashlib

# Page configuration
st.set_page_config(
    page_title="Alumni Network Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e40af;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
    }
    .alumni-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .profile-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 0.5rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# File paths
USERS_FILE = "users.json"
ALUMNI_CSV = "alumni_master (2).csv"
JOB_HISTORY_CSV = "job_history (2).csv"

# Helper functions
def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

@st.cache_data
def load_alumni_data():
    """Load alumni master data"""
    return pd.read_csv(ALUMNI_CSV)

@st.cache_data
def load_job_history():
    """Load job history data"""
    return pd.read_csv(JOB_HISTORY_CSV)

def authenticate(email, password):
    """Authenticate user"""
    users = load_users()
    if email in users:
        if users[email]['password'] == hash_password(password):
            return True, users[email]
    return False, None

def register_user(full_name, email, alumni_id, password, user_type):
    """Register new user - open for both students and alumni"""
    users = load_users()
    if email in users:
        return False, "Email already registered"
    
    # For students, alumni_id can be empty or will be assigned
    if not alumni_id:
        # Generate a temporary ID for students
        alumni_id = f"STU{datetime.now().year}{len(users):05d}"
    
    users[email] = {
        'full_name': full_name,
        'alumni_id': alumni_id,
        'password': hash_password(password),
        'user_type': user_type,
        'created_at': datetime.now().isoformat()
    }
    save_users(users)
    return True, "Registration successful"

def get_alumni_profile(alumni_id):
    """Get complete alumni profile with job history"""
    alumni_df = load_alumni_data()
    job_df = load_job_history()
    
    # Get alumni basic info - handle if not found (for new students)
    alumni_records = alumni_df[alumni_df['Alumni_ID'] == alumni_id]
    
    if not alumni_records.empty:
        alumni_info = alumni_records.iloc[0].to_dict()
    else:
        # Create default profile for new users (students)
        alumni_info = {
            'Alumni_ID': alumni_id,
            'Alumni_Name': 'New User',
            'Year_of_Joining': datetime.now().year,
            'Year_of_Passing': 'Current',
            'Alumni_Major': 'Not specified',
            'Current_Location': 'Not specified',
            'Interests': 'Not specified'
        }
    
    # Get job history
    jobs = job_df[job_df['Alumni_ID'] == alumni_id].sort_values('Start_Year', ascending=False)
    
    return alumni_info, jobs

def update_alumni_profile(alumni_id, updated_data):
    """Update alumni profile in CSV - add new row if user doesn't exist"""
    alumni_df = load_alumni_data()
    existing_records = alumni_df[alumni_df['Alumni_ID'] == alumni_id]
    
    if not existing_records.empty:
        # Update existing record
        idx = existing_records.index[0]
        for key, value in updated_data.items():
            if key in alumni_df.columns:
                alumni_df.at[idx, key] = value
    else:
        # Create new record for new students/users
        new_record = {
            'Alumni_ID': alumni_id,
            'Alumni_Name': updated_data.get('Alumni_Name', 'New User'),
            'Year_of_Joining': datetime.now().year,
            'Year_of_Passing': updated_data.get('Year_of_Passing', 'Current'),
            'Alumni_Major': updated_data.get('Alumni_Major', 'Not specified'),
            'Current_Location': updated_data.get('Current_Location', 'Not specified'),
            'Interests': updated_data.get('Interests', 'Not specified')
        }
        # Append new row
        alumni_df = pd.concat([alumni_df, pd.DataFrame([new_record])], ignore_index=True)
    
    alumni_df.to_csv(ALUMNI_CSV, index=False)
    st.cache_data.clear()

def add_job_experience(alumni_id, alumni_name, job_data):
    """Add new job experience to job_history CSV"""
    job_df = load_job_history()
    
    # Get the next Job_ID
    next_job_id = job_df['Job_ID'].max() + 1 if not job_df.empty else 1
    
    # Calculate years at company
    start_year = int(job_data['Start_Year'])
    end_year = int(job_data['End_Year']) if job_data['End_Year'] != 'Present' else datetime.now().year
    years_at_company = end_year - start_year
    
    # Create period string
    period = f"{start_year} - {job_data['End_Year']}"
    
    # Create new job record
    new_job = {
        'Job_ID': next_job_id,
        'Alumni_ID': alumni_id,
        'Alumni_Name': alumni_name,
        'Company_Name': job_data['Company_Name'],
        'Job_Title': job_data['Job_Title'],
        'Job_Location': job_data['Job_Location'],
        'Start_Year': start_year,
        'End_Year': end_year if job_data['End_Year'] != 'Present' else datetime.now().year,
        'Period': period,
        'Years_at_Company': f"{years_at_company} years" if years_at_company != 1 else "1 year"
    }
    
    # Append new job to dataframe
    job_df = pd.concat([job_df, pd.DataFrame([new_job])], ignore_index=True)
    
    # Save to CSV
    job_df.to_csv(JOB_HISTORY_CSV, index=False)
    st.cache_data.clear()

# Authentication Pages
def show_auth_page():
    """Show authentication page (login/signup)"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div style='text-align: center; margin-bottom: 2rem;'>", unsafe_allow_html=True)
        st.markdown("# 🎓")
        st.markdown("<div class='main-header'>Alumni Network Portal</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-header'>Connect with your alumni community</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
        
        with tab1:
            st.markdown("### Sign In")
            email = st.text_input("Email", key="login_email", placeholder="you@example.com")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Sign In", use_container_width=True, type="primary"):
                if email and password:
                    success, user_data = authenticate(email, password)
                    if success:
                        st.session_state.authenticated = True
                        st.session_state.user_email = email
                        st.session_state.alumni_id = user_data['alumni_id']
                        st.session_state.user_name = user_data['full_name']
                        st.rerun()
                    else:
                        st.error("Invalid email or password")
                else:
                    st.error("Please fill in all fields")
        
        with tab2:
            st.markdown("### Sign Up")
            st.caption("Open for both students and alumni")
            
            # User type selection
            user_type = st.radio(
                "I am a:",
                ["🎓 Student", "👨‍🎓 Alumni"],
                horizontal=True,
                key="user_type"
            )
            
            full_name = st.text_input("Full Name", key="signup_name", placeholder="John Doe")
            email = st.text_input("Email", key="signup_email", placeholder="you@example.com")
            
            # Alumni ID field - optional for students, required for alumni
            if "Alumni" in user_type:
                alumni_id = st.text_input(
                    "Alumni ID", 
                    key="signup_alumni_id", 
                    placeholder="SLU202000001",
                    help="Enter your Alumni ID from the database"
                )
            else:
                alumni_id = st.text_input(
                    "Student ID (Optional)", 
                    key="signup_alumni_id", 
                    placeholder="Leave empty to auto-generate",
                    help="Optional: Enter your student ID or leave blank"
                )
            
            password = st.text_input("Password", type="password", key="signup_password")
            
            if st.button("Create Account", use_container_width=True, type="primary"):
                if full_name and email and password:
                    success, message = register_user(full_name, email, alumni_id, password, user_type)
                    if success:
                        st.success(message + " Please sign in.")
                    else:
                        st.error(message)
                else:
                    st.error("Please fill in Full Name, Email, and Password")

# Analytics Tab
def show_analytics_tab():
    """Show analytics dashboard"""
    alumni_df = load_alumni_data()
    job_df = load_job_history()
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Alumni", len(alumni_df), delta=None)
    
    with col2:
        unique_departments = alumni_df['Alumni_Major'].nunique()
        st.metric("Departments", unique_departments)
    
    with col3:
        unique_companies = job_df['Company_Name'].nunique()
        st.metric("Companies", unique_companies)
    
    with col4:
        unique_locations = alumni_df['Current_Location'].nunique()
        st.metric("Locations", unique_locations)
    
    st.markdown("---")
    
    # Charts row
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Graduates by Year")
        st.caption("Number of alumni graduating each year")
        
        graduates_by_year = alumni_df['Year_of_Passing'].value_counts().sort_index()
        fig = px.bar(
            x=graduates_by_year.index,
            y=graduates_by_year.values,
            labels={'x': 'Year', 'y': 'Number of Graduates'},
            color_discrete_sequence=['#1e40af']
        )
        fig.update_layout(
            showlegend=False,
            height=400,
            xaxis_title="",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Alumni by Department")
        st.caption("Distribution across departments")
        
        dept_counts = alumni_df['Alumni_Major'].value_counts()
        fig = px.pie(
            values=dept_counts.values,
            names=dept_counts.index,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Top Locations
    st.markdown("### Top Locations")
    st.caption("Cities with most alumni")
    
    location_counts = alumni_df['Current_Location'].value_counts().head(10)
    fig = px.bar(
        y=location_counts.index,
        x=location_counts.values,
        orientation='h',
        labels={'x': 'Count', 'y': 'Location'},
        color_discrete_sequence=['#06b6d4']
    )
    fig.update_layout(
        showlegend=False,
        height=400,
        xaxis_title="",
        yaxis_title=""
    )
    st.plotly_chart(fig, use_container_width=True)

# Alumni Directory Tab
def show_directory_tab():
    """Show alumni directory with search and filters"""
    alumni_df = load_alumni_data()
    job_df = load_job_history()
    
    st.markdown("### Search & Filter Alumni")
    st.caption("Find alumni by name, graduation year, department, or company")
    
    # Filters
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        search_query = st.text_input("🔍 Search", placeholder="Name, email, or role...")
    
    with col2:
        years = ['All Years'] + sorted(alumni_df['Year_of_Passing'].unique().tolist())
        selected_year = st.selectbox("Graduation Year", years)
    
    with col3:
        departments = ['All Departments'] + sorted(alumni_df['Alumni_Major'].unique().tolist())
        selected_dept = st.selectbox("Department", departments)
    
    with col4:
        # Get current companies (latest job)
        latest_jobs = job_df.sort_values('End_Year', ascending=False).groupby('Alumni_ID').first()
        companies = ['All Companies'] + sorted(latest_jobs['Company_Name'].unique().tolist())
        selected_company = st.selectbox("Current Company", companies)
    
    # Apply filters
    filtered_df = alumni_df.copy()
    
    if search_query:
        filtered_df = filtered_df[
            filtered_df['Alumni_Name'].str.contains(search_query, case=False, na=False) |
            filtered_df['Alumni_Major'].str.contains(search_query, case=False, na=False)
        ]
    
    if selected_year != 'All Years':
        filtered_df = filtered_df[filtered_df['Year_of_Passing'] == selected_year]
    
    if selected_dept != 'All Departments':
        filtered_df = filtered_df[filtered_df['Alumni_Major'] == selected_dept]
    
    if selected_company != 'All Companies':
        alumni_with_company = latest_jobs[latest_jobs['Company_Name'] == selected_company].index
        filtered_df = filtered_df[filtered_df['Alumni_ID'].isin(alumni_with_company)]
    
    # Show results
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(f"Showing {len(filtered_df)} of {len(alumni_df)} alumni")
    with col2:
        if st.button("Clear Filters"):
            st.rerun()
    
    st.markdown("---")
    
    # Display alumni cards
    for idx, alumni in filtered_df.head(20).iterrows():
        # Get latest job
        alumni_jobs = job_df[job_df['Alumni_ID'] == alumni['Alumni_ID']].sort_values('End_Year', ascending=False)
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"### {alumni['Alumni_Name']}")
            
            if not alumni_jobs.empty:
                latest_job = alumni_jobs.iloc[0]
                st.markdown(f"**{latest_job['Job_Title']}** at **{latest_job['Company_Name']}**")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.caption(f"🎓 Class of {alumni['Year_of_Passing']}")
            with col_b:
                st.caption(f"📚 {alumni['Alumni_Major']}")
            with col_c:
                st.caption(f"📍 {alumni['Current_Location']}")
            
            if not alumni_jobs.empty:
                st.caption(f"💼 {len(alumni_jobs)} positions")
        
        with col2:
            if st.button("View Profile", key=f"view_{alumni['Alumni_ID']}"):
                st.session_state.view_alumni_id = alumni['Alumni_ID']
                st.session_state.show_alumni_profile = True
        
        st.markdown("---")
    
    # Show alumni profile modal
    if st.session_state.get('show_alumni_profile'):
        show_alumni_profile_modal(st.session_state.view_alumni_id)

def show_alumni_profile_modal(alumni_id):
    """Show detailed alumni profile in a modal-like view"""
    alumni_info, jobs = get_alumni_profile(alumni_id)
    
    with st.expander("👤 Alumni Profile", expanded=True):
        st.markdown(f"## {alumni_info['Alumni_Name']}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**Alumni ID:** {alumni_info['Alumni_ID']}")
        with col2:
            st.markdown(f"**Graduation:** {alumni_info['Year_of_Passing']}")
        with col3:
            st.markdown(f"**Major:** {alumni_info['Alumni_Major']}")
        
        st.markdown(f"**📍 Current Location:** {alumni_info['Current_Location']}")
        st.markdown(f"**🎯 Interests:** {alumni_info['Interests']}")
        
        st.markdown("### Work Experience")
        for idx, job in jobs.iterrows():
            st.markdown(f"**{job['Job_Title']}** at **{job['Company_Name']}**")
            st.caption(f"{job['Period']} • {job['Job_Location']} • {job['Years_at_Company']}")
            st.markdown("")
        
        if st.button("Close", key="close_profile"):
            st.session_state.show_alumni_profile = False
            st.rerun()

# My Profile Tab
def show_profile_tab():
    """Show user's profile with edit capabilities"""
    alumni_id = st.session_state.alumni_id
    alumni_info, jobs = get_alumni_profile(alumni_id)
    
    # Use the name from session if profile is not set up yet
    if alumni_info['Alumni_Name'] == 'New User':
        alumni_info['Alumni_Name'] = st.session_state.user_name
    
    # Profile header
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"# {alumni_info['Alumni_Name']}")
        if not jobs.empty:
            latest_job = jobs.iloc[0]
            st.markdown(f"### {latest_job['Job_Title']} at {latest_job['Company_Name']}")
        else:
            # Show user type for new users
            users = load_users()
            user_type = users[st.session_state.user_email].get('user_type', 'Student')
            st.markdown(f"### {user_type}")
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            year_display = alumni_info['Year_of_Passing'] if alumni_info['Year_of_Passing'] != 'Current' else 'Current Student'
            st.markdown(f"🎓 **{year_display}**")
        with col_b:
            st.markdown(f"📚 **{alumni_info['Alumni_Major']}**")
        with col_c:
            st.markdown(f"📍 **{alumni_info['Current_Location']}**")
    
    with col2:
        edit_mode = st.toggle("Edit Profile", value=False)
    
    st.markdown("---")
    
    # Personal Information Section
    st.markdown("## Personal Information")
    st.caption("Update your personal details and contact information")
    
    if edit_mode:
        col1, col2 = st.columns(2)
        
        with col1:
            new_name = st.text_input("Full Name", value=alumni_info['Alumni_Name'])
            new_location = st.text_input("Location", value=alumni_info['Current_Location'])
            new_major = st.text_input("Department/Major", value=alumni_info['Alumni_Major'])
        
        with col2:
            new_interests = st.text_area("Interests", value=alumni_info['Interests'], height=100)
            new_year = st.text_input("Graduation Year", value=str(alumni_info['Year_of_Passing']))
        
        if st.button("Save Changes", type="primary"):
            # Also update user's name in users.json
            users = load_users()
            users[st.session_state.user_email]['full_name'] = new_name
            save_users(users)
            st.session_state.user_name = new_name
            
            # Update alumni profile
            update_alumni_profile(alumni_id, {
                'Alumni_Name': new_name,
                'Current_Location': new_location,
                'Interests': new_interests,
                'Alumni_Major': new_major,
                'Year_of_Passing': new_year
            })
            st.success("Profile updated successfully!")
            st.rerun()
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Full Name", value=alumni_info['Alumni_Name'], disabled=True)
            st.text_input("Location", value=alumni_info['Current_Location'], disabled=True)
            st.text_input("Alumni ID", value=alumni_info['Alumni_ID'], disabled=True)
        
        with col2:
            users = load_users()
            user_email = st.session_state.user_email
            st.text_input("Email", value=user_email, disabled=True)
            user_type = users[user_email].get('user_type', 'Student')
            st.text_input("Account Type", value=user_type, disabled=True)
    
    st.markdown("---")
    
    # Education Section
    st.markdown("## Education")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_input("Department/Major", value=alumni_info['Alumni_Major'], disabled=not edit_mode, key="dept_display")
    with col2:
        st.text_input("Degree", value="Bachelor of Science", disabled=True)
    with col3:
        st.text_input("Year", value=str(alumni_info['Year_of_Passing']), disabled=not edit_mode, key="year_display")
    
    st.markdown("---")
    
    # Work Experience Section
    users = load_users()
    user_type = users[st.session_state.user_email].get('user_type', 'Student')
    is_alumni = "Alumni" in user_type
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## Work Experience")
        if is_alumni:
            st.caption("Your professional experience and career history")
        else:
            st.caption("Students cannot add work experience yet")
    
    with col2:
        if is_alumni:
            if st.button("➕ Add Experience", type="secondary"):
                st.session_state.show_add_experience = True
    
    # Show Add Experience Form for Alumni
    if is_alumni and st.session_state.get('show_add_experience', False):
        with st.expander("➕ Add New Work Experience", expanded=True):
            st.markdown("### Add New Position")
            
            col1, col2 = st.columns(2)
            
            with col1:
                job_title = st.text_input("Job Title*", placeholder="e.g., Senior Software Engineer", key="new_job_title")
                company_name = st.text_input("Company Name*", placeholder="e.g., Google", key="new_company_name")
                job_location = st.text_input("Location*", placeholder="e.g., San Francisco, CA", key="new_job_location")
            
            with col2:
                current_year = datetime.now().year
                start_year = st.selectbox(
                    "Start Year*", 
                    options=list(range(current_year, 1980, -1)),
                    key="new_start_year"
                )
                
                # End year can be "Present" or a year
                is_current = st.checkbox("I currently work here", key="is_current_job")
                
                if is_current:
                    end_year = "Present"
                else:
                    end_year = st.selectbox(
                        "End Year*",
                        options=list(range(current_year, 1980, -1)),
                        key="new_end_year"
                    )
            
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                if st.button("💾 Save Experience", type="primary", use_container_width=True):
                    if job_title and company_name and job_location:
                        # Validate years
                        if not is_current and int(end_year) < int(start_year):
                            st.error("End year must be after start year!")
                        else:
                            job_data = {
                                'Job_Title': job_title,
                                'Company_Name': company_name,
                                'Job_Location': job_location,
                                'Start_Year': str(start_year),
                                'End_Year': str(end_year)
                            }
                            add_job_experience(alumni_id, alumni_info['Alumni_Name'], job_data)
                            st.success("Work experience added successfully!")
                            st.session_state.show_add_experience = False
                            st.rerun()
                    else:
                        st.error("Please fill in all required fields (marked with *)")
            
            with col2:
                if st.button("❌ Cancel", use_container_width=True):
                    st.session_state.show_add_experience = False
                    st.rerun()
    
    # Display existing work experience
    if not jobs.empty:
        st.markdown("")
        for idx, job in jobs.iterrows():
            with st.container():
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"### {job['Job_Title']}")
                    st.markdown(f"**{job['Company_Name']}**")
                    st.caption(f"{job['Period']} • {job['Job_Location']}")
                
                st.markdown("")
    else:
        if is_alumni:
            st.info("👆 Click 'Add Experience' to add your first work experience")
        else:
            st.info("Work experience will be available once you graduate and become an alumni")

# Main Dashboard
def show_dashboard():
    """Show main dashboard with tabs"""
    # Header
    col1, col2 = st.columns([6, 1])
    
    with col1:
        st.markdown("# 🎓 Alumni Dashboard")
        st.markdown(f"Welcome back, **{st.session_state.user_name}**!")
    
    with col2:
        if st.button("🚪 Logout"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Analytics", "👥 Alumni Directory", "👤 My Profile"])
    
    with tab1:
        show_analytics_tab()
    
    with tab2:
        show_directory_tab()
    
    with tab3:
        show_profile_tab()

# Main App
def main():
    """Main application entry point"""
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    # Show appropriate page
    if st.session_state.authenticated:
        show_dashboard()
    else:
        show_auth_page()

if __name__ == "__main__":
    main()

