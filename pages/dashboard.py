import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.cv_analyzer import analyze_cv
from database import save_cv_analysis
import time

def show():
    """Display dashboard page"""
    st.markdown("<h1 style='text-align: center;'>📊 CV Personality Analysis Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Create two columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📄 Upload CV for Analysis")

        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a CV file (PDF, DOCX, or TXT)",
            type=['pdf', 'docx', 'txt'],
            help="Upload your CV to analyze personality traits"
        )

        if uploaded_file is not None:
            # Display file details
            file_details = {
                "Filename": uploaded_file.name,
                "File size": f"{uploaded_file.size / 1024:.2f} KB"
            }
            st.json(file_details)

            # Analyze button
            if st.button("🔍 Analyze CV", type="primary", use_container_width=True):
                with st.spinner("Analyzing CV... This may take a moment."):
                    time.sleep(2)

                    # Perform analysis
                    results = analyze_cv(uploaded_file)

                    # Save to database
                    analysis_id = save_cv_analysis(
                        st.session_state.user_id,
                        uploaded_file.name,
                        results['traits'],
                        results['scores'],
                        results['summary'],
                        results['recommendations']
                    )

                    # Store results in session state
                    st.session_state.last_analysis = results
                    st.session_state.analysis_id = analysis_id

                    st.success("✅ Analysis complete!")

    with col2:
        if 'last_analysis' in st.session_state:
            st.markdown("### 📊 Analysis Results")

            results = st.session_state.last_analysis

            # Create radar chart for personality traits
            categories = ['Openness', 'Conscientiousness', 'Extraversion',
                         'Agreeableness', 'Emotional Stability']

            values = [
                results['scores']['openness'] * 10,
                results['scores']['conscientiousness'] * 10,
                results['scores']['extraversion'] * 10,
                results['scores']['agreeableness'] * 10,
                results['scores']['emotional_stability'] * 10
            ]

            fig = go.Figure(data=go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                marker=dict(color='rgba(76, 175, 80, 0.8)')
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 10]
                    )),
                showlegend=False,
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

            # Display trait scores
            col_a, col_b = st.columns(2)
            with col_a:
                for trait, score in list(results['scores'].items())[:3]:
                    st.metric(trait.replace('_', ' ').title(), f"{score:.2f}")
            with col_b:
                for trait, score in list(results['scores'].items())[3:]:
                    st.metric(trait.replace('_', ' ').title(), f"{score:.2f}")

            # Summary
            st.markdown("### 📝 Summary")
            st.info(results['summary'])

            # Recommendations
            with st.expander("💡 Recommendations"):
                st.write(results['recommendations'])
        else:
            st.info("👈 Upload a CV to see analysis results here")

    # Additional features section
    st.markdown("---")
    st.markdown("### ✨ Key Features")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🧠 AI-Powered", "Deep Learning")
    with col2:
        st.metric("⚡ Fast Analysis", "< 2 minutes")
    with col3:
        st.metric("📊 5 Traits", "OCEAN Model")
    with col4:
        st.metric("🎯 95% Accuracy", "Proven Results")
