import streamlit as st
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_database
from auth import login, signup
from pages import dashboard, history, settings, about

# Page configuration
st.set_page_config(
    page_title="CV Personality Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    css_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'style.css')
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize database
init_database()

# Session state initialization
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'
if 'page' not in st.session_state:
    st.session_state.page = 'Dashboard'

# Main app logic
def main():
    # Load CSS
    load_css()

    # Apply theme
    if st.session_state.theme == 'dark':
        st.markdown("""
        <style>
        .stApp {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stMarkdown {
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)

    # Check if user is authenticated
    if not st.session_state.authenticated:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<h1 style='text-align: center;'>🧠 CV Personality Analyzer</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Welcome! Please login or signup to continue</p>", unsafe_allow_html=True)

            tab1, tab2 = st.tabs(["Login", "Sign Up"])

            with tab1:
                login()

            with tab2:
                signup()
    else:
        # Navigation sidebar
        with st.sidebar:
            st.markdown(f"### Welcome, {st.session_state.username}! 👋")
            st.markdown("---")

            # Navigation buttons
            if st.button("📊 Dashboard", use_container_width=True):
                st.session_state.page = 'Dashboard'
                st.rerun()

            if st.button("📜 History", use_container_width=True):
                st.session_state.page = 'History'
                st.rerun()

            if st.button("⚙️ Settings", use_container_width=True):
                st.session_state.page = 'Settings'
                st.rerun()

            if st.button("ℹ️ About Project", use_container_width=True):
                st.session_state.page = 'About'
                st.rerun()

            st.markdown("---")
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.username = None
                st.session_state.user_id = None
                st.session_state.page = 'Dashboard'
                st.rerun()

        # Main content area
        if st.session_state.page == 'Dashboard':
            dashboard.show()
        elif st.session_state.page == 'History':
            history.show()
        elif st.session_state.page == 'Settings':
            settings.show()
        elif st.session_state.page == 'About':
            about.show()

if __name__ == "__main__":
    main()
