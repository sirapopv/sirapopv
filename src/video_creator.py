"""
Video Creator Module
Step 7: Combine audio and image to create video using ffmpeg
"""

import subprocess
import os
from typing import Optional


def check_ffmpeg() -> bool:
    """Check if ffmpeg is installed"""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def create_video(
    audio_path: str,
    image_path: str,
    output_path: str,
    fps: int = 1,
    video_codec: str = "libx264",
    audio_codec: str = "aac"
) -> str:
    """
    Create video by combining audio and static image using ffmpeg

    Args:
        audio_path: Path to audio file (mp3, wav, etc.)
        image_path: Path to image file (jpg, png, etc.)
        output_path: Path where video will be saved
        fps: Frames per second (default: 1, sufficient for static image)
        video_codec: Video codec (default: libx264)
        audio_codec: Audio codec (default: aac)

    Returns:
        Path to the generated video file

    Raises:
        Exception: If ffmpeg is not installed or video creation fails
    """
    # Check if ffmpeg is installed
    if not check_ffmpeg():
        raise Exception(
            "ffmpeg is not installed. Please install it:\n"
            "Ubuntu/Debian: sudo apt-get install ffmpeg\n"
            "MacOS: brew install ffmpeg\n"
            "Or visit: https://ffmpeg.org/download.html"
        )

    # Verify input files exist
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Build ffmpeg command
    # -loop 1: Loop the image
    # -i image: Input image
    # -i audio: Input audio
    # -c:v libx264: Video codec
    # -tune stillimage: Optimize for still image
    # -c:a aac: Audio codec
    # -b:a 192k: Audio bitrate
    # -pix_fmt yuv420p: Pixel format for compatibility
    # -shortest: End video when audio ends
    # -movflags +faststart: Enable fast start for web playback

    command = [
        "ffmpeg",
        "-y",  # Overwrite output file if exists
        "-loop", "1",  # Loop the image
        "-framerate", str(fps),
        "-i", image_path,  # Input image
        "-i", audio_path,  # Input audio
        "-c:v", video_codec,  # Video codec
        "-tune", "stillimage",  # Optimize for still image
        "-c:a", audio_codec,  # Audio codec
        "-b:a", "192k",  # Audio bitrate
        "-pix_fmt", "yuv420p",  # Pixel format for compatibility
        "-shortest",  # End video when audio ends
        "-movflags", "+faststart",  # Fast start for web
        output_path
    ]

    try:
        # Run ffmpeg
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )

        # Verify output file was created
        if not os.path.exists(output_path):
            raise Exception(f"Video file was not created at {output_path}")

        # Get file size
        file_size = os.path.getsize(output_path)
        if file_size == 0:
            raise Exception("Video file is empty")

        return output_path

    except subprocess.CalledProcessError as e:
        error_msg = f"ffmpeg failed with error:\n{e.stderr}"
        raise Exception(error_msg)


def get_video_duration(video_path: str) -> Optional[float]:
    """
    Get duration of video in seconds using ffprobe

    Args:
        video_path: Path to video file

    Returns:
        Duration in seconds or None if failed
    """
    try:
        command = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            video_path
        ]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )

        return float(result.stdout.strip())

    except Exception:
        return None


if __name__ == "__main__":
    # Test the module
    print("Testing video creator module...")

    if not check_ffmpeg():
        print("ERROR: ffmpeg is not installed")
        exit(1)

    print("ffmpeg is installed ✓")

    # Note: This test requires actual audio and image files
    # Create dummy files for testing if needed
    print("\nTo test video creation, provide:")
    print("1. Audio file path (mp3, wav)")
    print("2. Image file path (jpg, png)")
    print("\nThen call: create_video(audio_path, image_path, 'output.mp4')")
