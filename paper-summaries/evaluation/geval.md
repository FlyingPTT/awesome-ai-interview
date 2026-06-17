# G-Eval

Paper: [arXiv:2303.16634](https://arxiv.org/abs/2303.16634)

## Problem

Traditional NLG metrics often correlate poorly with human judgment for open-ended generation.

## Method

G-Eval uses LLMs with task-specific rubrics and chain-of-thought-style evaluation steps to score generated outputs.

## Why It Matters

It popularized rubric-driven LLM evaluation for summarization and open-ended generation quality.

## Implementation Notes

- Rubric design matters.
- Judge prompts should be versioned.
- Scores should be calibrated against human labels.
- Evaluation prompts can themselves regress.

## Interview Talking Points

- LLM evaluation should be rubric-based.
- Judge prompts are part of the evaluation system.
- Correlation with human ratings must be measured.

