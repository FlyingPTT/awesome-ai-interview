# LLM Eval Harness Example

This example implements a tiny evaluation harness with no external dependencies.

It demonstrates:

- Versioned test cases.
- Deterministic model wrapper.
- Multiple evaluators.
- Pass/fail report.
- Latency tracking.
- Exact match, regex, citation, latency, and cost checks.
- JSON report export.

## Run

```bash
python3 examples/llm-eval-harness/run_eval.py
```

Write a JSON report:

```bash
python3 examples/llm-eval-harness/run_eval.py --report /tmp/llm-eval-report.json
```

## Files

- `test_cases/cases.json`: sample evaluation cases.
- `model.py`: deterministic mock model.
- `evaluators.py`: keyword, exact match, regex, JSON schema, citation, refusal, latency, and cost evaluators.
- `harness.py`: case runner and report builder.
- `run_eval.py`: runnable CLI demo.

## Interview Talking Points

- LLM apps need regression tests because prompts, models, and data change.
- Evaluation should decompose quality into task-specific checks.
- Deterministic evaluators are cheap and reliable for format and policy checks.
- LLM-as-a-judge can be added for open-ended semantic checks, but should be calibrated.
- Release gates should combine quality, safety, latency, and cost.

## Test

```bash
python3 -m unittest discover examples/llm-eval-harness/tests
```
