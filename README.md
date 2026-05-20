# PHASE 1 — CORE APPLICATION FOUNDATION

# Overview

Phase 1 focused on building the foundational full-stack AI Ticket Automation System using only local and open-source tools.

The primary goal of this phase was NOT advanced AI reasoning.

Instead, the focus was:

- building scalable architecture
- creating persistent storage
- implementing modular backend design
- integrating local AI safely
- preparing for future AI intelligence layers

By the end of Phase 1, the system became a production-style local AI ticket platform with:

- FastAPI backend
- React frontend
- SQLite persistence
- local LLM integration through Ollama
- workflow tracking
- conversational ticket system
- modular architecture for future expansion

---

# Final Phase 1 Architecture

```text
Frontend (React + Tailwind)
        ↓
API Layer (Axios)
        ↓
FastAPI Routes
        ↓
Service Layer
        ↓
Repository Layer
        ↓
SQLite Database
```

AI Flow:

```text
Frontend
   ↓
FastAPI
   ↓
Conversation Service
   ↓
Ollama Service
   ↓
Local LLM (Mistral)
   ↓
Response Sanitization
   ↓
Persistent Conversation Storage
```

---

# Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- React Router DOM

## Backend

- FastAPI
- Python
- SQLAlchemy
- Pydantic

## Database

- SQLite

## AI

- Ollama
- Mistral

---

# Important Architectural Principles

## 1. Thin Routes

Routes only:

- receive requests
- validate requests
- call services
- return responses

NO business logic exists inside routes.

---

## 2. Service Layer

Business logic belongs inside services.

Examples:

```text
services/
├── ticket_service.py
├── conversation_service.py
├── workflow_service.py
└── ollama_service.py
```

---

## 3. Repository Layer

Repositories handle ONLY database operations.

This separation:

- prevents SQL chaos
- improves maintainability
- simplifies future DB migration
- keeps services clean

---

## 4. AI Isolation

AI logic remains isolated from application logic.

Benefits:

- backend survives if AI crashes
- models can be swapped easily
- future RAG integration becomes easier
- future agent systems become modular

---

# Final Project Structure

```text
ticket-automation-system/
│
├── frontend/
├── backend/
├── database/
├── docs/
└── README.md
```

---

# Frontend Structure

```text
frontend/
│
├── src/
│   ├── api/
│   ├── components/
│   ├── hooks/
│   ├── layouts/
│   ├── pages/
│   ├── types/
│   ├── utils/
│   ├── App.jsx
│   └── main.jsx
│
├── public/
├── package.json
└── vite.config.js
```

---

# Backend Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
└── .env
```

---

# Database Design

## Database Choice

SQLite

Reason:

- lightweight
- local
- beginner friendly
- easy debugging
- ideal for architectural foundation

---

# Database Tables

## 1. tickets

Stores ticket information.

### Columns

| Column      | Type     |
| ----------- | -------- |
| id          | Integer  |
| title       | String   |
| description | Text     |
| status      | String   |
| priority    | String   |
| created_at  | DateTime |
| updated_at  | DateTime |

---

## Ticket Statuses

```text
OPEN
IN_PROGRESS
RESOLVED
CLOSED
```

---

## 2. conversations

Stores ticket conversations.

### Columns

| Column    | Type     |
| --------- | -------- |
| id        | Integer  |
| ticket_id | Integer  |
| sender    | String   |
| message   | Text     |
| timestamp | DateTime |

---

## Sender Types

```text
user
ai
system
```

---

## 3. workflow_logs

Tracks workflow actions.

### Columns

| Column    | Type     |
| --------- | -------- |
| id        | Integer  |
| ticket_id | Integer  |
| action    | String   |
| details   | Text     |
| timestamp | DateTime |

---

## Workflow Actions

```text
TICKET_CREATED
STATUS_UPDATED
MESSAGE_ADDED
AI_RESPONSE_GENERATED
```

---

# Relationships

```text
tickets
   ↓
conversations

tickets
   ↓
workflow_logs
```

---

# Backend Features Implemented

## Step 1 — Backend Skeleton

Implemented:

- FastAPI initialization
- modular folder structure
- configuration system
- environment variable management
- health routes
- root API route

---

## Step 2 — SQLite Integration

Implemented:

- SQLAlchemy engine
- session management
- database dependencies
- Base model architecture
- SQLite initialization

---

## Step 3 — Ticket CRUD System

Implemented:

- ticket model
- ticket repository
- ticket service
- ticket schemas
- create ticket API
- get tickets API
- get single ticket API
- update status API

---

# Ticket APIs

## Create Ticket

```http
POST /tickets
```

---

## Get All Tickets

```http
GET /tickets
```

---

## Get Single Ticket

```http
GET /tickets/{id}
```

---

## Update Ticket Status

```http
PATCH /tickets/{id}/status
```

---

# Ticket Service Responsibilities

The service layer handles:

- ticket validation
- business rules
- workflow logging
- repository coordination

Repositories only handle database operations.

---

# API Response Standard

## Success

```json
{
  "success": true,
  "data": {}
}
```

---

## Error

```json
{
  "success": false,
  "error": "Message"
}
```

---

# Current Phase 1 Status

At this point the system supports:

- persistent tickets
- modular backend architecture
- SQLite integration
- clean API design
- scalable architecture foundation

---

this is phase 1 and it is completed already now we want to move to phase 2

<!-- # Next Documentation Part

Part 2 will include:

* Conversation System
* Workflow Logs
* Ollama Integration
* AI Response Sanitization
* Frontend System
* React + Tailwind UI
* Final Testing Flow
* Phase 1 Final Outcome
* Future Phase Preparation -->

# PHASE 2 — MACHINE LEARNING + RAG

# Goal

Add the intelligence layer to the Ticket Automation System.

Phase 1 created:

- stable backend
- persistent database
- ticket management
- conversation handling
- local AI chat

Phase 2 introduces:

- machine learning
- semantic retrieval
- contextual AI responses
- document understanding

This phase transforms the system from:
"AI chat application"

into:

"Context-aware enterprise support assistant"

---

# Main Objectives

The system should now be able to:

- classify tickets automatically
- predict ticket priority
- route tickets to departments
- retrieve relevant company knowledge
- answer using grounded information
- generate contextual AI responses

---

# Core Technologies

## ML

- scikit-learn

## Embeddings

- sentence-transformers

## Vector Database

- ChromaDB

## Local LLMs

- Ollama
- Gemma
- Llama
- Mistral

---

# New Capabilities

## 1. Ticket Classification

Automatically detect:

- VPN issue
- Password reset
- Network issue
- Software issue
- Hardware issue

---

## 2. Priority Prediction

Predict:

- LOW
- MEDIUM
- HIGH
- CRITICAL

---

## 3. Department Routing

Automatically assign:

- IT Support
- Security
- Network Team
- HR Systems
- DevOps

---

## 4. Document Understanding

The system can:

- read documents
- split into chunks
- generate embeddings
- store vectors
- retrieve relevant information

---

## 5. Retrieval-Augmented Generation (RAG)

AI responses become grounded in:

- uploaded documents
- internal SOPs
- troubleshooting guides
- company policies

Instead of hallucinating.

---

# Phase 2 Outcome

The AI system becomes:

- contextual
- grounded
- searchable
- intelligent
- enterprise-ready

WITHOUT introducing agents yet.

# PHASE 2 ARCHITECTURE

# High-Level Architecture

```text
User Query
    ↓
FastAPI Backend
    ↓
Classification Layer
    ↓
Retrieval Layer
    ↓
Prompt Builder
    ↓
Ollama LLM
    ↓
Grounded Response
```

---

# New Architectural Layers

Phase 2 adds:

## ML Layer

Handles:

- classification
- priority prediction
- routing

---

## Embedding Layer

Handles:

- vector generation
- semantic representation

---

## Retrieval Layer

Handles:

- semantic search
- document retrieval
- context fetching

---

## RAG Layer

Combines:

- retrieved context
- ticket history
- user query

before sending to LLM.

---

# Updated System Flow

```text
Ticket Created
    ↓
ML Classification
    ↓
Priority Prediction
    ↓
Department Routing
    ↓
Conversation Starts
    ↓
User Query
    ↓
Embedding Generation
    ↓
Vector Search
    ↓
Relevant Chunks Retrieved
    ↓
Prompt Construction
    ↓
LLM Response
```

---

# Why RAG Matters

Without RAG:

- hallucinations increase
- generic responses
- unreliable troubleshooting

With RAG:

- grounded responses
- accurate troubleshooting
- contextual enterprise support

---

# Phase 2 Design Principles

## 1. Keep ML Modular

Do NOT mix ML directly into routes.

Create dedicated services:

- classification_service.py
- embedding_service.py
- retrieval_service.py

---

## 2. AI Must Stay Replaceable

The system should allow:

- model swapping
- embedding swapping
- vector DB replacement

---

## 3. RAG Must Be Optional

System should still function if:

- ChromaDB fails
- no documents exist
- embeddings unavailable

Fallback:
normal AI response.

---

# Future Compatibility

This architecture prepares for:

## Phase 3

- memory systems
- workflow reasoning

## Phase 4

- multi-agent orchestration

# PHASE 2 PROJECT STRUCTURE

# Updated Backend Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── ml/
│   ├── rag/
│   ├── vectorstore/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
```

---

# New Folders

# ml/

Machine learning logic.

Examples:

- classifier.py
- priority_model.py
- routing_model.py
- training_pipeline.py

---

# rag/

RAG pipeline logic.

Examples:

- chunking.py
- prompt_builder.py
- retrieval_pipeline.py

---

# vectorstore/

Vector DB management.

Examples:

- chroma_client.py
- vector_manager.py

---

# Recommended Service Files

```text
services/
│
├── classification_service.py
├── embedding_service.py
├── retrieval_service.py
├── rag_service.py
├── document_service.py
└── ollama_service.py
```

---

# Why This Separation Matters

This prevents:

- tightly coupled AI code
- giant RAG files
- unmaintainable pipelines

And allows:

- model replacement
- scaling
- experimentation

# MACHINE LEARNING DESIGN

# Goal

Introduce lightweight ML models for:

- classification
- routing
- prioritization

Using:

- scikit-learn

---

# Why scikit-learn

Advantages:

- lightweight
- beginner-friendly
- fast training
- easy debugging
- enough for ticket classification

Avoid deep learning initially.

---

# ML Tasks

# 1. Ticket Classification

Input:

```text
"VPN not connecting after password reset"
```

Output:

```text
VPN_ISSUE
```

---

# 2. Priority Prediction

Input:

```text
"Entire office network is down"
```

Output:

```text
CRITICAL
```

---

# 3. Department Routing

Input:

```text
"Email server login failure"
```

Output:

```text
IT_SUPPORT
```

---

# Recommended Models

## Start Simple

Use:

- Logistic Regression
- Naive Bayes

Later upgrade if needed.

---

# Feature Extraction

Use:

```python
TfidfVectorizer
```

For converting text into ML features.

---

# Training Pipeline

```text
Dataset
   ↓
Cleaning
   ↓
TF-IDF
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Evaluation
   ↓
Saved Model
```

---

# Storage

Save trained models locally using:

```python
joblib
```

Example:

```text
models/
├── classifier.pkl
├── priority_model.pkl
└── routing_model.pkl
```

---

# Important Rule

Keep ML separate from LLMs.

ML:

- structured prediction

LLM:

- language generation

DO NOT confuse both.

# RAG ARCHITECTURE

# Goal

Enable grounded AI responses using company knowledge.

---

# RAG Pipeline

```text
Document Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding Generation
    ↓
Store in ChromaDB
```

Query flow:

```text
User Question
    ↓
Generate Query Embedding
    ↓
Vector Search
    ↓
Retrieve Relevant Chunks
    ↓
Build Prompt
    ↓
Send to LLM
    ↓
Grounded Response
```

---

# Supported Documents

Examples:

- SOPs
- troubleshooting guides
- company policies
- VPN setup docs
- onboarding docs

---

# Chunking Strategy

Start simple.

Recommended:

- fixed chunk size
- overlap chunks

Example:

- chunk size: 500
- overlap: 100

---

# Embedding Model

Recommended starter:

```text
all-MiniLM-L6-v2
```

Using:

```python
sentence-transformers
```

---

# Why Embeddings Matter

Embeddings convert text into semantic vectors.

This enables:

- meaning-based search
  instead of:
- keyword matching

---

# Vector Database

Use:

- ChromaDB

Advantages:

- local
- lightweight
- easy setup
- beginner-friendly

---

# Prompt Construction

Retrieved chunks become context.

Example:

```text
Context:
VPN troubleshooting steps...

User Question:
VPN not connecting after password reset

Answer using context only.
```

---

# Anti-Hallucination Rule

Always instruct the LLM:

```text
Answer ONLY using provided context.
If information is missing, say so.
```

---

# Important Design Rule

RAG must remain modular.

Do NOT tightly couple:

- embeddings
- retrieval
- prompt building
- LLM calls

Each should be independently replaceable.

# PHASE 2 IMPLEMENTATION ORDER

# IMPORTANT

Build ONLY after Phase 1 is stable.

---

# STEP 1 — ML Dataset Preparation

Build:

- ticket datasets
- labels
- preprocessing pipeline

Goal:
Training data ready.

---

# STEP 2 — Ticket Classification

Build:

- TF-IDF vectorizer
- classifier model
- prediction service

Goal:
Automatic ticket category prediction.

---

# STEP 3 — Priority Prediction

Build:

- priority model
- prediction API

Goal:
Automatic urgency detection.

---

# STEP 4 — Department Routing

Build:

- routing model
- routing logic

Goal:
Automatic department assignment.

---

# STEP 5 — Document Upload System

Build:

- file upload API
- document storage
- text extraction

Goal:
Documents enter system.

---

# STEP 6 — Chunking Pipeline

Build:

- chunk splitter
- overlap logic

Goal:
Documents split into semantic chunks.

---

# STEP 7 — Embedding Generation

Build:

- sentence-transformers integration
- embedding service

Goal:
Generate vector embeddings.

---

# STEP 8 — ChromaDB Integration

Build:

- vector storage
- vector retrieval

Goal:
Semantic search works.

---

# STEP 9 — Retrieval Pipeline

Build:

- similarity search
- relevant chunk retrieval

Goal:
Relevant context retrieval works.

---

# STEP 10 — RAG Prompt Builder

Build:

- context injection
- grounding instructions

Goal:
LLM receives grounded prompts.

---

# STEP 11 — Grounded AI Responses

Build:

- RAG endpoint
- contextual answer generation

Goal:
AI answers using retrieved knowledge.

---

# STEP 12 — End-to-End Testing

Test:

- retrieval quality
- grounding quality
- hallucination reduction
- ML predictions

Goal:
Full intelligent AI support pipeline works.

---

# Final Deliverable

At the end of Phase 2:

✅ Ticket classification works

✅ Priority prediction works

✅ Department routing works

✅ ChromaDB works

✅ Embeddings work

✅ Semantic retrieval works

✅ Grounded AI responses work

✅ Architecture remains modular

✅ Ready for Phase 3 memory systems
