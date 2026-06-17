# RAG Interview Notes

## System Design Template

When asked to design a RAG system, cover:

1. Use case and constraints.
2. Data source and freshness.
3. Parsing and chunking.
4. Embedding and indexing.
5. Retrieval strategy.
6. Reranking.
7. Prompt construction.
8. Citation and refusal.
9. Evaluation.
10. Monitoring and iteration.

## Common Questions

### How do you debug poor RAG answers?

Start by separating retrieval failure from generation failure.

- If the right evidence is not retrieved, inspect parsing, chunking, embeddings, filters, query rewriting, and reranking.
- If the right evidence is retrieved but the answer is wrong, inspect prompt design, context ordering, citation requirements, and model behavior.
- If answers are inconsistent, add regression tests and track retrieval and generation metrics separately.

### What makes chunking difficult?

Chunking must balance recall and precision. Chunks that are too small may lose context. Chunks that are too large may dilute relevant evidence and waste context window. Good chunking often uses document structure such as headings, tables, paragraphs, and metadata.

### Why use reranking?

Embedding retrieval is optimized for fast candidate search, not final evidence ordering. A reranker can apply a more expensive relevance model to a smaller candidate set, improving answer grounding and reducing irrelevant context.

### How do you evaluate RAG?

Evaluate both retrieval and generation.

- Retrieval: recall, precision, MRR, nDCG, context relevance.
- Generation: faithfulness, answer correctness, citation accuracy, refusal quality.
- System: latency, cost, freshness, user satisfaction.

