# Runnable Examples

Small, dependency-free examples that turn the repository's interview notes into runnable code.

## Examples

- [Minimal Agent Framework](minimal-agent-framework/): model-tool-observation loop with explicit state, tool registry, schema validation, step budget, and trajectory logging.
- [LLM Eval Harness](llm-eval-harness/): versioned test cases, deterministic model wrapper, evaluators, latency tracking, and pass/fail reporting.

## Why These Examples Matter

These examples are intentionally small. They are designed for interview discussion:

- How do agents decide which tool to call?
- How do we validate tool arguments?
- How do we prevent runaway loops?
- How do we evaluate LLM behavior repeatedly?
- How do we build release gates for prompt and model changes?

