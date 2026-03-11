import streamlit as st
from database import create_user, verify_user

def login():
    """Handle user login"""
    with st.form("login_form"):
        username_email = st.text_input("Username or Email")
        password = st.text_input("Password", type="password")

        col1, col2 = st.columns([1, 1])
        with col1:
            submit = st.form_submit_button("Login", use_container_width=True)

        if submit:
            if username_email and password:
                success, user_data = verify_user(username_email, password)
                if success:
                    st.session_state.authenticated = True
                    st.session_state.username = user_data['username']
                    st.session_state.user_id = user_data['id']
                    st.session_state.user_email = user_data['email']
                    st.session_state.full_name = user_data.get('full_name', '')
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username/email or password")
            else:
                st.warning("Please fill in all fields")

def signup():
    """Handle user signup"""
    with st.form("signup_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        full_name = st.text_input("Full Name (Optional)")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        submit = st.form_submit_button("Sign Up", use_container_width=True)

        if submit:
            if not all([username, email, password, confirm_password]):
                st.warning("Please fill in all required fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long")
            else:
                success, message, user_id = create_user(username, email, password, full_name)
                if success:
                    st.success("Account created successfully! Please login.")
                else:
                    st.error(message)

def check_authentication():
    """Check if user is authenticated"""
    return st.session_state.get('authenticated', False)
