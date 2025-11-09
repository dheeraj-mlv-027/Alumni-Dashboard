# 💼 Work Experience Management Feature

## Overview

Alumni can now add, view, and manage their work experience directly through the portal. All work experience entries are saved to the `job_history (2).csv` file for permanent storage and analytics.

---

## 🎯 Key Features

### ✅ For Alumni:
- Add unlimited work experience entries
- Edit job title, company, location, and dates
- Mark current positions as "Present"
- All entries saved to CSV database
- Visible in analytics and directory
- Automatic data validation

### ❌ For Students:
- Cannot add work experience yet
- Message: "Students cannot add work experience yet"
- Feature unlocked upon graduation/alumni status
- Can still view alumni work experience in directory

---

## 🚀 How to Add Work Experience (Alumni Only)

### Step 1: Navigate to Profile
1. Sign in to your account
2. Click on "👤 My Profile" tab
3. Scroll to "Work Experience" section

### Step 2: Click "Add Experience"
- Look for the "➕ Add Experience" button in the top-right of Work Experience section
- Click to open the add experience form

### Step 3: Fill in Job Details

**Required Fields (marked with *):**

**Column 1:**
- **Job Title**: Your position/role
  - Example: "Senior Software Engineer"
  - Example: "Product Manager"
  - Example: "Data Scientist"

- **Company Name**: Name of the organization
  - Example: "Google"
  - Example: "Microsoft"
  - Example: "Amazon"

- **Location**: City and state/country
  - Example: "San Francisco, CA"
  - Example: "New York, NY"
  - Example: "Remote"

**Column 2:**
- **Start Year**: When you started this position
  - Dropdown with years from current year to 1980
  - Select the year you began

- **End Year**: When you left or current status
  - Option 1: Check "I currently work here" for ongoing positions
  - Option 2: Select end year if you've left
  - Validates that end year is after start year

### Step 4: Save or Cancel
- **💾 Save Experience**: Saves the entry to database
- **❌ Cancel**: Discards changes and closes form

### Example Entry:

```
Job Title: Senior Software Engineer
Company Name: Google
Location: Mountain View, CA
Start Year: 2021
☑️ I currently work here
```

This creates:
- Period: "2021 - Present"
- Duration: "3 years" (calculated automatically)
- Job ID: Auto-generated
- Immediately visible in your profile

---

## 📊 Data Storage

### Job History CSV Format

When you add experience, it's saved to `job_history (2).csv`:

```csv
Job_ID,Alumni_ID,Alumni_Name,Company_Name,Job_Title,Job_Location,Start_Year,End_Year,Period,Years_at_Company
8791,SLU202400001,Donald Brown,Google,Senior Software Engineer,Mountain View CA,2021,2025,2021 - Present,4 years
```

### Fields Explained:

| Field | Description | Example |
|-------|-------------|---------|
| Job_ID | Unique identifier (auto-generated) | 8791 |
| Alumni_ID | Your alumni ID | SLU202400001 |
| Alumni_Name | Your full name | Donald Brown |
| Company_Name | Employer name | Google |
| Job_Title | Your position | Senior Software Engineer |
| Job_Location | Work location | Mountain View, CA |
| Start_Year | Year started | 2021 |
| End_Year | Year ended or current | 2025 or Present |
| Period | Date range | 2021 - Present |
| Years_at_Company | Duration | 4 years |

---

## 🎨 User Interface

### Work Experience Section Layout

**For Alumni:**
```
┌─────────────────────────────────────────────────────┐
│ ## Work Experience           [➕ Add Experience]    │
│ Your professional experience and career history     │
├─────────────────────────────────────────────────────┤
│                                                     │
│ ### Senior Software Engineer                        │
│ **Google**                                          │
│ 2021 - Present • Mountain View, CA                 │
│                                                     │
│ ### Software Developer                              │
│ **Amazon**                                          │
│ 2018 - 2021 • Seattle, WA                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**For Students:**
```
┌─────────────────────────────────────────────────────┐
│ ## Work Experience                                  │
│ Students cannot add work experience yet             │
├─────────────────────────────────────────────────────┤
│                                                     │
│ ℹ️ Work experience will be available once you      │
│    graduate and become an alumni                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Add Experience Form

```
┌────────── Add New Work Experience ──────────┐
│ ### Add New Position                        │
│                                             │
│ ┌─────────────────┬─────────────────────┐  │
│ │ Job Title*      │ Start Year*         │  │
│ │ [____________]  │ [2025 ▼]            │  │
│ │                 │                     │  │
│ │ Company Name*   │ ☐ I currently work  │  │
│ │ [____________]  │   here              │  │
│ │                 │                     │  │
│ │ Location*       │ End Year*           │  │
│ │ [____________]  │ [2024 ▼]            │  │
│ └─────────────────┴─────────────────────┘  │
│                                             │
│ [💾 Save Experience] [❌ Cancel]            │
└─────────────────────────────────────────────┘
```

---

## 🔐 Access Control

### Who Can Add Experience?

**Alumni (✅ Can Add):**
- Users who selected "👨‍🎓 Alumni" during registration
- Can see "➕ Add Experience" button
- Form is accessible
- All features enabled

**Students (❌ Cannot Add):**
- Users who selected "🎓 Student" during registration
- No "Add Experience" button visible
- See informational message instead
- Feature locked

### How is User Type Determined?

```python
# From users.json
{
  "user@email.com": {
    "full_name": "John Doe",
    "user_type": "🎓 Student"  // or "👨‍🎓 Alumni"
  }
}

# In code:
is_alumni = "Alumni" in user_type
if is_alumni:
    # Show add experience button
else:
    # Show student message
```

---

## ✅ Validation Rules

### 1) Required Fields
- ❌ Cannot save without Job Title
- ❌ Cannot save without Company Name
- ❌ Cannot save without Location
- ✅ All fields must be filled

### 2) Year Validation
- ❌ End year cannot be before start year
- ✅ Start year can be current year
- ✅ End year can be "Present" for current jobs
- ✅ Years range from 1980 to current year

### 3) Data Format
- Job Title: Text (any format)
- Company Name: Text (any format)
- Location: Text (typically "City, State")
- Years: Integer or "Present"

### Error Messages:

**Missing Required Fields:**
```
⚠️ Please fill in all required fields (marked with *)
```

**Invalid Date Range:**
```
❌ End year must be after start year!
```

**Success:**
```
✅ Work experience added successfully!
```

---

## 📈 Impact on Analytics

### Updated Metrics

When alumni add experience, it affects:

1. **Companies Count**: Increases if new company added
2. **Alumni Directory**: Shows updated work history
3. **Company Filter**: New companies appear in dropdown
4. **Profile Display**: Immediately shows new position
5. **Career Paths**: Helps students see progression

### Example Analytics Update:

**Before:**
- Total Companies: 12
- Alumni at Google: 2

**After Adding Google Position:**
- Total Companies: 12 (if Google exists) or 13 (if new)
- Alumni at Google: 3
- Filter options updated
- Directory results updated

---

## 🎯 Use Cases

### Use Case 1: Alumni Gets New Job

**Scenario**: Sarah got promoted to Senior Engineer at Google

**Steps:**
1. Login → My Profile
2. Click "➕ Add Experience"
3. Fill in:
   - Job Title: "Senior Software Engineer"
   - Company: "Google"
   - Location: "Mountain View, CA"
   - Start Year: 2025
   - ☑️ Currently work here
4. Click "💾 Save Experience"
5. ✅ New position added!
6. Visible in profile and directory

### Use Case 2: Alumni Updates Career History

**Scenario**: Michael wants to add his previous jobs

**Steps:**
1. Login → My Profile
2. Click "➕ Add Experience" for first job
3. Add: Software Developer at Amazon (2018-2021)
4. Click "➕ Add Experience" again
5. Add: Junior Developer at Startup (2016-2018)
6. Both positions now displayed
7. Shown in chronological order (newest first)

### Use Case 3: Student Tries to Add Experience

**Scenario**: Emma (current student) wants to add internship

**Steps:**
1. Login → My Profile
2. Scrolls to Work Experience
3. Sees: "Students cannot add work experience yet"
4. No "Add Experience" button visible
5. Message: "Work experience will be available once you graduate"

**Solution for Emma:**
- Wait until graduation
- Or admin can change status to Alumni
- Then feature becomes available

---

## 🔄 Workflow Diagram

```
┌─────────────┐
│ User Login  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Check Type  │
└──────┬──────┘
       │
       ├─── Alumni ──────┐
       │                 ▼
       │          ┌──────────────┐
       │          │ Show Add Btn │
       │          └──────┬───────┘
       │                 │
       │                 ▼
       │          ┌──────────────┐
       │          │ Click Button │
       │          └──────┬───────┘
       │                 │
       │                 ▼
       │          ┌──────────────┐
       │          │  Fill Form   │
       │          └──────┬───────┘
       │                 │
       │                 ▼
       │          ┌──────────────┐
       │          │   Validate   │
       │          └──────┬───────┘
       │                 │
       │            Valid│Invalid
       │                 │    │
       │                 ▼    ▼
       │          ┌─────────────┐
       │          │ Save to CSV │
       │          └──────┬──────┘
       │                 │
       │                 ▼
       │          ┌─────────────┐
       │          │   Success   │
       │          └──────┬──────┘
       │                 │
       │                 ▼
       │          ┌─────────────┐
       │          │   Refresh   │
       │          └─────────────┘
       │
       └─── Student ─────┐
                        ▼
                 ┌──────────────┐
                 │ Show Message │
                 └──────────────┘
                 │ No Add Option│
                 └──────────────┘
```

---

## 🛠️ Technical Implementation

### Function: `add_job_experience()`

```python
def add_job_experience(alumni_id, alumni_name, job_data):
    """
    Add new job experience to job_history CSV
    
    Parameters:
    - alumni_id: User's alumni ID
    - alumni_name: User's full name
    - job_data: Dict with job details
    
    Returns: None (saves to CSV)
    """
    # 1. Load existing job history
    job_df = load_job_history()
    
    # 2. Generate new Job_ID
    next_job_id = job_df['Job_ID'].max() + 1
    
    # 3. Calculate duration
    years_at_company = end_year - start_year
    
    # 4. Create new record
    new_job = {
        'Job_ID': next_job_id,
        'Alumni_ID': alumni_id,
        'Alumni_Name': alumni_name,
        'Company_Name': job_data['Company_Name'],
        'Job_Title': job_data['Job_Title'],
        'Job_Location': job_data['Job_Location'],
        'Start_Year': start_year,
        'End_Year': end_year,
        'Period': f"{start_year} - {end_year}",
        'Years_at_Company': f"{years_at_company} years"
    }
    
    # 5. Append to dataframe
    job_df = pd.concat([job_df, pd.DataFrame([new_job])])
    
    # 6. Save to CSV
    job_df.to_csv(JOB_HISTORY_CSV, index=False)
    
    # 7. Clear cache
    st.cache_data.clear()
```

### UI Logic

```python
# Check user type
user_type = users[email].get('user_type')
is_alumni = "Alumni" in user_type

# Show button only for alumni
if is_alumni:
    if st.button("➕ Add Experience"):
        st.session_state.show_add_experience = True

# Show form if triggered
if is_alumni and st.session_state.get('show_add_experience'):
    # Display form
    # Collect input
    # Validate
    # Save
```

---

## 📝 Best Practices

### For Alumni Adding Experience:

1. **Be Accurate**
   - Use official job titles
   - Correct company names (for filtering)
   - Accurate dates

2. **Be Complete**
   - Add all relevant positions
   - Include internships if significant
   - Update when changing jobs

3. **Be Consistent**
   - Use standard location format: "City, State"
   - Year format: YYYY
   - Professional language

4. **Update Regularly**
   - Mark previous jobs as ended
   - Add new positions promptly
   - Keep timeline current

### For Admins:

1. **Data Validation**
   - Periodically check CSV integrity
   - Verify Job_IDs are unique
   - Ensure no duplicate entries

2. **Backup**
   - Regular CSV backups
   - Version control recommended
   - Keep audit trail

3. **Monitoring**
   - Watch for invalid entries
   - Check date ranges
   - Verify company names

---

## 🐛 Troubleshooting

### Issue: "Add Experience" Button Not Visible

**Cause**: User registered as Student

**Solution**:
1. Check account type in profile
2. If should be Alumni, update users.json:
```json
"user_type": "👨‍🎓 Alumni"
```
3. Re-login

### Issue: Cannot Save Experience

**Possible Causes:**
- Missing required fields → Fill all fields
- Invalid date range → Check start/end years
- CSV file locked → Close Excel/editors
- Permission error → Check file permissions

### Issue: Experience Not Showing

**Solutions:**
1. Refresh page (Ctrl/Cmd + R)
2. Clear cache (press 'C' in terminal)
3. Check CSV file for entry
4. Verify Alumni_ID matches

### Issue: Duplicate Entries

**Prevention:**
- Don't click Save multiple times
- Wait for success message
- Check before adding again

**Fix:**
- Manually edit CSV to remove duplicate
- Keep entry with lowest Job_ID
- Delete others

---

## 🎓 Student Transition to Alumni

### When Students Graduate:

**Option 1: Admin Update**
```json
// In users.json
{
  "student@email.com": {
    "user_type": "👨‍🎓 Alumni"  // Changed from Student
  }
}
```

**Option 2: Profile Update**
- Student updates graduation year
- Status changes in profile
- Work experience unlocked

**Option 3: New Registration**
- Register new account as Alumni
- Transfer profile data
- Merge accounts

---

## 📊 Sample Data

### Example Job History Entries:

**Entry 1: Current Position**
```csv
8791,SLU202400001,Donald Brown,Google,Senior Software Engineer,Mountain View CA,2021,2025,2021 - Present,4 years
```

**Entry 2: Past Position**
```csv
8792,SLU202400001,Donald Brown,Amazon,Software Developer,Seattle WA,2018,2021,2018 - 2021,3 years
```

**Entry 3: Short-term Position**
```csv
8793,SLU202000003,Nancy Turner,Startup Inc,Junior Developer,Austin TX,2021,2022,2021 - 2022,1 year
```

---

## 🚀 Future Enhancements

Potential features to add:

1. **Edit Experience**: Modify existing entries
2. **Delete Experience**: Remove incorrect entries
3. **Drag to Reorder**: Change display order
4. **Job Description**: Add detailed description field
5. **Skills Tags**: Add skill tags to each job
6. **Achievements**: List key accomplishments
7. **References**: Add reference contacts
8. **Document Upload**: Attach offer letters/certificates
9. **Import from LinkedIn**: Auto-import work history
10. **Export Resume**: Generate PDF resume

---

## 📞 Support

If you encounter issues:

1. Check this guide first
2. Verify you're logged in as Alumni
3. Ensure all required fields filled
4. Check console for error messages
5. Verify CSV file accessibility
6. Contact admin if problem persists

---

**Happy career building! 💼✨**

