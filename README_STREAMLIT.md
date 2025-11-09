# Alumni Network Portal - Streamlit Application

A comprehensive alumni management dashboard built with Streamlit that allows alumni to view analytics, search the directory, and manage their profiles.

## Features

### 1) Authentication System
- **Sign Up**: New alumni can register using their Alumni ID from the database
- **Sign In**: Existing users can log in with email and password
- **Secure Storage**: User credentials stored in JSON format with hashed passwords

### 2) Analytics Dashboard
- Total alumni, departments, companies, and locations metrics
- Graduates by Year bar chart
- Alumni by Department pie chart
- Top Locations horizontal bar chart

### 3) Alumni Directory
- Search alumni by name or major
- Filter by graduation year, department, and current company
- View detailed profiles of other alumni
- See complete work experience history

### 4) My Profile
- View personal information
- Edit profile (name, location, interests)
- View education details
- See complete work experience timeline

## Installation & Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Ensure Data Files are Present

Make sure these CSV files are in the same directory:
- `alumni_master (2).csv`
- `job_history (2).csv`

### Step 3: Run the Application

```bash
streamlit run alumni_dashboard_app.py
```

The application will open in your default browser at `http://localhost:8501`

## Usage

### First Time Users

1) **Sign Up**:
   - Click on the "Sign Up" tab
   - Enter your full name
   - Enter your email
   - Enter your Alumni ID (must exist in the database, e.g., SLU202400001)
   - Create a password
   - Click "Create Account"

2) **Sign In**:
   - Go to "Sign In" tab
   - Enter your email and password
   - Click "Sign In"

### Using the Dashboard

**Analytics Tab**:
- View overall statistics about the alumni network
- Explore graduation trends
- See department distribution
- Find where alumni are located

**Alumni Directory Tab**:
- Use search box to find alumni by name
- Apply filters for graduation year, department, or company
- Click "View Profile" to see detailed information about any alumni
- Use "Clear Filters" to reset all filters

**My Profile Tab**:
- View your complete profile information
- Toggle "Edit Profile" to update your details
- Update your name, location, and interests
- View your work experience history
- See your education details

## Data Storage

- **User Accounts**: Stored in `users.json` (created automatically on first signup)
- **Alumni Data**: Reads from `alumni_master (2).csv`
- **Job History**: Reads from `job_history (2).csv`
- Profile updates are saved back to the CSV files

## Sample Alumni IDs for Testing

You can use any Alumni ID from the database to sign up. Here are a few examples:
- SLU202400001 (Donald Brown)
- SLU200600002 (Ronald Jones)
- SLU202100003 (Nancy Turner)
- SLU200800004 (Betty Baker)

## Security Features

- Passwords are hashed using SHA256
- Alumni ID validation during signup
- Session-based authentication
- Secure logout functionality

## Troubleshooting

**Issue**: "Invalid Alumni ID" during signup
- **Solution**: Make sure you're using an Alumni ID that exists in the `alumni_master (2).csv` file

**Issue**: Charts not displaying
- **Solution**: Ensure plotly is installed: `pip install plotly`

**Issue**: "File not found" error
- **Solution**: Make sure both CSV files are in the same directory as the Python script

## Technology Stack

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive charts and visualizations
- **JSON**: User data storage
- **hashlib**: Password hashing

## Notes

- The application uses caching for better performance
- Profile updates are immediately reflected in the CSV files
- The dashboard is responsive and works on different screen sizes
