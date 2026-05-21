from app.rag.embedding_model import (
    generate_embeddings
)

from app.rag.vector_store import (
    search_similar_chunks
)


def retrieve_relevant_chunks(
    query: str,
    workflow_domain: str = "general",
    top_k: int = 3
):

    try:

        query_embedding = (
            generate_embeddings(
                [query]
            )[0]
        )

        results = (
            search_similar_chunks(
                query_embedding=query_embedding,
                workflow_domain=workflow_domain,
                top_k=top_k
            )
        )

        documents = results.get(
            "documents",
            []
        )

        if not documents:
            return []

        if not documents[0]:
            return []

        cleaned_documents = []

        for doc in documents[0]:

            if doc and isinstance(doc, str):

                cleaned_documents.append(
                    doc.strip()
                )

        return cleaned_documents

    except Exception:

        return []