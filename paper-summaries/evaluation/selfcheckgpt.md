# SelfCheckGPT

Paper: [arXiv:2303.08896](https://arxiv.org/abs/2303.08896)

## Problem

Black-box hallucination detection is difficult when token probabilities or model internals are unavailable.

## Method

SelfCheckGPT samples multiple responses and checks consistency across generations. Inconsistent claims are more likely to be hallucinated.

## Why It Matters

It gives a practical black-box approach for hallucination detection when the model provider exposes only text generation.

## Implementation Notes

- Sampling multiple outputs increases cost.
- Consistency does not guarantee truth.
- Works best when factual claims can be compared.
- Can be combined with retrieval-based evidence checks.

## Interview Talking Points

- Hallucination can be estimated through self-consistency.
- Black-box evaluation has tradeoffs.
- Retrieval evidence is still important for grounding.

