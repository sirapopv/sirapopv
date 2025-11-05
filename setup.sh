#!/bin/bash
# Setup script for YouTube Video to Podcast Converter

echo "🚀 Setting up YouTube Video to Podcast Converter..."
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi
echo "✅ Python is installed"
echo ""

# Check ffmpeg
echo "Checking ffmpeg..."
ffmpeg -version > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️  ffmpeg is not installed."
    echo "Please install it:"
    echo "  Ubuntu/Debian: sudo apt-get install ffmpeg"
    echo "  MacOS: brew install ffmpeg"
    echo ""
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✅ ffmpeg is installed"
fi
echo ""

# Create virtual environment (optional but recommended)
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo "✅ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your GEMINI_API_KEY"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

# Create output directory
mkdir -p output
echo "✅ Output directory created"
echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your GEMINI_API_KEY"
echo "2. (Optional) Customize config.yaml"
echo "3. Run: python main.py \"<youtube_url>\""
echo ""
echo "For more info, see README.md"
