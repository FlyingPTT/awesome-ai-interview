# RAG Paper Map

This page tracks papers and technical topics that help candidates understand Retrieval-Augmented Generation systems.

## Core Questions

- How should knowledge be retrieved?
- How should retrieved context be ranked and compressed?
- How do we evaluate faithfulness?
- How do we handle multi-hop questions?
- How do we build reliable production RAG systems?

## Reading Order

### 1. Retrieval Foundations

Study:

- Sparse retrieval such as BM25.
- Dense retrieval with dual encoders.
- Hybrid retrieval.
- Query expansion and query rewriting.

Interview takeaway:

- Dense retrieval is strong for semantic matching, while sparse retrieval is strong for exact terms. Production RAG often combines both.

### 2. RAG Architecture

Study:

- Retrieval-augmented generation.
- Fusion-in-decoder style architectures.
- Retrieve-then-read pipelines.
- Retrieval-augmented pretraining and inference-time retrieval.

Interview takeaway:

- RAG is not one algorithm. It is a family of systems that connect data pipelines, retrieval, ranking, generation, and evaluation.

### 3. Reranking And Context Selection

Study:

- Cross-encoder rerankers.
- Context compression.
- Lost-in-the-middle behavior.
- Long-context retrieval strategies.

Interview takeaway:

- More retrieved context does not always improve answer quality. Context precision matters.

### 4. Evaluation

Study:

- Retrieval recall.
- Context relevance.
- Faithfulness.
- Citation correctness.
- Refusal quality.

Interview takeaway:

- Evaluate retrieval and generation separately. A correct final answer can hide retrieval failures, and good retrieval can still lead to bad generation.

## Implementation Notes

- Preserve metadata from ingestion to citation.
- Add unanswerable questions to evaluation.
- Test access control with adversarial users.
- Keep document freshness observable.
- Log retrieved chunks for debugging.

## Interview Questions

- Why does naive chunking fail?
- How do you evaluate RAG without gold answers?
- When should you use reranking?
- How do you design RAG for frequently changing documents?
- How do you detect unsupported claims?

