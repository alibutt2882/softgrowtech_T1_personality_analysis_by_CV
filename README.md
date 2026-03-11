# 🧠 CV Personality Analyzer

A Streamlit-based web application that analyzes CVs and predicts personality traits using the **OCEAN (Big Five) model** with NLP and machine learning.

---

## 📁 Project Structure

```
cv_personality_analyzer/
├── app.py                    # Main entry point
├── auth.py                   # Login & signup logic
├── database.py               # SQLite DB operations
├── requirements.txt          # Python dependencies
│
├── assets/
│   └── style.css             # Custom CSS styling
│
├── pages/
│   ├── __init__.py
│   ├── dashboard.py          # CV upload & analysis results
│   ├── history.py            # Past analysis records
│   ├── settings.py           # Profile, theme, notifications
│   └── about.py              # Project information
│
├── utils/
│   ├── __init__.py
│   ├── cv_analyzer.py        # Text extraction & trait scoring
│   └── personality_model.py  # Scikit-learn ML model wrapper
│
├── models/                   # Saved model files (auto-created)
└── cv_analyzer.db            # SQLite database (auto-created)
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Download NLTK data (first run only)

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## ✨ Features

- **User Authentication** — Secure signup and login with bcrypt password hashing
- **CV Upload** — Supports PDF, DOCX, and TXT formats
- **Personality Analysis** — OCEAN Big Five trait scoring via NLP keyword analysis
- **Radar Chart Visualization** — Interactive Plotly chart for trait visualization
- **Analysis History** — View, download (CSV), and delete past analyses
- **Analytics Dashboard** — Trait evolution charts and summary statistics
- **User Settings** — Profile management, light/dark theme, notification preferences
- **Persistent Storage** — SQLite database with full CRUD support

---

## 🔬 OCEAN Model (Big Five Personality Traits)

| Trait | Description |
|-------|-------------|
| **Openness** | Creativity, curiosity, adaptability |
| **Conscientiousness** | Organization, reliability, discipline |
| **Extraversion** | Sociability, assertiveness, energy |
| **Agreeableness** | Empathy, cooperation, trust |
| **Emotional Stability** | Resilience, calm, stress management |

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit, Plotly, HTML/CSS
- **Backend**: Python, SQLite
- **ML/AI**: scikit-learn, NLTK, TF-IDF, RandomForest
- **Security**: bcrypt password hashing

---

## 👨‍💻 Developer

**Ali Haider Butt** — Senior ML/AI Developer  
© 2024 CV Personality Analyzer. All rights reserved.
