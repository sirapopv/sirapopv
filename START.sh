#!/bin/bash
# YouTube to Podcast Converter - Linux/Mac Launcher
# Run this to start the app

echo "========================================"
echo "  YouTube to Podcast Converter"
echo "========================================"
echo ""
echo "Starting application..."
echo ""
echo "The app will open in your browser automatically."
echo "Keep this terminal open while using the app."
echo ""
echo "To stop: Press Ctrl+C"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "ERROR: Virtual environment not found."
    echo "Please run ./SETUP.sh first!"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# Start Streamlit
streamlit run app.py

# Keep terminal open if there's an error
if [ $? -ne 0 ]; then
    echo ""
    echo "An error occurred."
    read -p "Press Enter to exit..."
fi
