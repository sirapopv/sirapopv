# Troubleshooting Guide - Installation Issues

This guide helps you fix common installation problems.

---

## 🔴 Problem: "Failed to install dependencies"

### Solution 1: Check Internet Connection

Make sure you have a stable internet connection. Try opening a website to verify.

### Solution 2: Install with Increased Timeout

```cmd
REM Open command prompt in project folder
venv\Scripts\activate
pip install --timeout=120 -r requirements.txt
```

### Solution 3: Install Packages One by One

If the full install fails, try installing packages individually:

```cmd
REM Activate virtual environment
venv\Scripts\activate

REM Install packages one by one
pip install youtube-transcript-api
pip install yt-dlp
pip install google-generativeai
pip install gtts
pip install Pillow
pip install pyyaml
pip install python-dotenv
pip install click
pip install rich
pip install streamlit
```

### Solution 4: Clear Pip Cache

```cmd
venv\Scripts\activate
pip cache purge
pip install -r requirements.txt
```

### Solution 5: Use Alternative Package Index

If PyPI is slow or blocked in your region:

```cmd
venv\Scripts\activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Solution 6: Install Without Optional Dependencies

```cmd
venv\Scripts\activate
pip install --no-deps -r requirements.txt
pip install -r requirements.txt
```

---

## 🔴 Problem: "Python is not recognized"

### Solution 1: Python Not Installed

1. Download from: https://www.python.org/downloads/
2. Run installer
3. **CHECK** "Add Python to PATH"
4. Click "Install Now"

### Solution 2: Python Installed but Not in PATH

**Windows 10/11:**

1. Press `Win + X` → "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "System variables", find "Path"
5. Click "Edit"
6. Click "New"
7. Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311` (adjust version)
8. Add another: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts`
9. Click OK on all windows
10. **Close and reopen** command prompt
11. Test: `python --version`

### Solution 3: Use Python Launcher

If Python is installed but `python` command doesn't work, try `py`:

```cmd
py --version
py -m venv venv
```

Then edit START.bat and replace `python` with `py`.

---

## 🔴 Problem: "pip is not recognized"

### Solution 1: Reinstall pip

```cmd
python -m ensurepip --default-pip
python -m pip install --upgrade pip
```

### Solution 2: Use python -m pip

Instead of `pip install`, use:

```cmd
python -m pip install -r requirements.txt
```

---

## 🔴 Problem: "Failed to create virtual environment"

### Solution 1: Check Permissions

Run command prompt as Administrator:
1. Right-click Command Prompt
2. Select "Run as Administrator"
3. Navigate to project folder
4. Run SETUP.bat

### Solution 2: Check Antivirus

Temporarily disable antivirus and try again. Some antivirus programs block Python from creating files.

### Solution 3: Use Different Location

Move project folder to a simpler path:
- ❌ Bad: `C:\Users\MyName\Documents\My Projects\youtube-converter`
- ✅ Good: `C:\youtube-converter`

### Solution 4: Manually Create venv

```cmd
python -m venv venv --clear
```

---

## 🔴 Problem: "ffmpeg is not installed"

### Solution 1: Using Chocolatey (Easiest)

First, install Chocolatey (if not installed):
1. Open PowerShell as Administrator
2. Run:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
3. Close PowerShell
4. Open new Command Prompt as Administrator
5. Run: `choco install ffmpeg`

### Solution 2: Using winget (Windows 10/11)

```cmd
winget install ffmpeg
```

### Solution 3: Manual Installation

1. Go to: https://www.gyan.dev/ffmpeg/builds/
2. Download: "ffmpeg-release-essentials.zip"
3. Extract to `C:\ffmpeg`
4. Add to PATH:
   - Press `Win + X` → "System"
   - "Advanced system settings"
   - "Environment Variables"
   - Edit "Path"
   - Add: `C:\ffmpeg\bin`
5. Close and reopen command prompt
6. Test: `ffmpeg -version`

### Solution 4: Verify PATH

```cmd
echo %PATH%
```

Check if ffmpeg path is listed. If not, add it to PATH (see Solution 3).

---

## 🔴 Problem: "Module not found" when running START.bat

### Solution 1: Activate Virtual Environment

Make sure virtual environment is activated:

```cmd
venv\Scripts\activate
```

You should see `(venv)` at the start of your command prompt.

### Solution 2: Reinstall Requirements

```cmd
venv\Scripts\activate
pip install -r requirements.txt --force-reinstall
```

### Solution 3: Check Virtual Environment

Delete and recreate:

```cmd
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔴 Problem: "SSL Certificate Error"

### Solution 1: Update Certificates

```cmd
pip install --upgrade certifi
```

### Solution 2: Use HTTP (Temporary)

```cmd
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

**Warning:** Only use this as a last resort.

---

## 🔴 Problem: "Permission Denied" errors

### Solution 1: Run as Administrator

Right-click SETUP.bat → "Run as Administrator"

### Solution 2: Check Folder Permissions

1. Right-click project folder
2. Properties → Security tab
3. Make sure your user has "Full Control"

### Solution 3: Disable Read-Only

1. Right-click project folder
2. Properties
3. Uncheck "Read-only"
4. Apply to all files and subfolders

---

## 🔴 Problem: Installation is very slow

### Solution 1: Use Faster Mirror

For users in Asia/China:

```cmd
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

For users in Europe:

```cmd
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
```

### Solution 2: Install Without Cache

```cmd
pip install --no-cache-dir -r requirements.txt
```

### Solution 3: Increase Timeout

```cmd
pip install --timeout=300 -r requirements.txt
```

---

## 🔴 Problem: "No module named 'streamlit'"

This means dependencies weren't installed properly.

### Solution: Reinstall Streamlit

```cmd
venv\Scripts\activate
pip install streamlit
```

Or reinstall everything:

```cmd
venv\Scripts\activate
pip install -r requirements.txt --force-reinstall
```

---

## 🔴 Problem: START.bat opens and immediately closes

### Solution 1: Check if Setup Completed

Run SETUP.bat again and make sure it completes without errors.

### Solution 2: Run from Command Prompt

1. Open Command Prompt
2. Navigate to project folder:
   ```cmd
   cd C:\path\to\youtube-converter
   ```
3. Run:
   ```cmd
   START.bat
   ```
4. Check error messages

### Solution 3: Manually Start

```cmd
cd C:\path\to\youtube-converter
venv\Scripts\activate
streamlit run app.py
```

---

## 🔴 Problem: Port 8501 already in use

### Solution 1: Kill Existing Process

```cmd
netstat -ano | findstr :8501
taskkill /PID [PID_NUMBER] /F
```

Replace [PID_NUMBER] with the number from the first command.

### Solution 2: Use Different Port

Edit START.bat and change the last line to:

```cmd
streamlit run app.py --server.port 8502
```

---

## 🔴 Problem: Browser doesn't open automatically

### Solution 1: Open Manually

After running START.bat, open your browser and go to:
```
http://localhost:8501
```

### Solution 2: Check if App is Running

Look for message in command prompt:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
```

If you see this, the app is running. Just open the URL manually.

---

## 🔴 Problem: Windows Defender SmartScreen blocks SETUP.bat

### Solution: Allow the Script

1. Click "More info"
2. Click "Run anyway"

This is safe - Windows blocks unknown scripts by default.

---

## 🔴 Problem: "VCRUNTIME140.dll is missing"

### Solution: Install Visual C++ Redistributables

Download and install:
https://aka.ms/vs/17/release/vc_redist.x64.exe

---

## 🔴 Problem: Everything installs but app shows errors

### Solution 1: Check API Key

Make sure you entered your Google Gemini API key in the sidebar.

### Solution 2: Check ffmpeg

The app needs ffmpeg for video creation. Install it:
```cmd
choco install ffmpeg
```

Or see ffmpeg solutions above.

### Solution 3: Check Internet

Make sure you have internet connection. The app needs it to:
- Call Google Gemini API
- Download YouTube videos

---

## 💡 Still Having Issues?

### Create a Fresh Installation

1. Delete the entire project folder
2. Download fresh copy
3. Extract to: `C:\youtube-converter` (simple path)
4. Run SETUP.bat as Administrator

### Check System Requirements

- Windows 10 or newer
- Python 3.8 or newer
- 4GB RAM minimum (8GB recommended)
- Internet connection
- 2GB free disk space

### Alternative: Use Linux Subsystem (WSL)

If Windows installation continues to fail, try WSL:

1. Install WSL2
2. Install Ubuntu from Microsoft Store
3. Follow Linux installation instructions

---

## 📧 Get More Help

If none of these solutions work:

1. **Check the error message carefully**
2. **Copy the full error message**
3. **Note which step failed**
4. **Check your Python version:** `python --version`
5. **Check your pip version:** `pip --version`

Common error patterns:
- Network errors → Check internet/firewall
- Permission errors → Run as Administrator
- Path errors → Move to simpler folder path
- Module errors → Reinstall requirements

---

## 🔧 Manual Installation (Advanced)

If automated setup keeps failing, try manual setup:

```cmd
REM 1. Create virtual environment
python -m venv venv

REM 2. Activate it
venv\Scripts\activate

REM 3. Upgrade pip
python -m pip install --upgrade pip

REM 4. Install wheel (helps with binary packages)
pip install wheel

REM 5. Install packages one by one
pip install youtube-transcript-api==0.6.2
pip install yt-dlp==2024.8.6
pip install google-generativeai==0.8.3
pip install gtts==2.5.4
pip install Pillow==10.4.0
pip install pyyaml==6.0.2
pip install python-dotenv==1.0.1
pip install click==8.1.7
pip install rich==13.9.4
pip install streamlit==1.32.2

REM 6. Create directories
mkdir output
mkdir settings

REM 7. Test run
streamlit run app.py
```

---

**Most issues can be solved by:**
1. Running as Administrator
2. Checking internet connection
3. Installing to simple path (C:\youtube-converter)
4. Using latest Python version
5. Clearing pip cache

Good luck! 🚀
