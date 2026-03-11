import streamlit as st
import pandas as pd
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import get_user_history, get_analysis_by_id, delete_analysis
import plotly.express as px
from datetime import datetime

def show():
    """Display history page"""
    st.markdown("<h1 style='text-align: center;'>📜 Analysis History</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Get user history
    history = get_user_history(st.session_state.user_id)

    if not history:
        st.info("No CV analyses found. Upload a CV in the Dashboard to get started!")
        return

    # Create tabs for different views
    tab1, tab2 = st.tabs(["📋 List View", "📊 Analytics View"])

    with tab1:
        # Display history in a table
        for analysis in history:
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 2, 3, 1])

                with col1:
                    st.markdown(f"**📄 {analysis['filename']}**")

                with col2:
                    try:
                        date = datetime.strptime(analysis['date'], '%Y-%m-%d %H:%M:%S')
                        st.markdown(f"📅 {date.strftime('%B %d, %Y')}")
                    except Exception:
                        st.markdown(f"📅 {analysis['date']}")

                with col3:
                    # Show mini trait bars
                    traits_html = ""
                    for trait, score in analysis['traits'].items():
                        score = score if score is not None else 0
                        color = "#4CAF50" if score > 0.7 else "#FFC107" if score > 0.4 else "#F44336"
                        trait_name = trait.replace('_', ' ').title()
                        traits_html += f"""
                        <div style="margin: 2px 0;">
                            <span style="display: inline-block; width: 130px; font-size: 0.85em;">{trait_name}:</span>
                            <div style="display: inline-block; width: 90px; height: 10px; background-color: #e0e0e0; border-radius: 5px; vertical-align: middle;">
                                <div style="width: {score*100:.0f}%; height: 100%; background-color: {color}; border-radius: 5px;"></div>
                            </div>
                            <span style="margin-left: 6px; font-size: 0.85em;">{score:.2f}</span>
                        </div>
                        """
                    st.markdown(traits_html, unsafe_allow_html=True)

                with col4:
                    # Create download data
                    df_data = {
                        'Filename': [analysis['filename']],
                        'Date': [analysis['date']],
                        **{k: [v] for k, v in analysis['traits'].items()}
                    }
                    df = pd.DataFrame(df_data)
                    csv = df.to_csv(index=False)

                    st.download_button(
                        label="📥 CSV",
                        data=csv,
                        file_name=f"{analysis['filename']}_analysis.csv",
                        mime="text/csv",
                        key=f"download_btn_{analysis['id']}"
                    )

                    if st.button("🗑️ Delete", key=f"delete_{analysis['id']}"):
                        delete_analysis(analysis['id'], st.session_state.user_id)
                        st.success("Analysis deleted.")
                        st.rerun()

                st.markdown("---")

    with tab2:
        # Create analytics visualizations
        st.markdown("### 📈 Trait Evolution Over Time")

        # Prepare data for plotting
        df_data = []
        for analysis in history:
            for trait, score in analysis['traits'].items():
                df_data.append({
                    'Date': analysis['date'],
                    'Trait': trait.replace('_', ' ').title(),
                    'Score': score if score is not None else 0
                })

        if df_data:
            df = pd.DataFrame(df_data)

            # Line chart
            fig = px.line(df, x='Date', y='Score', color='Trait',
                         title='Personality Traits Over Time',
                         markers=True)
            st.plotly_chart(fig, use_container_width=True)

            # Average traits
            st.markdown("### 📊 Average Trait Scores")
            avg_scores = df.groupby('Trait')['Score'].mean().reset_index()

            fig2 = px.bar(avg_scores, x='Trait', y='Score',
                         title='Average Personality Traits',
                         color='Score',
                         color_continuous_scale='viridis')
            st.plotly_chart(fig2, use_container_width=True)

            # Summary stats
            st.markdown("### 📋 Summary Statistics")
            summary_df = df.groupby('Trait')['Score'].agg(['mean', 'min', 'max', 'std']).round(3)
            summary_df.columns = ['Mean', 'Min', 'Max', 'Std Dev']
            st.dataframe(summary_df, use_container_width=True)
