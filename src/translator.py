"""
Translation Module using Google Gemini
Step 3: Translate transcript to desired language with custom style
"""

import google.generativeai as genai
from typing import Optional


def translate_transcript(
    transcript: str,
    api_key: str,
    target_language: str = "Thai",
    style_instructions: str = "",
    script_example: str = "",
    model: str = "gemini-2.0-flash-exp"
) -> str:
    """
    Translate transcript using Google Gemini API

    Args:
        transcript: Original transcript text
        api_key: Google Gemini API key
        target_language: Target language (default: "Thai")
        style_instructions: Custom style instructions for translation
        script_example: Example script for style reference
        model: Gemini model to use

    Returns:
        Translated text
    """
    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Build the prompt
    prompt_parts = [
        f"Translate the following transcript to {target_language}.",
        ""
    ]

    if style_instructions:
        prompt_parts.append("Style Instructions:")
        prompt_parts.append(style_instructions)
        prompt_parts.append("")

    if script_example:
        prompt_parts.append("Example of desired style:")
        prompt_parts.append(script_example)
        prompt_parts.append("")

    prompt_parts.append("Original Transcript:")
    prompt_parts.append(transcript)
    prompt_parts.append("")
    prompt_parts.append(f"Provide ONLY the translated {target_language} text, without any additional comments or explanations.")

    prompt = "\n".join(prompt_parts)

    # Generate translation
    model_obj = genai.GenerativeModel(model)
    response = model_obj.generate_content(prompt)

    if not response or not response.text:
        raise Exception("Failed to generate translation from Gemini API")

    return response.text.strip()


if __name__ == "__main__":
    # Test the module (requires API key in environment)
    import os
    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Please set GEMINI_API_KEY in .env file")
        exit(1)

    test_text = "Hello, this is a test transcript. Today we'll discuss artificial intelligence and its impact on society."

    translated = translate_transcript(
        transcript=test_text,
        api_key=api_key,
        target_language="Thai",
        style_instructions="Make it conversational and engaging for podcast listeners."
    )

    print("Original:")
    print(test_text)
    print("\nTranslated:")
    print(translated)
