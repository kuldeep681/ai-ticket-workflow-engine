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
    document_name,
    workflow_domain="general"
):

    ids = []

    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(
            f"{document_name}_{index}"
        )

        metadatas.append({

            "document":
            document_name,

            "chunk_index":
            index,

            "workflow_domain":
            workflow_domain
        })

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas,
        ids=ids
    )

    print(
        f"Stored {len(chunks)} chunks "
        f"for domain {workflow_domain}"
    )

# =========================================================
# SEMANTIC SEARCH
# =========================================================

def search_similar_chunks(
    query_embedding,
    workflow_domain="general",
    top_k: int = 3
):

    query_payload = {

        "query_embeddings": [
            query_embedding.tolist()
        ],

        "n_results": top_k
    }

    # ==============================================
    # DOMAIN FILTERING
    # ==============================================

    if workflow_domain != "general":

        query_payload["where"] = {

            "workflow_domain":
            workflow_domain
        }

    results = collection.query(
        **query_payload
    )

    return results