# RAG Engineer Roadmap

RAG engineering is about making LLM applications grounded, searchable, auditable, and maintainable.

## Pipeline

1. Ingest documents.
2. Parse and normalize content.
3. Chunk content.
4. Generate embeddings.
5. Index vectors and metadata.
6. Retrieve candidates.
7. Rerank results.
8. Generate grounded answers.
9. Evaluate quality.
10. Monitor production behavior.

## Key Design Choices

### Chunking

- Fixed-size chunks.
- Semantic chunks.
- Section-aware chunks.
- Parent-child chunks.
- Sliding windows.

### Retrieval

- Dense retrieval.
- BM25.
- Hybrid retrieval.
- Metadata filtering.
- Query rewriting.
- Multi-hop retrieval.

### Generation

- Citation-aware prompting.
- Refusal when evidence is insufficient.
- Structured answers.
- Context compression.

### Evaluation

- Retrieval recall.
- Answer faithfulness.
- Context precision.
- Citation correctness.
- Latency and cost.

## Interview Questions

- Why does naive chunking often hurt RAG quality?
- How do you debug a hallucinated answer in RAG?
- How do you choose embedding models?
- When should you use reranking?
- How do you build a RAG system for constantly changing documents?

