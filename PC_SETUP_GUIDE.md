# PC Setup Guide - Run Locally on Your Computer

Use the YouTube to Podcast Converter directly on your Windows, Mac, or Linux PC with a simple graphical interface!

**No website needed - runs completely on your computer!**

---

## 🖥️ Windows Setup (Simple!)

### Step 1: Install Prerequisites (One-time)

#### A. Install Python

1. Download Python from: https://www.python.org/downloads/
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Click "Install Now"

#### B. Install ffmpeg

**Option 1 - Using Chocolatey (Easiest):**
```cmd
choco install ffmpeg
```

**Option 2 - Manual:**
1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Get "ffmpeg-release-essentials.zip"
3. Extract to `C:\ffmpeg`
4. Add to PATH:
   - Search "Environment Variables" in Windows
   - Edit "Path" variable
   - Add: `C:\ffmpeg\bin`

### Step 2: Setup Application (One-time)

1. **Download/Extract** this project to a folder (e.g., `C:\youtube-converter`)

2. **Double-click `SETUP.bat`**
   - Installs all dependencies
   - Takes 2-5 minutes
   - Only needs to run once!

3. **Get API Key**
   - Go to: https://makersuite.google.com/app/apikey
   - Create API key
   - Copy it (you'll enter it in the app)

### Step 3: Run the Application

**Option A - Double-click `START.bat`**
- Opens automatically in browser
- Simple interface
- Use anytime!

**Option B - Create Desktop Shortcut**
1. Double-click `CREATE_SHORTCUT.bat`
2. A shortcut appears on your desktop
3. Double-click shortcut to launch!

### Step 4: Use the App

1. App opens in your web browser (but runs locally!)
2. **First time only:** Enter API key in sidebar → Click Save
3. Paste YouTube URL
4. Click "Convert Video"
5. Download your files!

**That's it!** Your settings are saved forever - just launch and use!

---

## 🍎 Mac Setup

### Step 1: Install Prerequisites

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and ffmpeg
brew install python3 ffmpeg
```

### Step 2: Setup Application

```bash
# Navigate to project folder
cd ~/Downloads/youtube-converter

# Run setup
chmod +x SETUP-LINUX.sh
./SETUP-LINUX.sh
```

### Step 3: Get API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Create and copy API key

### Step 4: Run the App

```bash
# Run this anytime you want to use it
./START.sh
```

Or create alias in `~/.zshrc`:
```bash
alias podcast='cd ~/path/to/youtube-converter && ./START.sh'
```

Then just type `podcast` in terminal!

---

## 🐧 Linux Setup

### Step 1: Install Prerequisites

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv ffmpeg git

# Fedora
sudo dnf install python3 python3-pip ffmpeg git

# Arch
sudo pacman -S python python-pip ffmpeg git
```

### Step 2: Setup Application

```bash
# Navigate to project folder
cd ~/youtube-converter

# Run setup
chmod +x SETUP-LINUX.sh
./SETUP-LINUX.sh
```

### Step 3: Get API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Create and copy API key

### Step 4: Run the App

```bash
./START.sh
```

**Create desktop shortcut:**
```bash
# Create .desktop file
cat > ~/.local/share/applications/youtube-converter.desktop << EOF
[Desktop Entry]
Name=YouTube Podcast Converter
Exec=/path/to/youtube-converter/START.sh
Type=Application
Terminal=true
Icon=multimedia-video-player
Categories=AudioVideo;
EOF
```

---

## 📖 How to Use the Interface

### First Time Setup (In the App)

1. **Launch the app** (START.bat or START.sh)
2. **Browser opens** automatically to `http://localhost:8501`
3. **Sidebar → API Key section:**
   - Paste your Google Gemini API key
   - Click "💾 Save API Key"
   - ✅ Done! Never need to enter again

### Optional: Customize Translation

**Add Style Instructions:**
- Sidebar → "Style Instructions"
- Example: "Make it conversational, use simple Thai language"
- Click "💾 Save"

**Upload Sample Script:**
- Sidebar → "Sample Script"
- Upload a .txt file with your preferred writing style
- AI will match your style

### Converting Videos

1. **Paste YouTube URL** in the main field
2. **Select options:**
   - Language: Thai, English, etc.
   - Thumbnail Style: modern, minimal, vibrant
3. **Click "🚀 Convert Video"**
4. **Wait 1-3 minutes** (progress bar shows status)
5. **Download files:**
   - 📹 Video (MP4)
   - 🎵 Audio (MP3)
   - 🖼️ Thumbnail (JPG)
   - 📄 Metadata (title, description, script)

### Where Are Files Saved?

Files are in the `output/` folder in your project directory:
```
youtube-converter/
└── output/
    ├── VIDEO_ID_20240101_120000.mp4
    ├── VIDEO_ID_20240101_120000.mp3
    ├── VIDEO_ID_20240101_120000.jpg
    └── VIDEO_ID_20240101_120000_metadata.txt
```

---

## 💡 Tips & Tricks

### Faster Startup

**Windows:**
Pin `START.bat` to taskbar for one-click access

**Mac/Linux:**
Create terminal alias:
```bash
alias podcast='cd ~/youtube-converter && ./START.sh'
```

### Batch Processing

Keep app open and convert multiple videos one after another!

### Editing Settings

All settings saved in `settings/` folder:
- `app_settings.json` - API key, preferences
- `sample_script.txt` - Your sample script

### Backing Up Settings

```bash
# Backup
cp -r settings settings_backup

# Restore
cp -r settings_backup settings
```

---

## 🔧 Troubleshooting

### "Python is not recognized"
- Reinstall Python
- **Check** "Add Python to PATH" during installation
- Restart computer

### "ffmpeg is not installed"
- Install ffmpeg (see Step 1)
- Restart terminal/command prompt
- Test: `ffmpeg -version`

### "Module not found" error
- Run `SETUP.bat` (Windows) or `./SETUP-LINUX.sh` (Mac/Linux) again

### App won't start
```bash
# Windows
cd path\to\youtube-converter
venv\Scripts\activate
pip install --upgrade -r requirements.txt

# Mac/Linux
cd path/to/youtube-converter
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Port already in use
- Close any running instances
- Open Task Manager → End "Python" processes
- Try again

### Can't save API key
- Check `settings/` folder exists
- Check folder permissions
- Try running as administrator (Windows)

---

## 🚫 Stopping the App

**Windows:**
- Close the command prompt window
- Or press `Ctrl+C` in the window

**Mac/Linux:**
- Press `Ctrl+C` in terminal
- Or close terminal window

---

## 🔄 Updating

When new features are added:

```bash
# Navigate to project folder
cd youtube-converter

# Pull updates
git pull

# Update dependencies
# Windows:
venv\Scripts\activate
pip install -r requirements.txt

# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

---

## ❓ Common Questions

**Q: Does this need internet?**
A: Yes, for API calls (Gemini AI) and downloading YouTube videos.

**Q: Is my API key safe?**
A: Yes! It's stored locally on your PC only. Never shared.

**Q: Can others access my app?**
A: No! It only runs on your PC (localhost). Private by default.

**Q: How much does it cost?**
A: The app is free. You only pay for Google Gemini API usage (very cheap, usually <$1/month for personal use).

**Q: Can I use this offline?**
A: No, requires internet for API and YouTube access.

**Q: Does it save my settings?**
A: Yes! API key, style instructions, and sample scripts are saved permanently.

---

## 📊 System Requirements

**Minimum:**
- Windows 10/11, macOS 10.14+, or Linux
- 4GB RAM
- 2GB free disk space
- Internet connection

**Recommended:**
- 8GB RAM
- SSD for faster processing
- Good internet connection

---

## 🎯 Quick Reference

### First Time:
1. Install Python + ffmpeg
2. Run `SETUP.bat` (Windows) or `./SETUP-LINUX.sh` (Mac/Linux)
3. Get API key from Google
4. Done!

### Every Time:
1. Double-click `START.bat` (Windows) or run `./START.sh` (Mac/Linux)
2. Paste YouTube URL
3. Click Convert
4. Download files!

---

## 🎉 You're Ready!

**Everything runs on YOUR PC - no website, no server, no deployment needed!**

The interface is simple and intuitive. Just launch, paste URLs, and convert!

Need help? Check the full documentation in README.md
