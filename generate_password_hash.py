#!/usr/bin/env python3
"""
Password Hash Generator for Authentication
Generate SHA256 hash for use with app_auth.py
"""

import hashlib
import getpass


def generate_hash(password: str) -> str:
    """Generate SHA256 hash of password"""
    return hashlib.sha256(password.encode()).hexdigest()


def main():
    print("=" * 60)
    print("YouTube to Podcast Converter - Password Hash Generator")
    print("=" * 60)
    print()

    # Get password securely (hidden input)
    password = getpass.getpass("Enter password: ")
    password_confirm = getpass.getpass("Confirm password: ")

    if password != password_confirm:
        print("\n❌ Passwords don't match! Please try again.")
        return

    if len(password) < 8:
        print("\n⚠️  Warning: Password is shorter than 8 characters.")
        print("Consider using a longer password for better security.")

    # Generate hash
    password_hash = generate_hash(password)

    print("\n✅ Password hash generated successfully!")
    print("\n" + "=" * 60)
    print("Configuration for Deployment:")
    print("=" * 60)
    print()
    print("Set these environment variables:")
    print()
    print(f"AUTH_USERNAME=admin")
    print(f"AUTH_PASSWORD_HASH={password_hash}")
    print()
    print("=" * 60)
    print()
    print("📝 Instructions:")
    print()
    print("1. For Docker Compose:")
    print("   Add to docker-compose.yml under 'environment:'")
    print()
    print("2. For Cloud Platforms (Railway, Render, etc.):")
    print("   Add as environment variables in dashboard")
    print()
    print("3. For VPS:")
    print("   Export variables before running:")
    print(f"   export AUTH_USERNAME=admin")
    print(f"   export AUTH_PASSWORD_HASH={password_hash}")
    print()
    print("4. Update Dockerfile to use app_auth.py:")
    print('   CMD ["streamlit", "run", "app_auth.py", ...]')
    print()
    print("=" * 60)
    print()
    print("🔒 Keep this hash secure and don't commit it to git!")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
