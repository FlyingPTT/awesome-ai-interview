# Project: Production RAG System

## Goal

Build a RAG system that answers questions over a private document collection with citations and refusal behavior.

## Architecture

- Document ingestion.
- PDF and Markdown parsing.
- Section-aware chunking.
- Embedding and vector index.
- Hybrid retrieval.
- Reranking.
- Grounded answer generation.
- Evaluation dashboard.

## Technical Highlights

- Parent-child chunking for better context.
- Hybrid retrieval for robustness.
- Reranking for evidence precision.
- Citation tracking from source document to answer.
- Regression set for prompt and retrieval changes.

## Resume Bullet

Built a production-style RAG system over private documents with hybrid retrieval, reranking, citation tracking, and evaluation metrics for answer faithfulness, retrieval recall, latency, and cost.

## Interview Talking Points

- Why chunking strategy matters.
- Why retrieval and generation should be evaluated separately.
- How to handle stale documents.
- How to reduce hallucination.

