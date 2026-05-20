from app.rag.text_extractor import (
    extract_document_text
)

from app.rag.chunker import (
    chunk_text
)

# =========================================================
# LOAD DOCUMENT
# =========================================================

file_path = (
    "app/storage/documents/vpn_guide.txt"
)

text = extract_document_text(
    file_path
)

# =========================================================
# CHUNK TEXT
# =========================================================

chunks = chunk_text(text)

# =========================================================
# RESULTS
# =========================================================

print(f"\nTotal Chunks: {len(chunks)}\n")

for index, chunk in enumerate(chunks[:3]):

    print(f"\n========== CHUNK {index + 1} ==========\n")

    print(chunk)