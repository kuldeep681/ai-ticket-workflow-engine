from app.rag.text_extractor import (
    extract_document_text
)

from app.rag.chunker import (
    chunk_text
)

from app.rag.embedding_model import (
    generate_embeddings
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
# CREATE CHUNKS
# =========================================================

chunks = chunk_text(text)

# =========================================================
# GENERATE EMBEDDINGS
# =========================================================

embeddings = generate_embeddings(
    chunks
)

# =========================================================
# RESULTS
# =========================================================

print("\n===================================")

print(f"Total Chunks: {len(chunks)}")

print(f"Total Embeddings: {len(embeddings)}")

print(f"Embedding Shape: {embeddings[0].shape}")

print("===================================\n")