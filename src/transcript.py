"""
YouTube Transcript Extraction Module
Step 2: Pull the transcript from a YouTube video
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re
from typing import Optional


def extract_video_id(youtube_url: str) -> Optional[str]:
    """
    Extract video ID from various YouTube URL formats

    Args:
        youtube_url: YouTube video URL

    Returns:
        Video ID or None if not found
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?]*)',
        r'youtube\.com\/embed\/([^&\n?]*)',
        r'youtube\.com\/v\/([^&\n?]*)'
    ]

    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)

    return None


def get_transcript(youtube_url: str, language: str = 'en') -> dict:
    """
    Get transcript from YouTube video

    Args:
        youtube_url: YouTube video URL
        language: Preferred language code (default: 'en')

    Returns:
        Dictionary containing:
            - transcript: Full transcript text
            - video_id: YouTube video ID
            - language: Language code of the transcript
            - raw_transcript: Raw transcript data with timestamps
    """
    video_id = extract_video_id(youtube_url)

    if not video_id:
        raise ValueError(f"Could not extract video ID from URL: {youtube_url}")

    try:
        # Try to get transcript in preferred language
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # First try to get manually created transcript in preferred language
        try:
            transcript = transcript_list.find_manually_created_transcript([language])
        except:
            # If not available, try auto-generated in preferred language
            try:
                transcript = transcript_list.find_generated_transcript([language])
            except:
                # Fall back to any available transcript
                transcript = transcript_list.find_transcript(['en'])

        # Fetch the actual transcript data
        raw_transcript = transcript.fetch()

        # Format as plain text
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(raw_transcript)

        return {
            'transcript': transcript_text,
            'video_id': video_id,
            'language': transcript.language_code,
            'raw_transcript': raw_transcript,
            'is_generated': transcript.is_generated,
            'url': youtube_url
        }

    except Exception as e:
        raise Exception(f"Error fetching transcript for video {video_id}: {str(e)}")


if __name__ == "__main__":
    # Test the module
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = get_transcript(test_url)
    print(f"Video ID: {result['video_id']}")
    print(f"Language: {result['language']}")
    print(f"Transcript length: {len(result['transcript'])} characters")
    print(f"\nFirst 200 characters:\n{result['transcript'][:200]}...")
