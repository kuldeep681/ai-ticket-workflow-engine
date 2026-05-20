from pathlib import Path
import joblib

# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SAVED_MODELS_DIR = BASE_DIR / "saved_models"

MODEL_PATH = SAVED_MODELS_DIR / "routing_model.pkl"

VECTORIZER_PATH = SAVED_MODELS_DIR / "routing_vectorizer.pkl"

# =========================================================
# LOAD MODEL + VECTORIZER
# =========================================================

print("Loading routing model...")

model = joblib.load(MODEL_PATH)

print("Loading routing vectorizer...")

vectorizer = joblib.load(VECTORIZER_PATH)

print("Routing inference layer ready!")

# =========================================================
# PREDICTION FUNCTION
# =========================================================

def predict_ticket_department(ticket_text: str) -> str:
    """
    Predict department using routing ML model.
    """

    if not ticket_text:
        return "IT_SUPPORT"

    text_vector = vectorizer.transform([ticket_text])

    prediction = model.predict(text_vector)

    return prediction[0]

# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    sample_ticket = "VPN not connecting after password reset"

    predicted_department = predict_ticket_department(
        sample_ticket
    )

    print("\n===================================")
    print(f"Ticket: {sample_ticket}")
    print(f"Predicted Department: {predicted_department}")
    print("===================================\n")