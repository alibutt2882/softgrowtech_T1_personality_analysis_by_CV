import streamlit as st

def show():
    """Display about page"""
    st.markdown("<h1 style='text-align: center;'>ℹ️ About CV Personality Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Hero section
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
         border-radius: 15px; color: white; margin-bottom: 30px;'>
        <h2 style='color: white;'>🧠 Revolutionizing CV Analysis with AI</h2>
        <p style='font-size: 18px;'>Using advanced machine learning algorithms to predict personality traits from CVs</p>
    </div>
    """, unsafe_allow_html=True)

    # Features section
    st.markdown("## 🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🧠 AI-Powered Analysis
        - Deep learning models trained on thousands of CVs
        - Natural Language Processing for text analysis
        - Pattern recognition for personality indicators
        - Real-time processing and results

        ### 📊 Comprehensive Trait Analysis
        - **Openness**: Creativity, curiosity, open-mindedness
        - **Conscientiousness**: Organization, responsibility, reliability
        - **Extraversion**: Sociability, energy, assertiveness
        - **Agreeableness**: Cooperation, empathy, trust
        - **Emotional Stability**: Resilience, stress management
        """)

    with col2:
        st.markdown("""
        ### ⚡ Quick & Efficient
        - Process CVs in under 2 minutes
        - Support for PDF, DOCX, and TXT formats
        - Batch processing capability
        - Instant results visualization

        ### 🔒 Secure & Private
        - End-to-end encryption
        - GDPR compliant
        - Data anonymization
        - Secure local database storage
        """)

    st.markdown("---")

    # How it works
    st.markdown("## 🔧 How It Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style='text-align:center; padding:20px; background:#f0f2f6; border-radius:10px;'>
            <h2>1️⃣</h2>
            <h4>Upload</h4>
            <p>Upload your CV in PDF, DOCX, or TXT format</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align:center; padding:20px; background:#f0f2f6; border-radius:10px;'>
            <h2>2️⃣</h2>
            <h4>Analyze</h4>
            <p>Our AI analyzes word choices, experiences, and accomplishments</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='text-align:center; padding:20px; background:#f0f2f6; border-radius:10px;'>
            <h2>3️⃣</h2>
            <h4>Map</h4>
            <p>Maps extracted features to OCEAN personality traits</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style='text-align:center; padding:20px; background:#f0f2f6; border-radius:10px;'>
            <h2>4️⃣</h2>
            <h4>Results</h4>
            <p>Get detailed personality analysis and recommendations</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Benefits
    st.markdown("## 💡 Benefits")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        ✅ **Reduce Bias** — Eliminate unconscious bias in hiring
        ✅ **Save Time** — Automated analysis vs manual evaluation
        ✅ **Improve Accuracy** — Data-driven personality assessment
        """)

    with col2:
        st.info("""
        ✅ **Better Matches** — Find candidates that fit company culture
        ✅ **Cost Effective** — Reduce recruitment costs
        ✅ **Scalable** — Analyze hundreds of CVs simultaneously
        """)

    st.markdown("---")

    # OCEAN Model explanation
    st.markdown("## 🔬 The OCEAN Model")
    st.markdown("""
    The **OCEAN Model** (also known as the Big Five) is one of the most scientifically validated
    frameworks for understanding human personality. It measures five key dimensions:
    """)

    traits = [
        ("🌟 Openness", "#667eea", "Reflects imagination, creativity, and willingness to try new things. High scorers tend to be curious, inventive, and open to diverse experiences."),
        ("📋 Conscientiousness", "#4CAF50", "Reflects organization, dependability, and self-discipline. High scorers tend to be goal-oriented, reliable, and detail-focused."),
        ("🗣️ Extraversion", "#FF9800", "Reflects sociability, assertiveness, and positive emotionality. High scorers thrive in social settings and enjoy being around others."),
        ("🤝 Agreeableness", "#00BCD4", "Reflects cooperation, empathy, and trust. High scorers are kind, sympathetic, and enjoy helping others."),
        ("🧘 Emotional Stability", "#9C27B0", "Reflects resilience and emotional balance. High scorers remain calm under pressure and manage stress effectively."),
    ]

    for trait_name, color, desc in traits:
        st.markdown(f"""
        <div style="border-left: 4px solid {color}; padding: 10px 20px; margin-bottom: 10px; background: #f9f9f9; border-radius: 0 8px 8px 0;">
            <strong>{trait_name}</strong><br/>
            <span style="color: #555;">{desc}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Technology stack
    st.markdown("## 🛠️ Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        **Frontend**
        - Streamlit
        - HTML/CSS
        - Plotly
        """)
    with col2:
        st.markdown("""
        **Backend**
        - Python
        - SQLite
        - bcrypt
        """)
    with col3:
        st.markdown("""
        **ML/AI**
        - Scikit-learn
        - NLTK
        - TF-IDF
        - RandomForest
        """)
    with col4:
        st.markdown("""
        **Deployment**
        - Docker
        - AWS/GCP
        - CI/CD
        """)

    st.markdown("---")

    # Footer with developer info
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;'>
        <h2 style='color: white;'>👨‍💻 Developed by Ali Haider Butt</h2>
        <p style='font-size: 18px;'>Senior ML/AI Developer with 20+ years of experience</p>
        <p>📧 alihaider.butt@example.com &nbsp;|&nbsp; 🔗 linkedin.com/in/alihaiderbutt &nbsp;|&nbsp; 🐦 @alihaiderbutt</p>
        <p style='margin-top: 20px; opacity: 0.8;'>© 2024 CV Personality Analyzer. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)
