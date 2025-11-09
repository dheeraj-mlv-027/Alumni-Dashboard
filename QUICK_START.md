# 🚀 Quick Start Guide - Alumni Network Portal

## Installation (One-Time Setup)

### Option 1: Using Start Script (Recommended)
```bash
cd /Users/dheeraj/Desktop/Assignments/Pavani
./start_app.sh
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run alumni_dashboard_app.py
```

---

## 📋 First Time Setup

1) **Open Browser**: App opens automatically at `http://localhost:8501`

2) **Create Account**:
   - Click "Sign Up" tab
   - Fill in your details
   - Use a valid Alumni ID from the database
   - Click "Create Account"

3) **Sign In**:
   - Enter your email and password
   - Click "Sign In"

4) **Explore Dashboard**:
   - Analytics: View statistics
   - Directory: Search alumni
   - My Profile: Update your info

---

## 🎓 Sample Alumni IDs for Testing

You can use any of these Alumni IDs to sign up:

| Alumni ID | Name | Major | Graduation Year |
|-----------|------|-------|-----------------|
| SLU202400001 | Donald Brown | Biotechnology | 2024 |
| SLU200600002 | Ronald Jones | Computer Science | 2006 |
| SLU202100003 | Nancy Turner | Finance | 2021 |
| SLU200800004 | Betty Baker | Data Science | 2008 |
| SLU201800005 | Benjamin Thomas | History | 2018 |

---

## 🔍 Quick Features Overview

### Analytics Tab
- ✅ View total alumni count
- ✅ See department distribution
- ✅ Check top locations
- ✅ Analyze graduation trends

### Directory Tab
- ✅ Search by name
- ✅ Filter by year/department/company
- ✅ View alumni profiles
- ✅ See work history

### My Profile Tab
- ✅ Update personal info
- ✅ Edit location and interests
- ✅ View work experience
- ✅ See education details

---

## 🛠️ Troubleshooting

### App Won't Start
```bash
# Check Python installation
python3 --version

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### "Invalid Alumni ID" Error
- Use an Alumni ID from the CSV file
- Format: SLU + YEAR + 5 digits (e.g., SLU202000001)

### Port Already in Use
```bash
# Stop existing Streamlit processes
pkill -f streamlit

# Or run on different port
streamlit run alumni_dashboard_app.py --server.port 8502
```

---

## 📁 File Structure

```
Pavani/
├── alumni_dashboard_app.py          # Main application
├── alumni_master (2).csv            # Alumni data
├── job_history (2).csv              # Job history data
├── users.json                       # User accounts (auto-created)
├── requirements.txt                 # Dependencies
├── start_app.sh                     # Quick start script
├── README_STREAMLIT.md              # Full documentation
├── FEATURES_GUIDE.md                # Detailed features
└── QUICK_START.md                   # This file
```

---

## ⚡ Common Commands

### Start Application
```bash
streamlit run alumni_dashboard_app.py
```

### Stop Application
- Press `Ctrl + C` in terminal
- Or close the terminal window

### Clear Cache (if data not updating)
- Press `C` in terminal while app is running
- Or restart the application

### View in Browser
- Main URL: `http://localhost:8501`
- Network URL: Check terminal for IP address

---

## 🎯 Next Steps

1) **Explore Analytics**: See overall alumni statistics
2) **Search Directory**: Find and connect with alumni
3) **Update Profile**: Keep your information current
4) **Network**: Use filters to find relevant connections

---

## 📚 Additional Resources

- **Full Documentation**: See `README_STREAMLIT.md`
- **Feature Details**: See `FEATURES_GUIDE.md`
- **Sample Data**: Check CSV files for available alumni

---

## 💡 Pro Tips

1) **Use Filters Together**: Combine year + department + company for targeted searches
2) **Keep Profile Updated**: Regular updates help others find you
3) **Explore Analytics**: Understand your alumni network better
4) **Save Often**: Remember to click "Save Changes" when editing profile

---

## 🆘 Need Help?

1) Check error messages in terminal
2) Review documentation files
3) Verify CSV files are present
4) Ensure Python 3.7+ is installed
5) Try restarting the application

---

**Enjoy connecting with your alumni community! 🎓✨**

