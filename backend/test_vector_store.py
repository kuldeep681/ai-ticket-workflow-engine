from app.rag.text_extractor import (
    extract_document_text
)

from app.rag.chunker import (
    chunk_text
)

from app.rag.embedding_model import (
    generate_embeddings
)

from app.rag.vector_store import (
    store_embeddings
)

# =========================================================
# LOAD DOCUMENT
# =========================================================

file_path = (
    "app/storage/documents/vpn_guide.txt"
)

document_name = "vpn_guide"

# =========================================================
# EXTRACT TEXT
# =========================================================

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
# STORE IN CHROMADB
# =========================================================

store_embeddings(
    chunks,
    embeddings,
    document_name
)

print("\n===================================")
print("Document stored successfully!")
print("===================================\n")