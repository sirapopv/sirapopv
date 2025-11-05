#!/bin/bash
# YouTube to Podcast Converter - Linux/Mac Setup
# Run this ONCE to set up everything

echo "========================================"
echo "  YouTube to Podcast Converter"
echo "  First-Time Setup"
echo "========================================"
echo ""
echo "This will install everything you need."
echo "This may take a few minutes..."
echo ""
read -p "Press Enter to continue..."

# Check Python
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo ""
    echo "ERROR: Python 3 is not installed!"
    echo ""
    echo "Install Python 3.8 or newer:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip python3-venv"
    echo "  macOS: brew install python3"
    echo ""
    exit 1
fi

echo "Python found!"
python3 --version
echo ""

# Check ffmpeg
echo "Checking ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo ""
    echo "WARNING: ffmpeg is not installed."
    echo ""
    echo "You need ffmpeg for video creation."
    echo ""
    echo "Install ffmpeg:"
    echo "  Ubuntu/Debian: sudo apt install ffmpeg"
    echo "  macOS: brew install ffmpeg"
    echo ""
    read -p "Continue anyway? (y/n): " continue
    if [ "$continue" != "y" ] && [ "$continue" != "Y" ]; then
        exit 1
    fi
else
    echo "ffmpeg found!"
    ffmpeg -version | head -n 1
fi
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists."
else
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Failed to create virtual environment."
        exit 1
    fi
    echo "Virtual environment created!"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing dependencies..."
echo "This may take a few minutes..."
echo ""
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies."
    exit 1
fi

# Create directories
echo ""
echo "Creating directories..."
mkdir -p output settings

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env 2>/dev/null || true
fi

# Make scripts executable
echo "Making scripts executable..."
chmod +x START.sh
chmod +x run_web.sh
chmod +x setup.sh

echo ""
echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Get your Google Gemini API key from:"
echo "   https://makersuite.google.com/app/apikey"
echo ""
echo "2. Run ./START.sh to launch the app"
echo ""
echo "3. Enter your API key in the app (only needed once)"
echo ""
echo "========================================"
echo ""
