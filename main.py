#!/usr/bin/env python3
"""
YouTube Video Converter - Main Script
Converts YouTube videos into podcasts automatically

Steps:
1. Extract transcript from YouTube video
2. Translate transcript to target language
3. Generate title and description
4. Generate audio from translated text
5. Generate thumbnail image
6. Create video (audio + image)
7. Save output

Usage:
    python main.py <youtube_url>
    python main.py <youtube_url> --language Thai --output-dir output
"""

import os
import sys
import yaml
import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.table import Table
from dotenv import load_dotenv
from datetime import datetime

# Import our modules
from src.transcript import get_transcript
from src.translator import translate_transcript
from src.content_writer import generate_title_and_description
from src.audio_generator import generate_audio
from src.image_generator import generate_thumbnail
from src.video_creator import create_video, check_ffmpeg, get_video_duration

# Initialize Rich console for pretty output
console = Console()


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML file"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        console.print(f"[yellow]Warning: {config_path} not found, using defaults[/yellow]")
        return {}


def ensure_output_directory(output_dir: str) -> str:
    """Create output directory if it doesn't exist"""
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


@click.command()
@click.argument('youtube_url')
@click.option('--language', '-l', default=None, help='Target language (default: from config)')
@click.option('--output-dir', '-o', default=None, help='Output directory (default: from config)')
@click.option('--style', '-s', default='modern', help='Thumbnail style: modern, minimal, vibrant')
@click.option('--config', '-c', default='config.yaml', help='Config file path')
def main(youtube_url: str, language: str, output_dir: str, style: str, config: str):
    """
    Convert YouTube video to podcast

    YOUTUBE_URL: The YouTube video URL to convert
    """
    # Load environment variables
    load_dotenv()

    # Load configuration
    config_data = load_config(config)

    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        console.print("[red]Error: GEMINI_API_KEY not found in environment variables[/red]")
        console.print("Please create a .env file with your API key:")
        console.print("  GEMINI_API_KEY=your_api_key_here")
        sys.exit(1)

    # Set defaults from config
    language = language or config_data.get('default_language', 'Thai')
    output_dir = output_dir or config_data.get('output_directory', 'output')

    # Ensure output directory exists
    ensure_output_directory(output_dir)

    # Display header
    console.print(Panel.fit(
        "[bold cyan]YouTube Video to Podcast Converter[/bold cyan]\n"
        f"Language: {language} | Style: {style}",
        border_style="cyan"
    ))

    # Check ffmpeg
    if not check_ffmpeg():
        console.print("[red]Error: ffmpeg is not installed[/red]")
        console.print("Please install ffmpeg:")
        console.print("  Ubuntu/Debian: sudo apt-get install ffmpeg")
        console.print("  MacOS: brew install ffmpeg")
        sys.exit(1)

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:

            # Step 1: Extract video ID and transcript
            task1 = progress.add_task("[cyan]Step 1/6: Extracting transcript...", total=None)
            transcript_data = get_transcript(youtube_url)
            video_id = transcript_data['video_id']
            transcript = transcript_data['transcript']
            progress.update(task1, completed=True)
            console.print(f"[green]✓[/green] Transcript extracted ({len(transcript)} characters)")

            # Step 2: Translate transcript
            task2 = progress.add_task("[cyan]Step 2/6: Translating to " + language + "...", total=None)
            translation_config = config_data.get('translation', {})
            translated_text = translate_transcript(
                transcript=transcript,
                api_key=api_key,
                target_language=language,
                style_instructions=translation_config.get('style_instructions', ''),
                script_example=translation_config.get('script_example', ''),
                model=config_data.get('gemini', {}).get('model', 'gemini-2.0-flash-exp')
            )
            progress.update(task2, completed=True)
            console.print(f"[green]✓[/green] Translation completed ({len(translated_text)} characters)")

            # Step 3: Generate title and description
            task3 = progress.add_task("[cyan]Step 3/6: Generating title & description...", total=None)
            content_config = config_data.get('content_generation', {})
            title, description = generate_title_and_description(
                translated_text=translated_text,
                api_key=api_key,
                language=language,
                title_prompt=content_config.get('title_prompt', ''),
                description_prompt=content_config.get('description_prompt', ''),
                model=config_data.get('gemini', {}).get('model', 'gemini-2.0-flash-exp')
            )
            progress.update(task3, completed=True)
            console.print(f"[green]✓[/green] Title: {title[:50]}...")

            # Create timestamp-based filenames
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_filename = f"{video_id}_{timestamp}"

            # Step 4: Generate audio
            task4 = progress.add_task("[cyan]Step 4/6: Generating audio...", total=None)
            audio_path = os.path.join(output_dir, f"{base_filename}.mp3")
            # Detect language code for TTS
            lang_code = "th" if language.lower() in ["thai", "ไทย"] else "en"
            generate_audio(
                text=translated_text,
                output_path=audio_path,
                language=lang_code
            )
            progress.update(task4, completed=True)
            console.print(f"[green]✓[/green] Audio generated: {audio_path}")

            # Step 5: Generate thumbnail
            task5 = progress.add_task("[cyan]Step 5/6: Generating thumbnail...", total=None)
            image_path = os.path.join(output_dir, f"{base_filename}.jpg")
            generate_thumbnail(
                title=title,
                output_path=image_path,
                width=1280,
                height=720,
                style=style
            )
            progress.update(task5, completed=True)
            console.print(f"[green]✓[/green] Thumbnail generated: {image_path}")

            # Step 6: Create video
            task6 = progress.add_task("[cyan]Step 6/6: Creating video...", total=None)
            video_path = os.path.join(output_dir, f"{base_filename}.mp4")
            create_video(
                audio_path=audio_path,
                image_path=image_path,
                output_path=video_path,
                fps=1
            )
            progress.update(task6, completed=True)

            # Get video duration
            duration = get_video_duration(video_path)
            duration_str = f"{int(duration)}s" if duration else "unknown"

            console.print(f"[green]✓[/green] Video created: {video_path}")

        # Display success summary
        console.print("\n")
        summary = Table(title="[bold green]Conversion Complete![/bold green]", show_header=False)
        summary.add_column("Property", style="cyan")
        summary.add_column("Value", style="white")

        summary.add_row("Video ID", video_id)
        summary.add_row("Title", title)
        summary.add_row("Language", language)
        summary.add_row("Duration", duration_str)
        summary.add_row("Video File", video_path)
        summary.add_row("Audio File", audio_path)
        summary.add_row("Image File", image_path)

        console.print(summary)

        # Save metadata
        metadata_path = os.path.join(output_dir, f"{base_filename}_metadata.txt")
        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write(f"Video ID: {video_id}\n")
            f.write(f"Original URL: {youtube_url}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Description:\n{description}\n")
            f.write(f"\n--- Translated Script ---\n{translated_text}\n")

        console.print(f"\n[dim]Metadata saved to: {metadata_path}[/dim]")

        console.print("\n[bold green]Ready for upload to YouTube![/bold green]")
        console.print("Next step: Implement YouTube upload (Step 8) or upload manually")

    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        sys.exit(1)


if __name__ == "__main__":
    main()
