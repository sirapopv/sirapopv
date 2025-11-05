# Web Interface Guide

This guide explains all the features and fields in the web interface.

## Interface Layout

```
┌─────────────────────────────────────────────────────────────┐
│                    YouTube to Podcast Converter             │
│                                                             │
├──────────────┬──────────────────────────────────────────────┤
│              │                                              │
│  SIDEBAR     │           MAIN CONTENT AREA                 │
│              │                                              │
│  Settings    │  - YouTube URL Input                        │
│  ────────    │  - Convert Button                           │
│              │  - Progress Display                         │
│  🔑 API Key  │  - Results & Downloads                      │
│              │                                              │
│  ✍️ Style     │                                              │
│              │                                              │
│  📄 Script   │                                              │
│              │                                              │
│  🎨 Options  │                                              │
│              │                                              │
└──────────────┴──────────────────────────────────────────────┘
```

## Sidebar Components

### 1. 🔑 API Key Section

**Purpose:** Store your Google AI Studio API key securely

**Fields:**
- **API Key Input** (password field)
  - Type: Password (hidden text)
  - Purpose: Enter your Gemini API key
  - Storage: Saved to `settings/app_settings.json` (not in git)

**Buttons:**
- **💾 Save API Key** - Saves the key permanently
- **🗑️ Clear API Key** - Removes saved key (requires page refresh)

**Status:**
- Shows "✅ API Key is configured" when saved

**Example:**
```
Input: AIzaSyD...your-key-here...xyz
Click: 💾 Save API Key
Result: ✅ API Key is configured
```

---

### 2. ✍️ Style Instructions Section

**Purpose:** Customize how the AI translates content

**Fields:**
- **Translation Style Instructions** (text area)
  - Type: Multi-line text
  - Default: From `config.yaml`
  - Storage: Saved to `settings/app_settings.json`

**Button:**
- **💾 Save Style Instructions** - Saves instructions permanently

**What to Write:**
Describe your preferred translation style. Examples:

**For Thai Podcast:**
```
แปลให้เป็นภาษาไทยแบบสบายๆ ฟังง่าย
ใช้คำพูดในชีวิตประจำวัน ไม่เป็นทางการจนเกินไป
เพิ่มตัวอย่างประกอบถ้าเหมาะสม
อธิบายศัพท์เทคนิคให้เข้าใจง่าย
```

**For Professional Tone:**
```
Translate to Thai with a professional but approachable tone.
Maintain accuracy while making it engaging.
Explain technical terms clearly.
Use active voice when possible.
```

**For Educational Content:**
```
แปลเนื้อหาเพื่อการศึกษา
ใช้ภาษาที่ชัดเจน เข้าใจง่าย
แบ่งเนื้อหาเป็นหัวข้อย่อย
เน้นประเด็นสำคัญ
```

---

### 3. 📄 Sample Script Section

**Purpose:** Provide an example script for AI to match your style

**Features:**
- **Upload Sample Script** (.txt file)
  - Accepts: Text files only
  - Storage: Saved to `settings/sample_script.txt`
  - Persistent: Upload once, use forever

**Buttons:**
- **👁️ View Sample Script** - Display current sample
- **🗑️ Delete Sample Script** - Remove saved sample

**Status:**
- Shows "✅ Sample script uploaded" when saved

**How to Create a Good Sample Script:**

1. **Write in your target language** (e.g., Thai)
2. **Match your podcast style** (casual, professional, educational)
3. **Include typical elements:**
   - Opening greeting
   - Topic introduction
   - Main content structure
   - Closing

**Example Sample Script (Thai Podcast):**

```text
สวัสดีครับผู้ฟังทุกท่าน ยินดีต้อนรับเข้าสู่พอดแคสต์ของเราอีกครั้ง

วันนี้เรามีหัวข้อที่น่าสนใจมาฝากกัน เรื่องของเทคโนโลยีใหม่ๆ
ที่กำลังเปลี่ยนแปลงวิธีการใช้ชีวิตของเรา

เรามาเริ่มกันเลยดีกว่า...

[เนื้อหาหลัก - อธิบายประเด็นต่างๆ อย่างละเอียด]
- ใช้ตัวอย่างประกอบ
- อธิบายง่ายๆ ไม่ซับซ้อน
- ตั้งคำถามกับผู้ฟัง

สรุปง่ายๆ คือ...

ขอบคุณที่รับฟังครับ แล้วพบกันใหม่ครั้งหน้า
```

**Why Use Sample Scripts?**
- ✅ AI learns your writing style
- ✅ Consistent tone across all videos
- ✅ Better translation quality
- ✅ Matches your brand voice

---

### 4. 🎨 Other Settings

**Target Language**
- Options: Thai (default), English, Japanese, Korean, Chinese
- Purpose: Choose output language
- Note: Affects translation and audio generation

**Thumbnail Style**
- Options:
  - `modern` - Dark blue gradient, professional
  - `minimal` - Clean white/gray, simple
  - `vibrant` - Purple/pink gradient, colorful
- Purpose: Choose thumbnail design style
- Preview: See examples in generated videos

---

## Main Content Area

### YouTube URL Input

**Field:** YouTube URL
- Accepts: Any valid YouTube URL format
  - `https://www.youtube.com/watch?v=VIDEO_ID`
  - `https://youtu.be/VIDEO_ID`
  - `https://www.youtube.com/embed/VIDEO_ID`

### Convert Button

**🚀 Convert Video**
- Primary action button
- Starts the conversion process
- Shows progress bar during conversion

**🔄 Clear**
- Clears the form and resets

---

## Conversion Process Display

When converting, you'll see:

### Progress Bar
```
Step 1/6: Extracting transcript... [████████░░] 10%
✅ Transcript extracted (2,543 characters)

Step 2/6: Translating to Thai... [████████████] 35%
✅ Translation completed (3,127 characters)

...and so on
```

### Results Display

After conversion completes:

1. **📝 Title Section**
   - Shows generated video title
   - Optimized for YouTube (60 characters)

2. **📄 Description Section**
   - Full video description
   - Includes summary and key points
   - Ready to paste into YouTube

3. **⏱️ Duration**
   - Video length in seconds

4. **🖼️ Thumbnail Preview**
   - Visual preview of generated thumbnail
   - Shows actual design that will be used

---

## Download Section

After successful conversion, download:

### 📹 Download Video (.mp4)
- Complete podcast video
- Audio + thumbnail combined
- Ready for upload to YouTube

### 🎵 Download Audio (.mp3)
- Audio track only
- Use for podcast platforms (Spotify, Apple Podcasts)

### 🖼️ Download Thumbnail (.jpg)
- Thumbnail image
- Use as custom YouTube thumbnail
- 1280x720 resolution

### 📄 Download Metadata (.txt)
- Video title
- Description
- Full translated script
- Original URL and video ID

---

## Data Persistence

### What Gets Saved

All settings are saved automatically in the `settings/` directory:

```
settings/
├── app_settings.json      # API key, style instructions, preferences
└── sample_script.txt      # Your sample script
```

### What Doesn't Get Saved

- YouTube URLs (for privacy)
- Generated videos (saved to `output/` locally)
- Conversion history

### Resetting Settings

To reset all settings:
```bash
# Delete settings directory
rm -rf settings/

# Restart the app
./run_web.sh
```

---

## Tips for Best Results

### 1. API Key
- ✅ Get from Google AI Studio (free tier available)
- ✅ Save it once, use forever
- ✅ Keep it private (never share)

### 2. Style Instructions
- ✅ Be specific about tone (casual/professional)
- ✅ Mention target audience
- ✅ Include do's and don'ts
- ✅ Update based on results

### 3. Sample Script
- ✅ Write in your actual style
- ✅ Include 200-500 words
- ✅ Show your typical structure
- ✅ Update as your style evolves

### 4. Testing
- ✅ Start with short videos (5-10 min)
- ✅ Review first few conversions
- ✅ Adjust settings as needed
- ✅ Build a consistent style

---

## Keyboard Shortcuts

When focused on input fields:
- `Tab` - Move to next field
- `Ctrl/Cmd + Enter` - Submit form (when in URL field)
- `Esc` - Cancel current operation

---

## Privacy & Security

### Your Data
- ✅ API key stored locally only
- ✅ Settings never leave your computer
- ✅ No telemetry or tracking
- ✅ Source code is open and auditable

### Generated Content
- ✅ Saved locally in `output/` folder
- ✅ You have full control
- ✅ Delete anytime

---

## Troubleshooting

### Can't Save Settings
- Check file permissions on `settings/` directory
- Run: `chmod -R 755 settings/`

### API Key Not Working
- Verify key is correct (no extra spaces)
- Check Google AI Studio for quota
- Ensure key has Gemini API enabled

### Sample Script Not Loading
- Check file encoding (should be UTF-8)
- Verify file size (< 1MB recommended)
- Ensure file extension is `.txt`

---

## Advanced Usage

### Custom Configuration

Edit `config.yaml` for:
- Custom title generation prompts
- Description templates
- Audio settings (future: voice selection)
- Video quality settings

### Integration with CLI

Settings are compatible with CLI:
```bash
# Web UI saves to settings/
# CLI can read from settings/
python main.py "URL" --use-saved-settings
```

---

## Future Features (Coming Soon)

- [ ] YouTube direct upload
- [ ] Batch processing UI
- [ ] Voice customization
- [ ] AI-generated thumbnails (Imagen)
- [ ] Multiple sample scripts
- [ ] Template presets
- [ ] Preview before download

---

Need more help? Check `QUICKSTART.md` or `README.md`
