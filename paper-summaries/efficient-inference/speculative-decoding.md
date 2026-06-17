# Speculative Decoding

Paper: [arXiv:2211.17192](https://arxiv.org/abs/2211.17192)

## Problem

Autoregressive decoding is slow because tokens are generated sequentially.

## Method

A smaller draft model proposes multiple tokens. The larger target model verifies them in parallel while preserving the target distribution.

## Why It Matters

Speculative decoding can reduce latency without changing final model outputs, when draft acceptance is high.

## Implementation Notes

- Draft model quality controls speedup.
- Acceptance rate is a key metric.
- Verification must preserve output distribution.
- Benefits depend on workload and hardware.

## Interview Talking Points

- Speculative decoding uses a cheap model to accelerate a strong model.
- It is useful when many drafted tokens are accepted.
- It trades extra draft computation for fewer target-model decoding steps.

