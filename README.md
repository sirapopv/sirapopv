# YouTube Video to Podcast Converter

Automatically convert YouTube videos into podcast-style videos with translated audio and custom thumbnails.

## Features

- 🎥 Extract transcripts from YouTube videos
- 🌐 Translate content using Google Gemini AI
- 🎙️ Generate audio narration (Thai & English support)
- 🖼️ Create custom thumbnails automatically
- 📹 Combine into professional podcast videos
- 🌐 **Easy-to-use Web Interface**
- 💾 **Persistent settings** (API keys, style instructions, sample scripts)
- 🚀 **Deploy to your website** (Docker, Railway, Render, VPS)
- 🔒 **Optional password protection** for public deployment
- ⚙️ Highly configurable via YAML

## 🌐 Deploy to Your Website

Want to use this on your website instead of locally?

**Quick Deploy:** [DEPLOY_QUICK.md](DEPLOY_QUICK.md) - Get online in 5 minutes!

**Deployment Options:**
- **Railway.app** (Easiest) - One-click deploy, ~$5/month
- **Render.com** (Free tier) - Free with limitations
- **VPS** (Full control) - $4-12/month with automated setup script
- **Docker** (Any server) - Self-hosted with Docker Compose

**Full Guide:** [DEPLOYMENT.md](DEPLOYMENT.md) - Comprehensive deployment documentation

## How It Works

1. **Extract** - Pulls the transcript from YouTube video
2. **Translate** - Translates to your desired language with custom style
3. **Generate** - Creates engaging title and description
4. **Synthesize** - Generates audio from translated text
5. **Design** - Creates a custom thumbnail
6. **Compile** - Combines audio + image into MP4 video
7. **Ready** - Output ready for YouTube upload!

## Prerequisites

1. **Python 3.8+**
2. **ffmpeg** (for video processing)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install ffmpeg

   # MacOS
   brew install ffmpeg
   ```

3. **Google Gemini API Key**
   - Get your API key from: https://makersuite.google.com/app/apikey

## Installation

1. Clone or download this repository

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file with your API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

4. (Optional) Customize `config.yaml` for your preferences

## Usage

### 🌐 Web Interface (Recommended)

The easiest way to use the converter is through the web interface:

```bash
# Run the web interface
./run_web.sh

# Or manually:
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

**Web Interface Features:**
- ✅ Enter and save your Google AI Studio API key securely
- ✅ Add and save custom style instructions for translation
- ✅ Upload and save sample scripts to match your preferred style
- ✅ All settings are saved automatically
- ✅ Easy-to-use interface with progress tracking
- ✅ Download generated videos, audio, and thumbnails directly

### 💻 Command Line Interface

You can also use the CLI for automation:

```bash
# Basic usage
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Advanced options
```bash
# Specify language
python main.py "URL" --language Thai

# Change output directory
python main.py "URL" --output-dir my_videos

# Choose thumbnail style
python main.py "URL" --style vibrant

# All options
python main.py "URL" --language Thai --output-dir output --style modern
```

### Thumbnail Styles

- `modern` - Dark blue gradient (default)
- `minimal` - Clean white/gray
- `vibrant` - Purple/pink gradient

## Configuration

Edit `config.yaml` to customize:

- Default language
- Translation style instructions
- Script examples for style reference
- Audio settings (voice, speed, pitch)
- Image dimensions and style
- Video encoding settings

### Adding Custom Translation Style

Edit the `translation.style_instructions` in `config.yaml`:

```yaml
translation:
  style_instructions: |
    Translate naturally for Thai podcast listeners.
    Use conversational tone.
    Explain technical terms simply.
    Add relevant cultural context.
```

### Adding Script Examples

Add your preferred script style in `config.yaml`:

```yaml
translation:
  script_example: |
    [Your example script here]
    This helps the AI match your desired style.
```

## Output Files

For each video conversion, the following files are created:

- `{video_id}_{timestamp}.mp4` - Final video
- `{video_id}_{timestamp}.mp3` - Generated audio
- `{video_id}_{timestamp}.jpg` - Thumbnail image
- `{video_id}_{timestamp}_metadata.txt` - Title, description, and script

## Project Structure

```
youtube-video-converter/
├── main.py                  # Main CLI script
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── .env                     # API keys (create from .env.example)
├── src/
│   ├── transcript.py       # YouTube transcript extraction
│   ├── translator.py       # Gemini translation
│   ├── content_writer.py   # Title/description generation
│   ├── audio_generator.py  # Text-to-speech
│   ├── image_generator.py  # Thumbnail creation
│   └── video_creator.py    # Video assembly
└── output/                  # Generated files (created automatically)
```

## Examples

### Example 1: Convert English video to Thai podcast

```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --language Thai
```

### Example 2: Batch processing

```bash
# Create a file with URLs (one per line)
cat urls.txt | while read url; do
    python main.py "$url"
done
```

## Troubleshooting

### "GEMINI_API_KEY not found"
- Create `.env` file from `.env.example`
- Add your API key: `GEMINI_API_KEY=your_key_here`

### "ffmpeg is not installed"
- Install ffmpeg using package manager (see Prerequisites)

### "No transcript available"
- Some videos don't have transcripts/captions
- Try videos with auto-generated captions

### Audio quality issues
- Currently using free gTTS (Google Text-to-Speech)
- For better quality, implement Google Cloud TTS in `src/audio_generator.py`

## Future Enhancements

- [ ] YouTube upload automation (Step 8)
- [ ] Support for more languages
- [ ] Better audio quality (Google Cloud TTS)
- [ ] AI-generated thumbnails (Imagen API)
- [ ] Batch processing UI
- [ ] Progress resumption
- [ ] Video preview before upload

## Contributing

Feel free to improve this project:
1. Add features
2. Fix bugs
3. Improve documentation
4. Add tests

## License

MIT License - Feel free to use and modify

## Credits

Built with:
- Google Gemini API
- youtube-transcript-api
- gTTS (Google Text-to-Speech)
- ffmpeg
- Python Rich for beautiful CLI

---

**Note**: This tool is for personal use. Respect copyright and YouTube's Terms of Service when converting content.
