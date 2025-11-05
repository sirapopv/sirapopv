@echo off
REM YouTube to Podcast Converter - Windows Launcher
REM Double-click this file to start the app

echo ========================================
echo   YouTube to Podcast Converter
echo ========================================
echo.
echo Starting application...
echo.
echo The app will open in your browser automatically.
echo Keep this window open while using the app.
echo.
echo To stop: Close this window or press Ctrl+C
echo ========================================
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo WARNING: Virtual environment not found.
    echo Please run SETUP.bat first!
    echo.
    pause
    exit /b 1
)

REM Start Streamlit
streamlit run app.py

pause
