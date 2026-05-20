from pathlib import Path
import joblib

# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SAVED_MODELS_DIR = BASE_DIR / "saved_models"

MODEL_PATH = SAVED_MODELS_DIR / "classifier_model.pkl"

VECTORIZER_PATH = SAVED_MODELS_DIR / "tfidf_vectorizer.pkl"

# =========================================================
# LOAD MODEL + VECTORIZER
# =========================================================

print("Loading classifier model...")

model = joblib.load(MODEL_PATH)

print("Loading TF-IDF vectorizer...")

vectorizer = joblib.load(VECTORIZER_PATH)

print("Inference layer ready!")

# =========================================================
# PREDICTION FUNCTION
# =========================================================

def predict_ticket_category(ticket_text: str) -> str:
    """
    Predict ticket category using trained ML model.
    """

    if not ticket_text:
        return "GENERAL"

    # vectorize input text
    text_vector = vectorizer.transform([ticket_text])

    # predict category
    prediction = model.predict(text_vector)

    return prediction[0]

# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    sample_ticket = "VPN not connecting after password reset"

    predicted_category = predict_ticket_category(sample_ticket)

    print("\n===================================")
    print(f"Ticket: {sample_ticket}")
    print(f"Predicted Category: {predicted_category}")
    print("===================================\n")