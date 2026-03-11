<div align="center">

# 🧠 CV Personality Analyzer

### AI-powered personality trait prediction from CVs using the Big Five (OCEAN) Model

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> Upload a CV → Get instant personality insights powered by NLP & Machine Learning

<br/>


</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [OCEAN Model](#-the-ocean-big-five-model)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🔍 Overview

**CV Personality Analyzer** is a full-stack web application that uses **Natural Language Processing** and **Machine Learning** to analyze CVs and predict personality traits based on the scientifically validated **OCEAN (Big Five)** model.

Whether you're an HR professional streamlining recruitment or a developer building smart hiring tools, this app delivers data-driven personality insights directly from uploaded resumes — all within a clean, interactive Streamlit interface.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **User Authentication** | Secure signup & login with `bcrypt` password hashing |
| 📄 **Multi-format CV Upload** | Supports **PDF**, **DOCX**, and **TXT** files |
| 🤖 **AI Personality Analysis** | NLP keyword scoring mapped to OCEAN traits |
| 📊 **Radar Chart Visualization** | Interactive Plotly radar chart of trait scores |
| 📜 **Analysis History** | View, download (CSV), and delete past analyses |
| 📈 **Analytics Dashboard** | Trait evolution over time + average score charts |
| 🎨 **Light / Dark Theme** | User-selectable UI theme, persisted in database |
| ⚙️ **Profile Settings** | Edit name, email, and upload profile picture |
| 💾 **Persistent Storage** | Full SQLite CRUD — no cloud dependency needed |

---

## 🔬 The OCEAN (Big Five) Model

The **OCEAN model** is one of the most widely used and scientifically validated frameworks for measuring human personality. The app scores candidates across five dimensions:

```
O ── Openness          →  Creativity, curiosity, adaptability
C ── Conscientiousness →  Organization, discipline, reliability
E ── Extraversion      →  Sociability, assertiveness, energy
A ── Agreeableness     →  Empathy, cooperation, trust
N ── (Emotional) Stability → Resilience, calm, stress tolerance
```

Each trait is scored between **0.0 – 1.0** based on keyword frequency and semantic patterns extracted from the CV text.

---

## 🛠️ Tech Stack

**Frontend**
- [Streamlit](https://streamlit.io/) — UI framework
- [Plotly](https://plotly.com/) — Interactive charts
- HTML / CSS — Custom styling

**Backend**
- Python 3.8+
- SQLite — Local persistent database
- bcrypt — Password hashing

**Machine Learning / NLP**
- [scikit-learn](https://scikit-learn.org/) — TF-IDF vectorization, RandomForest regression
- [NLTK](https://www.nltk.org/) — Tokenization, stopword removal
- PyPDF2 — PDF text extraction
- python-docx — DOCX text extraction

---

## 📁 Project Structure

```
cv_personality_analyzer/
│
├── app.py                        # 🚀 Main entry point
├── auth.py                       # 🔐 Login & signup logic
├── database.py                   # 🗄️  SQLite DB operations (CRUD)
├── requirements.txt              # 📦 Python dependencies
├── README.md                     # 📖 This file
│
├── assets/
│   └── style.css                 # 🎨 Custom CSS styles
│
├── pages/
│   ├── __init__.py
│   ├── dashboard.py              # 📊 CV upload & analysis results
│   ├── history.py                # 📜 Past analysis records & analytics
│   ├── settings.py               # ⚙️  Profile, theme, notifications
│   └── about.py                  # ℹ️  Project info & OCEAN explanation
│
├── utils/
│   ├── __init__.py
│   ├── cv_analyzer.py            # 🤖 Text extraction & trait scoring engine
│   └── personality_model.py     # 🧬 Scikit-learn ML model wrapper
│
├── models/                       # 💾 Saved ML model files (auto-created)
└── cv_analyzer.db                # 🗃️  SQLite database (auto-created on first run)
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8 or higher**
- pip

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cv-personality-analyzer.git
cd cv-personality-analyzer
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK data

> This only needs to be done once. The app handles it automatically on first run, but you can also run it manually:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501` 🎉

---

## ⚙️ How It Works

```
┌─────────────┐     ┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  Upload CV  │────▶│  Extract Text    │────▶│  NLP Processing   │────▶│  OCEAN Scores    │
│ PDF/DOCX/TXT│     │ PyPDF2 / docx    │     │ Tokenize, Remove  │     │ 0.0 ──── 1.0     │
└─────────────┘     └──────────────────┘     │ Stopwords, Score  │     └──────────────────┘
                                             │ Keywords per Trait│              │
                                             └───────────────────┘              ▼
                                                                     ┌──────────────────────┐
                                                                     │  Radar Chart +       │
                                                                     │  Summary +           │
                                                                     │  Role Recommendations│
                                                                     └──────────────────────┘
```

1. **Upload** — User uploads a CV in PDF, DOCX, or TXT format
2. **Extract** — Text is extracted using PyPDF2 (PDF) or python-docx (DOCX)
3. **Tokenize** — NLTK cleans and tokenizes the text, removing stopwords
4. **Score** — Each word is checked against a curated OCEAN keyword dictionary; scores are normalized per trait
5. **Visualize** — Results are displayed as a radar chart with summary and career recommendations
6. **Save** — All results are stored in SQLite for later review in the History page

---

## 📸 Screenshots

| Dashboard | History | Settings |
|---|---|---|
| ![Dashboard](https://via.placeholder.com/250x160?text=Dashboard) | ![History](https://via.placeholder.com/250x160?text=History) | ![Settings](https://via.placeholder.com/250x160?text=Settings) |

> 💡 Replace placeholders above with actual screenshots of your running app.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: your feature description"`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

### Ideas for contributions
- [ ] Integrate a real pre-trained NLP model (e.g., BERT, spaCy)
- [ ] Add resume parsing for structured data extraction
- [ ] Export full report as PDF
- [ ] Add batch CV upload and comparison
- [ ] Deploy to Streamlit Cloud / Docker

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Ali Haider Butt**
Senior ML/AI Developer · 20+ Years Experience

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ali-haider-butt-3389183a8)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/alibutt2882)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:alihaiderbutt2060@gmail.com)

<br/>

*If you find this project useful, please consider giving it a ⭐ on GitHub!*

© 2024 CV Personality Analyzer. All rights reserved.

</div>
