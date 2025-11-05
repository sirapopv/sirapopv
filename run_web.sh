#!/bin/bash
# Run the YouTube to Podcast Converter Web Interface

echo "🚀 Starting YouTube to Podcast Converter Web Interface..."
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check if streamlit is installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "⚠️  Streamlit not found. Installing dependencies..."
    pip install -r requirements.txt
fi

# Run Streamlit app
echo ""
echo "Opening web interface..."
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
