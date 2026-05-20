import requests

from app.rag.retriever import (
    retrieve_relevant_chunks
)

# =========================================================
# OLLAMA CONFIG
# =========================================================

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "mistral"

# =========================================================
# BUILD CONTEXT
# =========================================================

def build_context(
    retrieved_chunks
):

    return "\n\n".join(retrieved_chunks)

# =========================================================
# GENERATE RAG RESPONSE
# =========================================================

def generate_rag_response(
    question: str
):

    # ==============================================
    # RETRIEVE RELEVANT CHUNKS
    # ==============================================

    retrieved_chunks = retrieve_relevant_chunks(
        question
    )

    # ==============================================
    # BUILD CONTEXT
    # ==============================================

    context = build_context(
        retrieved_chunks
    )

    # ==============================================
    # BUILD PROMPT
    # ==============================================

    prompt = f"""
You are an enterprise IT support assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say:
"I could not find relevant information in the knowledge base."

================ CONTEXT ================

{context}

================ QUESTION ================

{question}

================ ANSWER ================
"""

    # ==============================================
    # OLLAMA REQUEST
    # ==============================================

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return {
        "question": question,
        "answer": result["response"],
        "sources": retrieved_chunks
    }