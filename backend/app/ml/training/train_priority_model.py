import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

import joblib

# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = (
    BASE_DIR
    / "datasets"
    / "cleaned"
    / "priority_dataset.csv"
)

SAVED_MODELS_DIR = BASE_DIR / "saved_models"

SAVED_MODELS_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# LOAD DATASET
# =========================================================

print("Loading priority dataset...")

df = pd.read_csv(DATASET_PATH)

# =========================================================
# CLEAN DATA
# =========================================================

df = df.dropna()

df = df[df["text"].str.len() > 5]

# =========================================================
# FEATURES + LABELS
# =========================================================

X = df["text"]

y = df["priority"]

# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================================================
# TF-IDF
# =========================================================

print("Vectorizing text...")

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_train_vectors = vectorizer.fit_transform(X_train)

X_test_vectors = vectorizer.transform(X_test)

# =========================================================
# MODEL TRAINING
# =========================================================

print("Training priority model...")

model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train_vectors, y_train)

# =========================================================
# PREDICTIONS
# =========================================================

y_pred = model.predict(X_test_vectors)

# =========================================================
# EVALUATION
# =========================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n===================================")
print(f"Priority Model Accuracy: {accuracy:.4f}")
print("===================================\n")

print(classification_report(y_test, y_pred))

# =========================================================
# SAVE MODEL
# =========================================================

joblib.dump(
    model,
    SAVED_MODELS_DIR / "priority_model.pkl"
)

joblib.dump(
    vectorizer,
    SAVED_MODELS_DIR / "priority_vectorizer.pkl"
)

print("Priority model saved successfully!")