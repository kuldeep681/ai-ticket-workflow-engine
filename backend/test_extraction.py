from app.rag.text_extractor import (
    extract_document_text
)

# =========================================================
# TEST DOCUMENT
# =========================================================

file_path = (
    "app/storage/documents/vpn_guide.txt"
)

# =========================================================
# EXTRACT TEXT
# =========================================================

text = extract_document_text(
    file_path
)

print("\n================ EXTRACTED TEXT ================\n")

print(text[:3000])

print("\n================================================\n")