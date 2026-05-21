import os

from sentence_transformers import (
    SentenceTransformer
)

# =========================================================
# FORCE OFFLINE MODE
# =========================================================

os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

os.environ["TRANSFORMERS_OFFLINE"] = "1"

os.environ["HF_DATASETS_OFFLINE"] = "1"

# =========================================================
# LOAD EMBEDDING MODEL
# =========================================================

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    local_files_only=True
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