import chromadb

# =========================================================
# CREATE CHROMADB CLIENT
# =========================================================

client = chromadb.PersistentClient(
    path="app/chroma_db"
)

# =========================================================
# CREATE COLLECTION
# =========================================================

collection = client.get_or_create_collection(
    name="enterprise_knowledge"
)

# =========================================================
# STORE CHUNKS + EMBEDDINGS
# =========================================================

def store_embeddings(
    chunks,
    embeddings,
    document_name
):

    ids = []

    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(
            f"{document_name}_{index}"
        )

        metadatas.append(
            {
                "document": document_name,
                "chunk_index": index
            }
        )

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas,
        ids=ids
    )

    print(
        f"Stored {len(chunks)} chunks in ChromaDB."
    )

# =========================================================
# SEMANTIC SEARCH
# =========================================================

def search_similar_chunks(
    query_embedding,
    top_k: int = 3
):

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=top_k
    )

    return results