# Retrieval-Augmented Generation For Knowledge-Intensive NLP Tasks

Paper: [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

## Problem

Parametric-only language models store knowledge in weights, but updating that knowledge and tracing provenance are difficult.

## Method

The paper combines a seq2seq generator with non-parametric memory accessed through dense retrieval. It compares variants that condition on the same retrieved passages across the output versus variants that can use different passages per generated token.

## Why It Matters

This paper is one of the foundational references for modern RAG. It frames retrieval as a way to improve factuality, specificity, and knowledge updating.

## Implementation Notes

- Retrieval quality becomes part of generation quality.
- Source provenance matters for trust.
- Retrieval can be changed without fully retraining the model.
- Evaluation should include both task accuracy and factual grounding.

## Interview Talking Points

- RAG combines parametric and non-parametric memory.
- RAG helps knowledge freshness and provenance.
- Retrieval and generation should be evaluated separately.

