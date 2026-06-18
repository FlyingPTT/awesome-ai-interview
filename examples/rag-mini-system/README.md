# RAG Mini System

A dependency-free mini RAG system over local Markdown files.

It demonstrates:

- Local document ingestion.
- Tokenization.
- Sparse BM25-style retrieval.
- Dense mock retrieval with token-overlap similarity.
- Hybrid score fusion.
- Grounded answer synthesis.
- Citations.
- Refusal when evidence is weak.

## Run

```bash
python3 examples/rag-mini-system/run_demo.py
```

## Test

```bash
python3 -m unittest discover examples/rag-mini-system/tests
```

## Files

- `docs/`: local Markdown knowledge base.
- `rag.py`: retrieval, scoring, and answer synthesis.
- `run_demo.py`: runnable demo.
- `tests/`: unit tests.

## Interview Talking Points

- RAG quality depends on parsing, chunking, retrieval, reranking, generation, citation, and evaluation.
- Retrieval failure and generation failure should be debugged separately.
- Refusal behavior is a product requirement, not just a prompt trick.
- Even a tiny RAG system should expose retrieved evidence and scores.
- Hybrid retrieval often improves robustness because sparse retrieval handles exact terms while dense retrieval handles semantic overlap.
