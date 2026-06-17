# Reflexion

Paper: [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)

## Problem

Agents often fail repeatedly because they do not learn effectively from prior attempts without expensive fine-tuning.

## Method

Reflexion uses verbal feedback and episodic memory. The agent reflects on feedback from the environment or itself, stores lessons, and uses them in later attempts.

## Why It Matters

It shows how agents can improve across attempts through language-level memory rather than weight updates.

## Implementation Notes

- Reflection should be bounded to avoid loops.
- Memory must be curated or it can preserve bad lessons.
- Feedback can come from tests, tools, humans, or verifier models.

## Interview Talking Points

- Reflexion is a memory-and-feedback pattern for agents.
- It is useful for coding and sequential decision tasks.
- Reflection adds cost and needs evaluation.

