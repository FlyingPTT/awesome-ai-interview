# LLM System Design Interview Notes

## Answer Framework

For LLM system design questions, use this structure:

1. Clarify the use case.
2. Define users and constraints.
3. Sketch the high-level architecture.
4. Discuss data flow.
5. Discuss model and retrieval choices.
6. Discuss evaluation.
7. Discuss latency, cost, and reliability.
8. Discuss safety and monitoring.

## Example Question

Design an enterprise knowledge assistant.

## Strong Answer Outline

### Requirements

- Employees ask questions over internal documents.
- Answers must include citations.
- The system should refuse when evidence is insufficient.
- Documents update frequently.
- Access control must be respected.

### Architecture

- Document connector.
- Parser.
- Chunker.
- Embedding service.
- Vector database.
- Metadata index.
- Retriever.
- Reranker.
- LLM answer generator.
- Evaluation and monitoring service.

### Key Tradeoffs

- Chunk size affects retrieval precision and context completeness.
- Hybrid retrieval is more robust than dense retrieval alone.
- Reranking improves quality but adds latency.
- Strong citation tracking requires source ids throughout the pipeline.
- Access control should be enforced before retrieval and before generation.

### Evaluation

- Retrieval recall.
- Answer faithfulness.
- Citation correctness.
- Refusal accuracy.
- Latency.
- Cost per query.

