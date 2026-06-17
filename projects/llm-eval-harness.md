# Project: LLM Evaluation Harness

## Goal

Build a small evaluation harness that can run prompts, models, tools, and expected outputs through repeatable test cases. This is a strong interview project because it shows you understand how LLM systems are shipped safely, not just demoed.

## What The Harness Should Do

- Load test cases from JSON or YAML.
- Run a prompt or workflow against a model.
- Support deterministic checks and rubric-based checks.
- Compare outputs across model versions.
- Record latency, token usage, cost, and pass/fail results.
- Export a report for regression tracking.

## Architecture

```text
test cases
   |
   v
case runner -> prompt/workflow executor -> model client
   |                                      |
   v                                      v
evaluators <------------------------ raw outputs
   |
   v
reporter
```

## Core Abstractions

### Test Case

```json
{
  "id": "rag_refusal_001",
  "input": "What is the refund policy for enterprise plan?",
  "expected_behavior": "refuse_if_no_evidence",
  "tags": ["rag", "refusal", "policy"]
}
```

### Evaluator

An evaluator checks one aspect of the output.

Examples:

- Exact match evaluator.
- JSON schema evaluator.
- Citation evaluator.
- Faithfulness evaluator.
- LLM-as-a-judge evaluator.
- Safety evaluator.

### Report

The report should include:

- Pass rate.
- Failed cases.
- Latency distribution.
- Cost estimate.
- Model and prompt version.
- Diff from previous run.

## Minimal Pseudocode

```python
class EvalHarness:
    def __init__(self, model, evaluators):
        self.model = model
        self.evaluators = evaluators

    def run_case(self, case):
        output = self.model.generate(case["input"])
        scores = [e.evaluate(case, output) for e in self.evaluators]
        return {
            "case_id": case["id"],
            "output": output,
            "scores": scores,
            "passed": all(score.passed for score in scores),
        }

    def run_suite(self, cases):
        return [self.run_case(case) for case in cases]
```

## Evaluation Dimensions

- Correctness.
- Format validity.
- Faithfulness.
- Citation correctness.
- Refusal quality.
- Safety.
- Latency.
- Cost.

## Interview Talking Points

- LLM systems need regression tests because prompts and model versions change.
- Final answer quality should be decomposed into task-specific metrics.
- RAG evaluation should separately test retrieval and generation.
- Agent evaluation should include trajectory and tool-call correctness.
- LLM-as-a-judge should be calibrated against human labels.

## Common Follow-Up Questions

- How do you avoid LLM-as-a-judge bias?
- How do you build a golden dataset?
- How do you evaluate open-ended answers?
- How do you compare two model versions?
- How do you decide a release gate?

## Resume Bullet

Built an LLM evaluation harness that runs versioned test suites across prompts and models, supports deterministic and rubric-based evaluators, and reports quality, latency, cost, and regression metrics for safe LLM application releases.

