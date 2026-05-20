from app.rag.retriever import (
    retrieve_relevant_chunks
)

# =========================================================
# TEST QUERY
# =========================================================

query = (
    "VPN not connecting after password reset"
)

# =========================================================
# RETRIEVE CHUNKS
# =========================================================

results = retrieve_relevant_chunks(
    query
)

# =========================================================
# DISPLAY RESULTS
# =========================================================

print("\n===================================")

print(f"Query: {query}")

print("===================================\n")

for index, chunk in enumerate(results):

    print(f"\n========== RESULT {index + 1} ==========\n")

    print(chunk)