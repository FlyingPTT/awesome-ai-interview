# RAG Eval Set

A small evaluation set for the local [RAG Mini System](../rag-mini-system/).

It demonstrates:

- Answerable and unanswerable questions.
- Expected source document checks.
- Citation checks.
- Retrieval hit checks.
- Keyword coverage checks.
- Failure analysis for retrieval, citation, refusal, and generation issues.
- JSON report export.

## Run

```bash
python3 examples/rag-eval-set/evaluate.py
```

Write a report:

```bash
python3 examples/rag-eval-set/evaluate.py --report /tmp/rag-eval-report.json
```

## Test

```bash
python3 -m unittest discover examples/rag-eval-set/tests
```

## Interview Talking Points

- RAG evaluation should include answerable and unanswerable cases.
- Retrieval quality and generation quality should be checked separately.
- Citation correctness is a first-class product metric.
- Small eval sets can become regression gates for prompt, retrieval, and chunking changes.
- Failure analysis should map symptoms to likely pipeline components.
