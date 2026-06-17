# Toolformer

Paper: [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

## Problem

Language models can solve many tasks but struggle with simple external operations such as arithmetic, factual lookup, translation, or calendar access.

## Method

Toolformer teaches language models to call APIs using a small number of demonstrations and self-supervised data generation. The model learns when to call a tool, what arguments to use, and how to incorporate results.

## Why It Matters

It frames tool use as a learnable behavior rather than only a hand-written orchestration pattern.

## Implementation Notes

- Tool call data quality matters.
- Tool APIs should be narrow and well described.
- Model-generated tool calls need validation.
- Tool use can improve capability without increasing model size.

## Interview Talking Points

- Toolformer learns tool use from self-supervised signals.
- Tool use helps with tasks where external systems are stronger than the model.
- Schema design and validation are still required in production.

