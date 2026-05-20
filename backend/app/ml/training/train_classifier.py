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

CLEANED_DATASET_DIR = BASE_DIR / "datasets" / "cleaned"
SAVED_MODELS_DIR = BASE_DIR / "saved_models"

SAVED_MODELS_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# LOAD DATASET
# =========================================================

DATASET_PATH = CLEANED_DATASET_DIR / "classification_dataset.csv"

print("Loading classification dataset...")

df = pd.read_csv(DATASET_PATH)

# =========================================================
# REMOVE INVALID ROWS
# =========================================================

df = df.dropna()

df = df[df["text"].str.len() > 5]

# =========================================================
# FEATURES + LABELS
# =========================================================

X = df["text"]

y = df["category"]

# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# =========================================================
# TF-IDF VECTORIZATION
# =========================================================

print("Vectorizing text using TF-IDF...")

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_train_vectors = vectorizer.fit_transform(X_train)

X_test_vectors = vectorizer.transform(X_test)

# =========================================================
# MODEL TRAINING
# =========================================================

print("Training Logistic Regression model...")

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
print(f"Model Accuracy: {accuracy:.4f}")
print("===================================\n")

print(classification_report(y_test, y_pred))

# =========================================================
# SAVE MODEL
# =========================================================

print("Saving model...")

joblib.dump(
    model,
    SAVED_MODELS_DIR / "classifier_model.pkl"
)

joblib.dump(
    vectorizer,
    SAVED_MODELS_DIR / "tfidf_vectorizer.pkl"
)

print("Model and vectorizer saved successfully!")