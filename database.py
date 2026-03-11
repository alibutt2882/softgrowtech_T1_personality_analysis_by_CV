import sqlite3
import bcrypt
from datetime import datetime
import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cv_analyzer.db')

def init_database():
    """Initialize database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        full_name TEXT,
        profile_pic TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create cv_analyses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cv_analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        personality_traits TEXT,
        openness REAL,
        conscientiousness REAL,
        extraversion REAL,
        agreeableness REAL,
        emotional_stability REAL,
        summary TEXT,
        recommendations TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    # Create user_settings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_settings (
        user_id INTEGER PRIMARY KEY,
        theme TEXT DEFAULT 'light',
        email_notifications BOOLEAN DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    conn.commit()
    conn.close()

def create_user(username, email, password, full_name=""):
    """Create a new user"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Hash password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    try:
        cursor.execute('''
        INSERT INTO users (username, email, password, full_name)
        VALUES (?, ?, ?, ?)
        ''', (username, email, hashed, full_name))

        user_id = cursor.lastrowid

        # Create default settings for user
        cursor.execute('''
        INSERT INTO user_settings (user_id)
        VALUES (?)
        ''', (user_id,))

        conn.commit()
        return True, "User created successfully", user_id
    except sqlite3.IntegrityError as e:
        return False, "Username or email already exists", None
    finally:
        conn.close()

def verify_user(username_or_email, password):
    """Verify user credentials"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id, username, email, password, full_name
    FROM users
    WHERE username = ? OR email = ?
    ''', (username_or_email, username_or_email))

    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[3]):
        return True, {
            'id': user[0],
            'username': user[1],
            'email': user[2],
            'full_name': user[4]
        }
    return False, None

def save_cv_analysis(user_id, filename, traits, scores, summary, recommendations):
    """Save CV analysis results"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO cv_analyses
    (user_id, filename, personality_traits, openness, conscientiousness,
     extraversion, agreeableness, emotional_stability, summary, recommendations)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user_id, filename, json.dumps(traits),
        scores['openness'], scores['conscientiousness'],
        scores['extraversion'], scores['agreeableness'],
        scores['emotional_stability'], summary, recommendations
    ))

    analysis_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return analysis_id

def get_user_history(user_id):
    """Get CV analysis history for a user"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id, filename, analysis_date, openness, conscientiousness,
           extraversion, agreeableness, emotional_stability
    FROM cv_analyses
    WHERE user_id = ?
    ORDER BY analysis_date DESC
    ''', (user_id,))

    history = cursor.fetchall()
    conn.close()

    return [{
        'id': h[0],
        'filename': h[1],
        'date': h[2],
        'traits': {
            'openness': h[3],
            'conscientiousness': h[4],
            'extraversion': h[5],
            'agreeableness': h[6],
            'emotional_stability': h[7]
        }
    } for h in history]

def get_user_settings(user_id):
    """Get user settings"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT theme, email_notifications FROM user_settings WHERE user_id = ?', (user_id,))
    settings = cursor.fetchone()
    conn.close()

    return {'theme': settings[0], 'email_notifications': settings[1]} if settings else None

def update_user_settings(user_id, theme, email_notifications):
    """Update user settings"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE user_settings
    SET theme = ?, email_notifications = ?
    WHERE user_id = ?
    ''', (theme, email_notifications, user_id))

    conn.commit()
    conn.close()

def update_user_profile(user_id, full_name, email):
    """Update user profile"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE users
    SET full_name = ?, email = ?
    WHERE id = ?
    ''', (full_name, email, user_id))

    conn.commit()
    conn.close()

def get_analysis_by_id(analysis_id, user_id):
    """Get a specific analysis by ID"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id, filename, analysis_date, personality_traits, openness, conscientiousness,
           extraversion, agreeableness, emotional_stability, summary, recommendations
    FROM cv_analyses
    WHERE id = ? AND user_id = ?
    ''', (analysis_id, user_id))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'id': row[0],
            'filename': row[1],
            'date': row[2],
            'personality_traits': json.loads(row[3]) if row[3] else {},
            'scores': {
                'openness': row[4],
                'conscientiousness': row[5],
                'extraversion': row[6],
                'agreeableness': row[7],
                'emotional_stability': row[8]
            },
            'summary': row[9],
            'recommendations': row[10]
        }
    return None

def delete_analysis(analysis_id, user_id):
    """Delete a specific analysis"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM cv_analyses
    WHERE id = ? AND user_id = ?
    ''', (analysis_id, user_id))

    conn.commit()
    conn.close()
