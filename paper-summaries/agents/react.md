# ReAct

Paper: [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

## Problem

Reasoning and acting were often studied separately: models could reason in text or act in environments, but not combine both cleanly.

## Method

ReAct interleaves reasoning traces with actions. The model thinks, calls tools or takes actions, observes results, and continues.

## Why It Matters

ReAct became a core mental model for tool-using agents. It makes trajectories more interpretable and supports external information gathering.

## Implementation Notes

- Tool observations should be structured.
- Reasoning/action loops need step budgets.
- Tool outputs can introduce prompt injection risk.
- ReAct is useful but not sufficient for production safety.

## Interview Talking Points

- ReAct combines reasoning and acting.
- It improves interpretability through visible trajectories.
- Production agents need guardrails beyond ReAct prompting.

