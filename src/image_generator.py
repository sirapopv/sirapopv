"""
Image Generation Module
Step 6: Generate image/thumbnail from video title

Currently uses PIL to create simple thumbnails.
For AI-generated images, you can integrate with:
- Google Imagen API
- OpenAI DALL-E
- Stable Diffusion
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from typing import Tuple
import random


def create_gradient_background(width: int, height: int, color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> Image.Image:
    """Create a gradient background image"""
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


def generate_thumbnail(
    title: str,
    output_path: str,
    width: int = 1280,
    height: int = 720,
    style: str = "modern"
) -> str:
    """
    Generate a simple thumbnail image with title text

    Args:
        title: Video title to display
        output_path: Path where image will be saved
        width: Image width (default: 1280)
        height: Image height (default: 720)
        style: Style preset (modern, minimal, vibrant)

    Returns:
        Path to the generated image
    """
    # Style presets
    styles = {
        "modern": {
            "bg_color1": (20, 30, 48),
            "bg_color2": (36, 59, 85),
            "text_color": (255, 255, 255),
            "accent_color": (100, 210, 255)
        },
        "minimal": {
            "bg_color1": (240, 240, 245),
            "bg_color2": (255, 255, 255),
            "text_color": (30, 30, 30),
            "accent_color": (200, 0, 100)
        },
        "vibrant": {
            "bg_color1": (138, 43, 226),
            "bg_color2": (255, 105, 180),
            "text_color": (255, 255, 255),
            "accent_color": (255, 215, 0)
        }
    }

    # Get style or use default
    style_config = styles.get(style, styles["modern"])

    # Create gradient background
    img = create_gradient_background(
        width, height,
        style_config["bg_color1"],
        style_config["bg_color2"]
    )

    draw = ImageDraw.Draw(img)

    # Try to load a nice font, fall back to default if not available
    try:
        # Try different font paths for different systems
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf"
        ]

        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, 72)
                break

        if font is None:
            font = ImageFont.load_default()

    except Exception:
        font = ImageFont.load_default()

    # Wrap text to fit image
    margin = 100
    max_width = width - (2 * margin)

    # Simple word wrap
    wrapped_lines = []
    words = title.split()
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                wrapped_lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        wrapped_lines.append(' '.join(current_line))

    # Calculate total text height
    line_height = 80
    total_text_height = len(wrapped_lines) * line_height

    # Draw text centered
    y = (height - total_text_height) // 2

    for line in wrapped_lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2

        # Draw shadow
        draw.text((x + 3, y + 3), line, font=font, fill=(0, 0, 0, 128))
        # Draw main text
        draw.text((x, y), line, font=font, fill=style_config["text_color"])

        y += line_height

    # Add decorative elements
    # Top accent line
    draw.rectangle(
        [(margin, margin), (width - margin, margin + 8)],
        fill=style_config["accent_color"]
    )

    # Bottom accent line
    draw.rectangle(
        [(margin, height - margin - 8), (width - margin, height - margin)],
        fill=style_config["accent_color"]
    )

    # Save image
    img.save(output_path, quality=95)

    if not os.path.exists(output_path):
        raise Exception(f"Image was not created at {output_path}")

    return output_path


def generate_image_with_ai(
    prompt: str,
    output_path: str,
    api_key: str,
    width: int = 1280,
    height: int = 720
) -> str:
    """
    Generate image using AI (Placeholder for future implementation)

    To implement this, you can use:
    - Google Imagen API (via Vertex AI)
    - OpenAI DALL-E API
    - Stable Diffusion

    Args:
        prompt: Image generation prompt
        output_path: Path where image will be saved
        api_key: API key for image generation service
        width: Image width
        height: Image height

    Returns:
        Path to the generated image
    """
    raise NotImplementedError(
        "AI image generation is not implemented yet. "
        "Using generate_thumbnail() for now. "
        "To add AI generation, implement this function with your preferred API."
    )


if __name__ == "__main__":
    # Test the module
    test_title = "การเรียนรู้ AI และอนาคตของเทคโนโลยี"
    output_file = "test_thumbnail.jpg"

    print(f"Generating thumbnail for: {test_title}")

    # Test different styles
    for style in ["modern", "minimal", "vibrant"]:
        test_output = f"test_{style}.jpg"
        result = generate_thumbnail(test_title, test_output, style=style)
        print(f"Thumbnail ({style}) saved to: {result}")

        # Clean up
        if os.path.exists(test_output):
            os.remove(test_output)

    print("Test completed and cleaned up")
