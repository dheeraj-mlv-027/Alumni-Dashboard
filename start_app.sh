#!/bin/bash

echo "🎓 Alumni Network Portal - Starting Application..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found!"
    exit 1
fi

# Check if CSV files exist
if [ ! -f "alumni_master (2).csv" ]; then
    echo "❌ alumni_master (2).csv not found!"
    exit 1
fi

if [ ! -f "job_history (2).csv" ]; then
    echo "❌ job_history (2).csv not found!"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt -q

# Check if streamlit was installed successfully
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit installation failed!"
    exit 1
fi

echo ""
echo "✅ All checks passed!"
echo ""
echo "🚀 Starting Streamlit application..."
echo ""
echo "📱 The application will open in your default browser."
echo "🔗 If it doesn't, navigate to: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application."
echo ""

# Run the Streamlit app
streamlit run alumni_dashboard_app.py

