"""
Personality Prediction Model Module
Author: Ali Haider Butt

ML model for personality trait prediction from CV text using
TF-IDF vectorization and RandomForest classification.
"""

import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
import joblib


TRAITS = ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_stability']


class PersonalityPredictor:
    """
    Machine Learning model for personality prediction from CVs.

    Uses TF-IDF vectorization with RandomForest regression
    to predict scores for each OCEAN trait.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)  # Include bigrams for richer features
        )
        self.models = {}
        self.is_trained = False

    def train(self, cv_texts, personality_scores):
        """
        Train the model on CV texts and corresponding personality scores.

        Args:
            cv_texts (list[str]): List of CV text strings
            personality_scores (list[dict]): List of dicts with trait -> score mappings
        """
        if not cv_texts or not personality_scores:
            raise ValueError("Training data cannot be empty.")

        # Fit-transform texts to TF-IDF features
        X = self.vectorizer.fit_transform(cv_texts)

        # Train a regressor for each trait
        for trait in TRAITS:
            model = RandomForestRegressor(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                n_jobs=-1
            )
            y = [scores.get(trait, 0.5) for scores in personality_scores]
            self.models[trait] = model.fit(X, y)

        self.is_trained = True
        print(f"Model trained on {len(cv_texts)} samples.")

    def predict(self, cv_text):
        """
        Predict personality traits from a single CV text string.

        Args:
            cv_text (str): Extracted text from a CV

        Returns:
            dict: trait -> predicted score (float between 0 and 1)
        """
        if not self.is_trained:
            return self._mock_predict()

        X = self.vectorizer.transform([cv_text])
        predictions = {}
        for trait, model in self.models.items():
            raw = model.predict(X)[0]
            predictions[trait] = round(max(0.2, min(0.95, float(raw))), 2)

        return predictions

    def _mock_predict(self):
        """
        Generate mock predictions for demonstration when model is not trained.

        Returns:
            dict: trait -> random score in a realistic range
        """
        return {
            'openness': round(np.random.uniform(0.35, 0.85), 2),
            'conscientiousness': round(np.random.uniform(0.4, 0.9), 2),
            'extraversion': round(np.random.uniform(0.25, 0.8), 2),
            'agreeableness': round(np.random.uniform(0.45, 0.9), 2),
            'emotional_stability': round(np.random.uniform(0.3, 0.8), 2)
        }

    def evaluate(self, cv_texts, personality_scores):
        """
        Evaluate model performance using Mean Absolute Error per trait.

        Args:
            cv_texts (list[str]): Validation CV texts
            personality_scores (list[dict]): Ground truth scores

        Returns:
            dict: trait -> MAE score
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before evaluation.")

        from sklearn.metrics import mean_absolute_error

        X = self.vectorizer.transform(cv_texts)
        errors = {}
        for trait, model in self.models.items():
            y_true = [s.get(trait, 0.5) for s in personality_scores]
            y_pred = model.predict(X)
            errors[trait] = round(mean_absolute_error(y_true, y_pred), 4)

        return errors

    def save_model(self, path='models/'):
        """
        Save trained model artifacts to disk.

        Args:
            path (str): Directory to save model files
        """
        if not self.is_trained:
            raise RuntimeError("Cannot save an untrained model.")

        os.makedirs(path, exist_ok=True)
        joblib.dump(self.vectorizer, os.path.join(path, 'vectorizer.pkl'))
        for trait, model in self.models.items():
            joblib.dump(model, os.path.join(path, f'model_{trait}.pkl'))

        print(f"Model saved to {path}")

    def load_model(self, path='models/'):
        """
        Load trained model artifacts from disk.

        Args:
            path (str): Directory containing saved model files
        """
        try:
            self.vectorizer = joblib.load(os.path.join(path, 'vectorizer.pkl'))
            for trait in TRAITS:
                self.models[trait] = joblib.load(os.path.join(path, f'model_{trait}.pkl'))
            self.is_trained = True
            print(f"Model loaded from {path}")
        except FileNotFoundError:
            print("No pre-trained models found. Using mock predictions.")
        except Exception as e:
            print(f"Error loading model: {e}. Using mock predictions.")

    def get_feature_importance(self, trait, top_n=20):
        """
        Return top N most important features (keywords) for a given trait.

        Args:
            trait (str): One of the OCEAN traits
            top_n (int): Number of top features to return

        Returns:
            list[tuple]: [(feature_name, importance_score), ...]
        """
        if not self.is_trained or trait not in self.models:
            return []

        model = self.models[trait]
        feature_names = self.vectorizer.get_feature_names_out()
        importances = model.feature_importances_

        indices = np.argsort(importances)[::-1][:top_n]
        return [(feature_names[i], round(importances[i], 4)) for i in indices]
