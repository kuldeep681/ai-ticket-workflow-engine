from sentence_transformers import (
    SentenceTransformer
)

# =========================================================
# LOAD EMBEDDING MODEL
# =========================================================

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding model loaded!")

# =========================================================
# GENERATE EMBEDDINGS
# =========================================================

def generate_embeddings(
    text_chunks: list[str]
):

    embeddings = embedding_model.encode(
        text_chunks,
        show_progress_bar=True
    )

    return embeddings