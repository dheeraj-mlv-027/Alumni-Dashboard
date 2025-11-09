# Alumni Network Portal - Complete Features Guide

## 🎯 Overview

The Alumni Network Portal is a comprehensive Streamlit application that provides a complete alumni management system with analytics, directory search, and profile management capabilities.

---

## 🔐 Authentication System

### Sign Up Process
1) Navigate to the "Sign Up" tab
2) Required fields:
   - **Full Name**: Your complete name
   - **Email**: Valid email address (becomes your login username)
   - **Alumni ID**: Must match an ID in the database (format: SLU + YEAR + 5 digits)
   - **Password**: Secure password for your account

3) Validation:
   - Email must be unique (not already registered)
   - Alumni ID must exist in `alumni_master (2).csv`
   - All fields are required

4) On successful registration:
   - Account created in `users.json`
   - Password is hashed for security
   - Redirected to sign in

### Sign In Process
1) Navigate to the "Sign In" tab
2) Enter your registered email and password
3) On successful login:
   - Session is created
   - Redirected to dashboard
   - Full access to all features

### Security Features
- **Password Hashing**: SHA256 encryption for all passwords
- **Session Management**: Secure session-based authentication
- **Alumni ID Verification**: Ensures only valid alumni can register
- **Logout**: Secure logout that clears all session data

---

## 📊 Analytics Dashboard

### Key Metrics (Top Cards)

**1) Total Alumni**
- Shows total number of alumni in the database
- Real-time count from CSV data

**2) Departments**
- Number of unique academic departments/majors
- Represents diversity of programs

**3) Companies**
- Count of unique companies where alumni have worked
- Based on job history data

**4) Locations**
- Number of unique cities where alumni currently reside
- Geographic distribution metric

### Visualizations

**1) Graduates by Year (Bar Chart)**
- X-axis: Graduation years
- Y-axis: Number of graduates
- Color: Blue gradient
- Shows trends in alumni graduation over time
- Identifies peak graduation years

**2) Alumni by Department (Pie Chart)**
- Shows percentage distribution across departments
- Each slice represents a major/department
- Labels show both percentage and department name
- Color-coded for easy identification
- Helps understand program popularity

**3) Top Locations (Horizontal Bar Chart)**
- Shows top 10 cities with most alumni
- Y-axis: City names
- X-axis: Alumni count
- Color: Teal gradient
- Sorted by count (descending)
- Helps identify major alumni hubs

### Use Cases for Analytics
- **Recruitment**: Identify target demographics
- **Networking Events**: Plan events in cities with most alumni
- **Department Relations**: Understand which programs have largest networks
- **Trend Analysis**: See graduation patterns over years

---

## 👥 Alumni Directory

### Search Functionality

**Search Box**
- Free-text search across:
  - Alumni names
  - Major/department names
- Case-insensitive matching
- Real-time filtering

### Filter Options

**1) Graduation Year Filter**
- Dropdown with all available years
- Option: "All Years" to clear filter
- Filters alumni by their graduation year
- Useful for finding classmates

**2) Department Filter**
- Dropdown with all majors/departments
- Option: "All Departments" to clear filter
- Find alumni from specific programs
- Network with same-field professionals

**3) Current Company Filter**
- Dropdown with all companies from job history
- Option: "All Companies" to clear filter
- Based on most recent job position
- Find alumni at target companies
- Useful for job referrals

**Clear Filters Button**
- Resets all filters to default
- Clears search query
- Shows all alumni again

### Alumni Cards

Each alumni card displays:

**Header Section:**
- **Name**: Alumni's full name (large, bold)
- **Current Position**: Latest job title and company

**Badge Row:**
- 🎓 **Graduation Year**: Class of XXXX
- 📚 **Department**: Major/field of study
- 📍 **Location**: Current city and state

**Additional Info:**
- 💼 **Position Count**: Number of jobs in their history

**Actions:**
- **View Profile Button**: Opens detailed profile view

### Results Display
- Shows count: "Showing X of Y alumni"
- Displays up to 20 results at a time
- Sorted by relevance

### Detailed Profile View

When clicking "View Profile", an expandable section shows:

**Personal Information:**
- Full name and Alumni ID
- Graduation year and major
- Current location
- Interests and hobbies

**Complete Work Experience:**
- All jobs in reverse chronological order (newest first)
- For each position:
  - Job title and company name
  - Date range (Start Year - End Year)
  - Job location
  - Duration (years at company)

**Close Button:**
- Returns to directory listing

---

## 👤 My Profile

### Profile Header

**Left Section:**
- **Name**: Large display of your full name
- **Current Role**: Latest job title and company
- **Quick Info Row**:
  - 🎓 Class of [Year]
  - 📚 [Your Major]
  - 📍 [Your Location]

**Right Section:**
- **Edit Profile Toggle**: Switch between view and edit mode
- **Logout Button**: Sign out of the application

### Personal Information Section

**View Mode** (Edit Profile OFF):
- Full Name (read-only)
- Location (read-only)
- Alumni ID (read-only)
- Email (read-only)

**Edit Mode** (Edit Profile ON):
- Full Name (editable text input)
- Location (editable text input)
- Interests (editable text area)
- **Save Changes Button**: Saves updates to CSV

**Editable Fields:**
1) **Full Name**: Update your display name
2) **Location**: Change current city and state
3) **Interests**: Update hobbies, skills, and interests

**Note**: Alumni ID and Email cannot be changed for data integrity

### Education Section

Displays:
- **Department/Major**: Your field of study
- **Degree**: Degree type (Bachelor of Science)
- **Graduation Year**: Year you graduated

All fields are read-only (sourced from alumni master data)

### Work Experience Section

Shows complete employment history:

**For Each Position:**
- **Job Title**: Large heading
- **Company Name**: Bold company name
- **Duration**: Date range in "YYYY - YYYY" format
- **Location**: City and state of job
- **Visual Separation**: Each job clearly separated

**Ordering:**
- Most recent job appears first
- Chronologically descending order

**Data Source:**
- Pulled from `job_history (2).csv`
- Linked via Alumni ID
- Shows all historical positions

---

## 🔄 Data Flow

### Data Sources

**1) alumni_master (2).csv**
- Alumni_ID (Primary Key)
- Alumni_Name
- Year_of_Joining
- Year_of_Passing
- Alumni_Major (Department)
- Current_Location
- Interests

**2) job_history (2).csv**
- Job_ID (Primary Key)
- Alumni_ID (Foreign Key)
- Alumni_Name
- Company_Name
- Job_Title
- Job_Location
- Start_Year
- End_Year
- Period
- Years_at_Company

**3) users.json** (Created by app)
```json
{
  "user@example.com": {
    "full_name": "John Doe",
    "alumni_id": "SLU202000001",
    "password": "hashed_password_here",
    "created_at": "2025-11-06T12:00:00"
  }
}
```

### Update Flow

1) User logs in with credentials from `users.json`
2) Alumni ID from `users.json` links to `alumni_master (2).csv`
3) Profile data loaded from CSV files
4) User edits profile information
5) Click "Save Changes"
6) Updates written back to `alumni_master (2).csv`
7) Cache cleared and data reloaded
8) Updated profile displayed

---

## 🎨 Design Features

### Color Scheme
- **Primary Blue**: #1e40af (buttons, main elements)
- **Teal**: #06b6d4 (charts, accents)
- **Purple Gradient**: For profile headers
- **Gray**: #64748b (secondary text)

### Responsive Design
- Works on desktop, tablet, and mobile
- Columns adjust based on screen size
- Charts scale appropriately
- Mobile-friendly touch targets

### User Experience
- Clear visual hierarchy
- Intuitive navigation with tabs
- Immediate feedback on actions
- Consistent styling throughout
- Loading states for better UX

---

## 💡 Tips & Best Practices

### For Alumni

**1) Complete Your Profile**
- Add detailed interests
- Keep location updated
- Ensure accuracy for networking

**2) Use Filters Effectively**
- Combine multiple filters for specific searches
- Use company filter to find alumni at target employers
- Year filter to connect with classmates

**3) Privacy**
- Your profile is visible to all logged-in alumni
- Keep information professional
- Update regularly for accuracy

### For Administrators

**1) Data Management**
- Keep CSV files backed up
- Validate data before importing
- Maintain consistent ID formats

**2) User Management**
- Monitor `users.json` for accounts
- Alumni IDs must exist in database before signup
- Regular data validation recommended

**3) Performance**
- App uses caching for better performance
- Large datasets handled efficiently
- Clear cache if data seems stale

---

## 🐛 Common Issues & Solutions

### Issue: Cannot Sign Up
**Possible Causes:**
- Alumni ID doesn't exist in database
- Email already registered
- Missing required fields

**Solutions:**
- Verify Alumni ID in CSV file
- Try different email
- Ensure all fields filled

### Issue: Profile Won't Update
**Possible Causes:**
- Not in edit mode
- No changes made
- File permissions

**Solutions:**
- Toggle "Edit Profile" switch
- Make actual changes before saving
- Check file write permissions

### Issue: Charts Not Showing
**Possible Causes:**
- Plotly not installed
- Data format issues
- Browser compatibility

**Solutions:**
- Run: `pip install plotly`
- Check CSV data integrity
- Try different browser

### Issue: Search Returns No Results
**Possible Causes:**
- Too restrictive filters
- Typo in search query
- No matching data

**Solutions:**
- Clear all filters
- Check spelling
- Try broader search terms

---

## 📈 Future Enhancement Ideas

1) **Email Integration**: Send emails to alumni
2) **Event Management**: Create and manage alumni events
3) **Job Board**: Post and apply for jobs
4) **Mentorship Program**: Connect students with alumni
5) **Discussion Forum**: Community discussions
6) **Advanced Analytics**: More detailed insights
7) **Photo Uploads**: Profile pictures
8) **LinkedIn Integration**: Import profiles
9) **Export Features**: Download directory as PDF/Excel
10) **Admin Panel**: Manage users and data

---

## 📞 Support

For issues or questions:
1) Check this guide first
2) Review README_STREAMLIT.md
3) Verify CSV data format
4) Check console for error messages
5) Ensure all dependencies installed

---

## 🚀 Quick Start Reminder

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run alumni_dashboard_app.py

# Or use the start script
./start_app.sh
```

---

**Built with ❤️ using Streamlit, Pandas, and Plotly**

