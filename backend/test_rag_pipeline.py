from app.rag.rag_pipeline import (
    generate_rag_response
)

# =========================================================
# TEST QUESTION
# =========================================================

question = (
    "VPN stopped working after password reset"
)

# =========================================================
# GENERATE RESPONSE
# =========================================================

result = generate_rag_response(
    question
)

# =========================================================
# DISPLAY RESPONSE
# =========================================================

print("\n===================================")

print(f"Question: {result['question']}")

print("\n===================================")

print("AI RESPONSE:\n")

print(result["answer"])

print("\n===================================")

print("SOURCES USED:\n")

for source in result["sources"]:

    print(source[:300])

    print("\n-----------------------------------")