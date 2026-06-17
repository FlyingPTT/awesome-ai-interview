# Judging LLM-as-a-Judge With MT-Bench And Chatbot Arena

Paper: [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)

## Problem

Open-ended chat assistant quality is hard to evaluate with static benchmarks or exact-match metrics.

## Method

The paper studies strong LLMs as judges, introduces MT-Bench and Chatbot Arena, and analyzes biases such as position, verbosity, and self-enhancement bias.

## Why It Matters

LLM-as-a-judge is now a common evaluation pattern, but it must be calibrated and bias-aware.

## Implementation Notes

- Use rubrics.
- Shuffle output order when comparing.
- Calibrate with human labels.
- Track judge model version.
- Combine with deterministic checks where possible.

## Interview Talking Points

- LLM judges scale semantic evaluation.
- Biases make judge calibration necessary.
- LLM-as-a-judge should not replace all deterministic or human evaluation.

