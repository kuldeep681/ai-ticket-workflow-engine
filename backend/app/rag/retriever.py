from app.rag.embedding_model import (
    generate_embeddings
)

from app.rag.vector_store import (
    search_similar_chunks
)

# =========================================================
# RETRIEVE RELEVANT CHUNKS
# =========================================================

def retrieve_relevant_chunks(
    query: str,
    top_k: int = 3
):

    # ==============================================
    # GENERATE QUERY EMBEDDING
    # ==============================================

    query_embedding = generate_embeddings(
        [query]
    )[0]

    # ==============================================
    # SEARCH VECTOR DATABASE
    # ==============================================

    results = search_similar_chunks(
        query_embedding,
        top_k
    )

    # ==============================================
    # RETURN DOCUMENT CHUNKS
    # ==============================================

    return results["documents"][0]