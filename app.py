#!/usr/bin/env python3
"""
YouTube Video to Podcast Converter - Web Interface
Streamlit-based UI for easy video conversion
"""

import streamlit as st
import os
import sys
from datetime import datetime
import yaml
from pathlib import Path

# Import our modules
from src.settings_manager import SettingsManager
from src.transcript import get_transcript
from src.translator import translate_transcript
from src.content_writer import generate_title_and_description
from src.audio_generator import generate_audio
from src.image_generator import generate_thumbnail
from src.video_creator import create_video, check_ffmpeg, get_video_duration

# Page configuration
st.set_page_config(
    page_title="YouTube to Podcast Converter",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize settings manager
if 'settings_manager' not in st.session_state:
    st.session_state.settings_manager = SettingsManager()

settings = st.session_state.settings_manager

# Load config
def load_config():
    try:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except:
        return {}

config = load_config()

# Sidebar - Settings
st.sidebar.title("⚙️ Settings")

# API Key Section
st.sidebar.subheader("🔑 API Key")
saved_api_key = settings.get_api_key()
api_key_input = st.sidebar.text_input(
    "Google AI Studio API Key",
    value=saved_api_key if saved_api_key else "",
    type="password",
    help="Enter your Google AI Studio API key. It will be saved securely."
)

if st.sidebar.button("💾 Save API Key"):
    if api_key_input:
        settings.set_api_key(api_key_input)
        st.sidebar.success("API Key saved!")
    else:
        st.sidebar.error("Please enter an API key")

if saved_api_key:
    st.sidebar.success("✅ API Key is configured")
    if st.sidebar.button("🗑️ Clear API Key"):
        settings.clear_api_key()
        st.sidebar.warning("API Key cleared. Please refresh the page.")
        st.rerun()

st.sidebar.markdown("---")

# Style Instructions Section
st.sidebar.subheader("✍️ Style Instructions")
saved_style = settings.get_style_instructions()
style_instructions = st.sidebar.text_area(
    "Translation Style Instructions",
    value=saved_style if saved_style else config.get('translation', {}).get('style_instructions', ''),
    height=150,
    help="Describe how you want the content to be translated. E.g., 'Make it conversational and engaging for Thai podcast listeners.'"
)

if st.sidebar.button("💾 Save Style Instructions"):
    settings.set_style_instructions(style_instructions)
    st.sidebar.success("Style instructions saved!")

st.sidebar.markdown("---")

# Sample Script Section
st.sidebar.subheader("📄 Sample Script")
st.sidebar.write("Upload a sample script to help AI match your style")

# Show if sample script exists
if settings.has_sample_script():
    st.sidebar.success("✅ Sample script uploaded")
    if st.sidebar.button("👁️ View Sample Script"):
        st.session_state.show_sample = True
    if st.sidebar.button("🗑️ Delete Sample Script"):
        settings.delete_sample_script()
        st.sidebar.success("Sample script deleted")
        st.rerun()

# File uploader
uploaded_file = st.sidebar.file_uploader(
    "Upload Sample Script (.txt)",
    type=['txt'],
    help="Upload a text file with your preferred script style"
)

if uploaded_file is not None:
    content = uploaded_file.read().decode('utf-8')
    settings.set_sample_script(content)
    st.sidebar.success(f"Sample script saved! ({len(content)} characters)")
    st.rerun()

st.sidebar.markdown("---")

# Other Settings
st.sidebar.subheader("🎨 Other Settings")
language = st.sidebar.selectbox(
    "Target Language",
    ["Thai", "English", "Japanese", "Korean", "Chinese"],
    index=0
)

thumbnail_style = st.sidebar.selectbox(
    "Thumbnail Style",
    ["modern", "minimal", "vibrant"],
    index=0
)

# Main Content
st.title("🎙️ YouTube to Podcast Converter")
st.markdown("Convert YouTube videos into podcast-style videos automatically with AI")

# Check ffmpeg
if not check_ffmpeg():
    st.error("⚠️ **ffmpeg is not installed!**")
    st.code("""
    # Install ffmpeg:
    Ubuntu/Debian: sudo apt-get install ffmpeg
    MacOS: brew install ffmpeg
    """)
    st.stop()

# Check API key
if not settings.get_api_key():
    st.warning("⚠️ Please enter your Google AI Studio API key in the sidebar")
    st.info("👈 Enter your API key in the sidebar to get started")
    st.markdown("---")
    st.markdown("### How to get API Key:")
    st.markdown("1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)")
    st.markdown("2. Create or select a project")
    st.markdown("3. Generate an API key")
    st.markdown("4. Copy and paste it in the sidebar")
    st.stop()

# Show sample script if requested
if st.session_state.get('show_sample', False):
    with st.expander("📄 Current Sample Script", expanded=True):
        st.text_area(
            "Sample Script Content",
            value=settings.get_sample_script(),
            height=300,
            disabled=True
        )
        if st.button("Close"):
            st.session_state.show_sample = False
            st.rerun()

# Main conversion form
st.markdown("---")
st.subheader("🎬 Convert Video")

youtube_url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=...",
    help="Paste the YouTube video URL you want to convert"
)

col1, col2, col3 = st.columns([1, 1, 3])
with col1:
    convert_button = st.button("🚀 Convert Video", type="primary", use_container_width=True)
with col2:
    clear_button = st.button("🔄 Clear", use_container_width=True)

if clear_button:
    st.rerun()

if convert_button:
    if not youtube_url:
        st.error("Please enter a YouTube URL")
    else:
        try:
            # Create output directory
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)

            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Step 1: Extract transcript
            status_text.text("Step 1/6: Extracting transcript...")
            progress_bar.progress(10)

            transcript_data = get_transcript(youtube_url)
            video_id = transcript_data['video_id']
            transcript = transcript_data['transcript']

            st.success(f"✅ Transcript extracted ({len(transcript)} characters)")
            progress_bar.progress(20)

            # Step 2: Translate
            status_text.text(f"Step 2/6: Translating to {language}...")

            # Get style instructions and sample script
            style_inst = settings.get_style_instructions()
            sample_script = settings.get_sample_script() if settings.has_sample_script() else ""

            translated_text = translate_transcript(
                transcript=transcript,
                api_key=settings.get_api_key(),
                target_language=language,
                style_instructions=style_inst,
                script_example=sample_script,
                model=config.get('gemini', {}).get('model', 'gemini-2.0-flash-exp')
            )

            st.success(f"✅ Translation completed ({len(translated_text)} characters)")
            progress_bar.progress(35)

            # Step 3: Generate title and description
            status_text.text("Step 3/6: Generating title & description...")

            content_config = config.get('content_generation', {})
            title, description = generate_title_and_description(
                translated_text=translated_text,
                api_key=settings.get_api_key(),
                language=language,
                title_prompt=content_config.get('title_prompt', ''),
                description_prompt=content_config.get('description_prompt', ''),
                model=config.get('gemini', {}).get('model', 'gemini-2.0-flash-exp')
            )

            st.success(f"✅ Title: {title}")
            progress_bar.progress(50)

            # Create filenames
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_filename = f"{video_id}_{timestamp}"

            # Step 4: Generate audio
            status_text.text("Step 4/6: Generating audio...")

            audio_path = output_dir / f"{base_filename}.mp3"
            lang_code = "th" if language.lower() in ["thai", "ไทย"] else "en"

            generate_audio(
                text=translated_text,
                output_path=str(audio_path),
                language=lang_code
            )

            st.success(f"✅ Audio generated")
            progress_bar.progress(65)

            # Step 5: Generate thumbnail
            status_text.text("Step 5/6: Generating thumbnail...")

            image_path = output_dir / f"{base_filename}.jpg"
            generate_thumbnail(
                title=title,
                output_path=str(image_path),
                width=1280,
                height=720,
                style=thumbnail_style
            )

            st.success(f"✅ Thumbnail generated")
            progress_bar.progress(80)

            # Step 6: Create video
            status_text.text("Step 6/6: Creating video...")

            video_path = output_dir / f"{base_filename}.mp4"
            create_video(
                audio_path=str(audio_path),
                image_path=str(image_path),
                output_path=str(video_path),
                fps=1
            )

            duration = get_video_duration(str(video_path))
            duration_str = f"{int(duration)}s" if duration else "unknown"

            progress_bar.progress(100)
            status_text.text("✅ Conversion complete!")

            # Success message
            st.balloons()
            st.success("🎉 Video conversion completed successfully!")

            # Display results
            st.markdown("---")
            st.subheader("📊 Results")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**📝 Title:**")
                st.info(title)

                st.markdown("**📄 Description:**")
                st.text_area("", description, height=150, disabled=True)

                st.markdown("**⏱️ Duration:**")
                st.write(duration_str)

            with col2:
                st.markdown("**🖼️ Thumbnail:**")
                st.image(str(image_path), use_container_width=True)

            # Download section
            st.markdown("---")
            st.subheader("⬇️ Download Files")

            col1, col2, col3 = st.columns(3)

            with col1:
                with open(video_path, 'rb') as f:
                    st.download_button(
                        "📹 Download Video",
                        f,
                        file_name=f"{base_filename}.mp4",
                        mime="video/mp4",
                        use_container_width=True
                    )

            with col2:
                with open(audio_path, 'rb') as f:
                    st.download_button(
                        "🎵 Download Audio",
                        f,
                        file_name=f"{base_filename}.mp3",
                        mime="audio/mp3",
                        use_container_width=True
                    )

            with col3:
                with open(image_path, 'rb') as f:
                    st.download_button(
                        "🖼️ Download Thumbnail",
                        f,
                        file_name=f"{base_filename}.jpg",
                        mime="image/jpeg",
                        use_container_width=True
                    )

            # Save metadata
            metadata_path = output_dir / f"{base_filename}_metadata.txt"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                f.write(f"Video ID: {video_id}\n")
                f.write(f"Original URL: {youtube_url}\n")
                f.write(f"Title: {title}\n")
                f.write(f"Description:\n{description}\n")
                f.write(f"\n--- Translated Script ---\n{translated_text}\n")

            with open(metadata_path, 'r', encoding='utf-8') as f:
                st.download_button(
                    "📄 Download Metadata",
                    f,
                    file_name=f"{base_filename}_metadata.txt",
                    mime="text/plain",
                    use_container_width=True
                )

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            with st.expander("Show error details"):
                import traceback
                st.code(traceback.format_exc())

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>YouTube to Podcast Converter v1.0 | Built with Streamlit & Google Gemini</p>
        <p>Make sure to respect copyright and YouTube's Terms of Service</p>
    </div>
    """,
    unsafe_allow_html=True
)
