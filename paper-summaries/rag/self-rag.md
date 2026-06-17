# Self-RAG

Paper: [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)

## Problem

Naive RAG retrieves a fixed number of passages even when retrieval is unnecessary or retrieved evidence is weak.

## Method

Self-RAG trains a model to retrieve, generate, and critique using reflection tokens. The model can decide when retrieval is needed and reflect on retrieved evidence and its own generations.

## Why It Matters

It introduces a more adaptive view of RAG: retrieval should be controlled, evidence should be assessed, and generation should be critique-aware.

## Implementation Notes

- Retrieval should not always be unconditional.
- Critique signals can improve citation and factuality.
- Production systems can approximate this with retrieval gating and answer verification.

## Interview Talking Points

- Fixed top-k retrieval can hurt quality.
- Adaptive retrieval and self-critique are important RAG design ideas.
- Reflection can be implemented with model tokens, verifier models, or workflow logic.

