# LLM Evaluation Interview Notes

## Why Evaluation Matters

LLM applications are probabilistic systems. Prompt changes, model upgrades, data changes, and retrieval changes can all introduce regressions. Evaluation is the main mechanism for shipping safely.

## Evaluation Types

### Exact Evaluation

Useful when the output has a deterministic answer, such as classification, extraction, or structured fields.

### Semantic Evaluation

Useful when multiple answers may be valid. This often uses embeddings, rubrics, or LLM-as-a-judge.

### Human Evaluation

Useful for high-risk, subjective, or product-critical cases.

### System Evaluation

Measures latency, cost, reliability, safety, and user satisfaction.

## Common Metrics

- Accuracy.
- Faithfulness.
- Relevance.
- Helpfulness.
- Refusal quality.
- Tool-call accuracy.
- Retrieval recall.
- Citation correctness.
- Cost per successful task.
- Human intervention rate.

## Interview Questions

- How do you evaluate a chatbot without a single correct answer?
- How do you prevent LLM-as-a-judge bias?
- How do you evaluate an AI agent?
- How do you build a regression test suite for prompts?
- How do you evaluate RAG retrieval and generation separately?

