import streamlit as st
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import get_user_settings, update_user_settings, update_user_profile
from PIL import Image
import io

def show():
    """Display settings page"""
    st.markdown("<h1 style='text-align: center;'>⚙️ Settings</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Create tabs for different settings
    tab1, tab2, tab3 = st.tabs(["👤 Profile", "🎨 Theme", "🔔 Notifications"])

    with tab1:
        st.markdown("### Profile Settings")

        col1, col2 = st.columns([1, 2])

        with col1:
            # Profile picture
            if 'profile_pic' not in st.session_state:
                st.session_state.profile_pic = None

            uploaded_pic = st.file_uploader("Upload Profile Picture", type=['png', 'jpg', 'jpeg'])
            if uploaded_pic:
                st.session_state.profile_pic = uploaded_pic
                image = Image.open(uploaded_pic)
                st.image(image, caption='Profile Picture', use_container_width=True)
            else:
                # Show placeholder avatar
                st.markdown("""
                <div style="width:120px; height:120px; background: linear-gradient(135deg, #667eea, #764ba2);
                     border-radius: 50%; display:flex; align-items:center; justify-content:center;
                     font-size: 48px; color: white; margin: auto;">
                     👤
                </div>
                """, unsafe_allow_html=True)

        with col2:
            with st.form("profile_form"):
                full_name = st.text_input("Full Name", value=st.session_state.get('full_name', ''))
                email = st.text_input("Email", value=st.session_state.get('user_email', ''))
                username = st.text_input("Username", value=st.session_state.get('username', ''), disabled=True)

                col_a, col_b = st.columns(2)
                with col_a:
                    if st.form_submit_button("Save Changes", use_container_width=True):
                        update_user_profile(st.session_state.user_id, full_name, email)
                        st.session_state.full_name = full_name
                        st.session_state.user_email = email
                        st.success("Profile updated successfully!")

                with col_b:
                    if st.form_submit_button("Change Password", use_container_width=True):
                        st.info("Password change feature coming soon!")

        # Account info card
        st.markdown("---")
        st.markdown("### 📋 Account Information")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Username", st.session_state.get('username', 'N/A'))
        with col_b:
            st.metric("Email", st.session_state.get('user_email', 'N/A'))
        with col_c:
            st.metric("Full Name", st.session_state.get('full_name', 'Not set') or 'Not set')

    with tab2:
        st.markdown("### Theme Settings")

        # Get current theme
        settings = get_user_settings(st.session_state.user_id)
        current_theme = settings['theme'] if settings else 'light'

        # Theme selection
        theme = st.radio(
            "Select Theme",
            options=['Light', 'Dark'],
            index=0 if current_theme == 'light' else 1,
            horizontal=True
        )

        if st.button("Apply Theme", type="primary"):
            st.session_state.theme = theme.lower()
            update_user_settings(
                st.session_state.user_id,
                theme.lower(),
                settings.get('email_notifications', True) if settings else True
            )
            st.success(f"Theme changed to {theme} mode!")
            st.rerun()

        # Theme preview
        st.markdown("### Preview")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div style="background-color: #ffffff; color: #000000; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
                <h4>☀️ Light Mode Preview</h4>
                <p>This is how text looks in light mode.</p>
                <button style="background-color: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 5px; cursor: pointer;">Button</button>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: #1a1a1a; color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #444;">
                <h4>🌙 Dark Mode Preview</h4>
                <p>This is how text looks in dark mode.</p>
                <button style="background-color: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 5px; cursor: pointer;">Button</button>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("### Notification Settings")

        settings = get_user_settings(st.session_state.user_id)
        email_notifications = settings['email_notifications'] if settings else True

        with st.form("notification_form"):
            notify_email = st.checkbox("Email Notifications", value=bool(email_notifications))
            notify_analysis = st.checkbox("Notify when analysis complete", value=True)
            notify_newsletter = st.checkbox("Receive newsletter", value=False)

            if st.form_submit_button("Save Notification Settings", use_container_width=True):
                update_user_settings(st.session_state.user_id, st.session_state.theme, notify_email)
                st.success("Notification settings updated!")
