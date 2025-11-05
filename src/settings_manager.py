"""
Settings Manager Module
Handles persistent storage of user settings, API keys, and sample scripts
"""

import json
import os
from typing import Optional, Dict, Any
from pathlib import Path


class SettingsManager:
    """Manage application settings with persistent storage"""

    def __init__(self, settings_dir: str = "settings"):
        """
        Initialize settings manager

        Args:
            settings_dir: Directory to store settings files
        """
        self.settings_dir = Path(settings_dir)
        self.settings_dir.mkdir(exist_ok=True)

        self.settings_file = self.settings_dir / "app_settings.json"
        self.sample_script_file = self.settings_dir / "sample_script.txt"

        # Load or create default settings
        self.settings = self._load_settings()

    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from file or create default"""
        if self.settings_file.exists():
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass

        # Default settings
        return {
            'api_key': '',
            'style_instructions': '',
            'language': 'Thai',
            'thumbnail_style': 'modern',
            'output_directory': 'output'
        }

    def _save_settings(self):
        """Save settings to file"""
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value"""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any):
        """Set a setting value and save"""
        self.settings[key] = value
        self._save_settings()

    def get_api_key(self) -> str:
        """Get the API key"""
        return self.settings.get('api_key', '')

    def set_api_key(self, api_key: str):
        """Set the API key"""
        self.set('api_key', api_key)

    def get_style_instructions(self) -> str:
        """Get style instructions"""
        return self.settings.get('style_instructions', '')

    def set_style_instructions(self, instructions: str):
        """Set style instructions"""
        self.set('style_instructions', instructions)

    def get_sample_script(self) -> str:
        """Get sample script content"""
        if self.sample_script_file.exists():
            try:
                with open(self.sample_script_file, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception:
                pass
        return ''

    def set_sample_script(self, content: str):
        """Set sample script content"""
        try:
            with open(self.sample_script_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error saving sample script: {e}")

    def has_sample_script(self) -> bool:
        """Check if sample script exists"""
        return self.sample_script_file.exists() and len(self.get_sample_script()) > 0

    def delete_sample_script(self):
        """Delete the sample script file"""
        if self.sample_script_file.exists():
            self.sample_script_file.unlink()

    def get_all_settings(self) -> Dict[str, Any]:
        """Get all settings"""
        settings_copy = self.settings.copy()
        settings_copy['sample_script'] = self.get_sample_script()
        settings_copy['has_sample_script'] = self.has_sample_script()
        return settings_copy

    def clear_api_key(self):
        """Clear the stored API key"""
        self.set('api_key', '')


if __name__ == "__main__":
    # Test the settings manager
    manager = SettingsManager()

    # Test API key
    manager.set_api_key("test_key_123")
    print(f"API Key: {manager.get_api_key()}")

    # Test style instructions
    manager.set_style_instructions("Make it conversational and fun!")
    print(f"Style: {manager.get_style_instructions()}")

    # Test sample script
    manager.set_sample_script("สวัสดีครับ นี่คือตัวอย่างสคริปต์")
    print(f"Sample Script: {manager.get_sample_script()}")
    print(f"Has Sample Script: {manager.has_sample_script()}")

    # Test all settings
    print("\nAll Settings:")
    print(json.dumps(manager.get_all_settings(), indent=2, ensure_ascii=False))
