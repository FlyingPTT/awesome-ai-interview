# Runnable Examples

Small, dependency-free examples that turn the repository's interview notes into runnable code.

## Examples

- [Minimal Agent Framework](minimal-agent-framework/): model-tool-observation loop with explicit state, tool registry, schema validation, step budget, and trajectory logging.
- [LLM Eval Harness](llm-eval-harness/): versioned test cases, deterministic model wrapper, evaluators, latency tracking, and pass/fail reporting.
- [RAG Mini System](rag-mini-system/): local Markdown ingestion, BM25-style retrieval, cited answers, and refusal behavior.
- [Model Router](model-router/): risk and complexity routing between cheap and strong models with cost and latency estimates.
- [RAG Eval Set](rag-eval-set/): answerable/unanswerable evaluation cases, citation checks, retrieval checks, and report export.

## Why These Examples Matter

These examples are intentionally small. They are designed for interview discussion:

- How do agents decide which tool to call?
- How do we validate tool arguments?
- How do we prevent runaway loops?
- How do we evaluate LLM behavior repeatedly?
- How do we build release gates for prompt and model changes?
- How do we build a tiny RAG pipeline with citations?
- How do we route tasks by cost, latency, risk, and complexity?
- How do we turn a RAG demo into a regression-tested workflow?
