"""
Content Writer Module using Google Gemini
Step 4: Generate engaging video title and description
"""

import google.generativeai as genai
from typing import Tuple


def generate_title_and_description(
    translated_text: str,
    api_key: str,
    language: str = "Thai",
    title_prompt: str = "",
    description_prompt: str = "",
    model: str = "gemini-2.0-flash-exp"
) -> Tuple[str, str]:
    """
    Generate engaging title and description using Google Gemini

    Args:
        translated_text: Translated transcript
        api_key: Google Gemini API key
        language: Content language
        title_prompt: Custom prompt for title generation
        description_prompt: Custom prompt for description generation
        model: Gemini model to use

    Returns:
        Tuple of (title, description)
    """
    # Configure Gemini API
    genai.configure(api_key=api_key)
    model_obj = genai.GenerativeModel(model)

    # Default prompts if not provided
    if not title_prompt:
        title_prompt = f"Create an engaging {language} YouTube title (60 characters max) for a podcast based on this content. Make it catchy and clickable."

    if not description_prompt:
        description_prompt = f"Write a compelling {language} YouTube description for this podcast. Include a brief overview and key topics."

    # Generate title
    title_full_prompt = f"{title_prompt}\n\nContent:\n{translated_text[:1000]}\n\nProvide ONLY the title, nothing else."
    title_response = model_obj.generate_content(title_full_prompt)

    if not title_response or not title_response.text:
        raise Exception("Failed to generate title from Gemini API")

    title = title_response.text.strip()

    # Generate description
    desc_full_prompt = f"{description_prompt}\n\nContent:\n{translated_text[:2000]}\n\nProvide ONLY the description, nothing else."
    desc_response = model_obj.generate_content(desc_full_prompt)

    if not desc_response or not desc_response.text:
        raise Exception("Failed to generate description from Gemini API")

    description = desc_response.text.strip()

    return title, description


if __name__ == "__main__":
    # Test the module
    import os
    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Please set GEMINI_API_KEY in .env file")
        exit(1)

    test_content = """
    สวัสดีครับ วันนี้เราจะมาพูดถึงเรื่องปัญญาประดิษฐ์และผลกระทบต่อสังคม
    AI กำลังเปลี่ยนแปลงวิธีที่เราทำงาน เรียนรู้ และใช้ชีวิตประจำวัน
    เรามาดูกันว่ามีอะไรน่าสนใจบ้าง
    """

    title, description = generate_title_and_description(
        translated_text=test_content,
        api_key=api_key,
        language="Thai"
    )

    print("Generated Title:")
    print(title)
    print("\nGenerated Description:")
    print(description)
