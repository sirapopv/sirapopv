"""
Audio Generation Module
Step 5: Generate audio from translated text

Note: Currently using gTTS (Google Text-to-Speech) which is free.
For higher quality, consider upgrading to Google Cloud Text-to-Speech API.
"""

from gtts import gTTS
import os
from typing import Optional


def generate_audio(
    text: str,
    output_path: str,
    language: str = "th",
    slow: bool = False
) -> str:
    """
    Generate audio file from text using gTTS

    Args:
        text: Text to convert to speech
        output_path: Path where audio file will be saved
        language: Language code (default: "th" for Thai)
        slow: Speak slowly (default: False)

    Returns:
        Path to the generated audio file
    """
    try:
        # Create TTS object
        tts = gTTS(text=text, lang=language, slow=slow)

        # Save audio file
        tts.save(output_path)

        if not os.path.exists(output_path):
            raise Exception(f"Audio file was not created at {output_path}")

        return output_path

    except Exception as e:
        raise Exception(f"Error generating audio: {str(e)}")


def generate_audio_cloud_tts(
    text: str,
    output_path: str,
    api_key: str,
    language_code: str = "th-TH",
    voice_name: str = "th-TH-Standard-A",
    speaking_rate: float = 1.0,
    pitch: float = 0.0
) -> str:
    """
    Generate audio using Google Cloud Text-to-Speech API (premium option)

    This requires google-cloud-texttospeech package and proper GCP setup.
    Uncomment the implementation below if you want to use this.

    Args:
        text: Text to convert to speech
        output_path: Path where audio file will be saved
        api_key: Google Cloud API key (or use service account)
        language_code: Language code (e.g., "th-TH")
        voice_name: Voice name (e.g., "th-TH-Standard-A")
        speaking_rate: Speaking rate (0.25 to 4.0)
        pitch: Pitch adjustment (-20.0 to 20.0)

    Returns:
        Path to the generated audio file
    """
    raise NotImplementedError(
        "Google Cloud TTS is not implemented yet. "
        "To use it, install: pip install google-cloud-texttospeech "
        "and uncomment the implementation in this function."
    )

    # Uncomment below to use Cloud TTS:
    # from google.cloud import texttospeech
    # import os
    #
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_key
    #
    # client = texttospeech.TextToSpeechClient()
    #
    # synthesis_input = texttospeech.SynthesisInput(text=text)
    #
    # voice = texttospeech.VoiceSelectionParams(
    #     language_code=language_code,
    #     name=voice_name
    # )
    #
    # audio_config = texttospeech.AudioConfig(
    #     audio_encoding=texttospeech.AudioEncoding.MP3,
    #     speaking_rate=speaking_rate,
    #     pitch=pitch
    # )
    #
    # response = client.synthesize_speech(
    #     input=synthesis_input,
    #     voice=voice,
    #     audio_config=audio_config
    # )
    #
    # with open(output_path, "wb") as out:
    #     out.write(response.audio_content)
    #
    # return output_path


if __name__ == "__main__":
    # Test the module
    test_text = "สวัสดีครับ นี่คือการทดสอบระบบแปลงข้อความเป็นเสียง"
    output_file = "test_audio.mp3"

    print(f"Generating audio: {test_text}")
    result = generate_audio(test_text, output_file, language="th")
    print(f"Audio saved to: {result}")

    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)
        print("Test file cleaned up")
