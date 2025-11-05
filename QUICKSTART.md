# Quick Start Guide - Web Interface

Get started with the YouTube to Podcast Converter in 3 easy steps!

## Step 1: Setup (One-time)

### Install Dependencies

```bash
# Run the setup script
./setup.sh

# Or manually:
pip install -r requirements.txt
```

### Get Your API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the API key (you'll need it in Step 2)

## Step 2: Launch Web Interface

```bash
./run_web.sh
```

Your browser will open to `http://localhost:8501`

## Step 3: Configure Settings (First Time)

### 1. Add API Key 🔑

In the sidebar:
- Paste your Google AI Studio API key
- Click "💾 Save API Key"
- You'll see "✅ API Key is configured"

**Note:** Your API key is saved securely on your computer and never shared.

### 2. Add Style Instructions ✍️ (Optional but Recommended)

In the sidebar under "Style Instructions":
- Describe how you want content translated
- Example for Thai:
  ```
  แปลเนื้อหาให้เป็นภาษาไทยที่ฟังง่าย เหมือนพูดคุยกับเพื่อน
  ใช้คำง่ายๆ หลีกเลี่ยงศัพท์เทคนิคที่ยาก
  เพิ่มตัวอย่างประกอบถ้าเหมาะสม
  ```
- Click "💾 Save Style Instructions"

### 3. Upload Sample Script 📄 (Optional)

If you have a preferred script style:
- Click "Browse files" under "Sample Script"
- Upload your `.txt` file
- The AI will try to match your style

**Example sample script:**
```
สวัสดีครับผู้ฟังทุกคน วันนี้เรามีเรื่องน่าสนใจมาฝากกัน
เรื่องที่จะพูดถึงวันนี้คือ...
[Your preferred style here]
```

## Step 4: Convert Your First Video! 🎬

1. **Paste YouTube URL**
   - Copy any YouTube video URL
   - Paste it in the "YouTube URL" field

2. **Choose Settings** (Optional)
   - Target Language: Thai (default), English, etc.
   - Thumbnail Style: modern, minimal, or vibrant

3. **Click "🚀 Convert Video"**
   - Watch the progress bar
   - Wait 1-3 minutes depending on video length

4. **Download Your Files**
   - 📹 Download Video (MP4)
   - 🎵 Download Audio (MP3)
   - 🖼️ Download Thumbnail (JPG)
   - 📄 Download Metadata (title, description, script)

## Tips 💡

### Best Practices

1. **Start with short videos** (5-10 minutes) to test
2. **Refine your style instructions** based on results
3. **Keep your sample script** updated with your latest style
4. **Check the metadata file** for title and description before uploading to YouTube

### Troubleshooting

**"ffmpeg is not installed"**
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# MacOS
brew install ffmpeg
```

**"No transcript available"**
- Some videos don't have captions
- Try videos with auto-generated subtitles enabled

**Translation doesn't match my style**
- Add more detailed style instructions
- Upload a sample script with your preferred tone

**Audio sounds robotic**
- Currently using free gTTS
- For better quality, upgrade to Google Cloud TTS (advanced)

### Settings Are Saved! 💾

Good news! All your settings are saved automatically:
- ✅ API key
- ✅ Style instructions
- ✅ Sample script
- ✅ Language preferences

You only need to set them up once!

## Example Workflow

Here's a typical workflow:

1. **Morning**: Find 3-5 interesting YouTube videos
2. **Convert**: Paste URLs one by one, click convert
3. **Review**: Check titles, descriptions, and videos
4. **Edit** (optional): Adjust titles/descriptions if needed
5. **Upload**: Upload to your YouTube channel (Step 8 - coming soon!)

## Next Steps

### Customize Further

Edit `config.yaml` to adjust:
- Default language
- Title generation prompts
- Description templates
- Audio settings
- Video quality

### Batch Processing

Use the CLI for multiple videos:
```bash
# Create urls.txt with one URL per line
cat urls.txt | while read url; do
    python main.py "$url"
done
```

### Add YouTube Upload

Coming soon: Direct upload to YouTube!

## Need Help?

Check:
- `README.md` - Full documentation
- `config.yaml` - Configuration options
- Web interface help text (hover over ⓘ icons)

## Have Fun! 🎉

You're all set! Start converting videos and building your podcast library.

---

**Remember:** Respect copyright laws and YouTube's Terms of Service when converting content.
