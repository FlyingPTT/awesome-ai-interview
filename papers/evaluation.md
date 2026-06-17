# LLM Evaluation Paper Map

This page tracks concepts and research directions for evaluating LLMs, RAG systems, and agents.

## Core Questions

- How do we evaluate open-ended answers?
- How do we evaluate faithfulness?
- How do we detect regressions after prompt or model changes?
- How reliable is LLM-as-a-judge?
- How do we evaluate agents beyond final answer quality?

## Evaluation Levels

### 1. Model-Level Evaluation

Focus:

- General benchmarks.
- Reasoning.
- Coding.
- Safety.
- Multilingual capability.

Interview takeaway:

- Benchmarks are useful but can be contaminated or misaligned with product tasks.

### 2. Application-Level Evaluation

Focus:

- Task-specific datasets.
- Rubrics.
- Human review.
- Regression tests.
- Product metrics.

Interview takeaway:

- A production LLM app needs its own evaluation set, not only public benchmark scores.

### 3. RAG Evaluation

Focus:

- Retrieval recall.
- Context precision.
- Answer faithfulness.
- Citation correctness.
- Refusal quality.

Interview takeaway:

- RAG evaluation must separate retrieval quality from generation quality.

### 4. Agent Evaluation

Focus:

- Task success.
- Tool-call accuracy.
- Trajectory quality.
- Recovery from failure.
- Safety violations.
- Cost and latency.

Interview takeaway:

- Final answer quality is not enough. Unsafe or wasteful trajectories matter.

## LLM-As-A-Judge Notes

Strengths:

- Scales semantic evaluation.
- Supports rubric-based scoring.
- Useful for comparing outputs.

Risks:

- Position bias.
- Verbosity bias.
- Model-family bias.
- Prompt sensitivity.
- Weak calibration.

Mitigations:

- Calibrate against human labels.
- Use pairwise comparisons when appropriate.
- Shuffle output order.
- Keep rubrics specific.
- Track judge version.

## Interview Questions

- How do you evaluate open-ended answers?
- How do you build a golden set?
- How do you avoid LLM-as-a-judge bias?
- How do you evaluate refusal quality?
- How do you design release gates for LLM apps?

