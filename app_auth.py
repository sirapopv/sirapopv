#!/usr/bin/env python3
"""
YouTube Video to Podcast Converter - Web Interface with Authentication
Version with optional password protection for public deployment
"""

import streamlit as st
import os
import hashlib

# Authentication configuration
# Set these environment variables for password protection
AUTH_USERNAME = os.getenv("AUTH_USERNAME", "")  # Leave empty to disable auth
AUTH_PASSWORD_HASH = os.getenv("AUTH_PASSWORD_HASH", "")  # SHA256 hash of password


def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def check_authentication():
    """Check if authentication is required and validate credentials"""

    # If no username is set, authentication is disabled
    if not AUTH_USERNAME:
        return True

    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    # If already authenticated, return True
    if st.session_state.authenticated:
        return True

    # Show login form
    st.markdown("# 🔒 Authentication Required")
    st.markdown("Please log in to access the YouTube to Podcast Converter")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            password_hash = hash_password(password)
            if username == AUTH_USERNAME and password_hash == AUTH_PASSWORD_HASH:
                st.session_state.authenticated = True
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    st.markdown("---")
    st.info("""
    **For administrators:**

    To set up authentication, set these environment variables:
    - `AUTH_USERNAME`: Your desired username
    - `AUTH_PASSWORD_HASH`: SHA256 hash of your password

    Generate password hash:
    ```python
    import hashlib
    print(hashlib.sha256("your_password".hexdigest())
    ```
    """)

    return False


def show_logout_button():
    """Show logout button in sidebar if authenticated"""
    if AUTH_USERNAME and st.session_state.get('authenticated', False):
        st.sidebar.markdown("---")
        if st.sidebar.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.rerun()


# Check authentication before loading main app
if check_authentication():
    # Import and run the main app
    import sys

    # Load the original app module
    with open('app.py', 'r', encoding='utf-8') as f:
        app_code = f.read()

    # Remove the shebang and imports that are already imported
    app_code = app_code.replace('#!/usr/bin/env python3', '')

    # Execute the main app
    exec(app_code)

    # Add logout button
    show_logout_button()
