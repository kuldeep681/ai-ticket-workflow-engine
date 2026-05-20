from pathlib import Path
import joblib

# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SAVED_MODELS_DIR = BASE_DIR / "saved_models"

MODEL_PATH = SAVED_MODELS_DIR / "priority_model.pkl"

VECTORIZER_PATH = SAVED_MODELS_DIR / "priority_vectorizer.pkl"

# =========================================================
# LOAD MODEL + VECTORIZER
# =========================================================

print("Loading priority model...")

model = joblib.load(MODEL_PATH)

print("Loading priority vectorizer...")

vectorizer = joblib.load(VECTORIZER_PATH)

print("Priority inference layer ready!")

# =========================================================
# PREDICTION FUNCTION
# =========================================================

def predict_ticket_priority(ticket_text: str) -> str:
    """
    Predict ticket priority using ML model.
    """

    if not ticket_text:
        return "MEDIUM"
    
    text = ticket_text.lower()
    # ==========================================
    # RULE-BASED CRITICALITY OVERRIDES
    # ==========================================
    if (
        "entire office" in text
        or "system down" in text
        or "network down" in text
        or "production down" in text
        or "server outage" in text
        or "vpn" in text
        or "remote access" in text
    ):
        return "HIGH"
    
    

    # vectorize text
    text_vector = vectorizer.transform([ticket_text])

    # predict priority
    prediction = model.predict(text_vector)

    return prediction[0]

# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    sample_ticket = "Entire office network is down"

    predicted_priority = predict_ticket_priority(
        sample_ticket
    )

    print("\n===================================")
    print(f"Ticket: {sample_ticket}")
    print(f"Predicted Priority: {predicted_priority}")
    print("===================================\n")