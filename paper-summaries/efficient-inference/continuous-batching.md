# Continuous Batching

Reference: vLLM and modern LLM serving systems.

## Problem

Static batching wastes GPU capacity when requests have different prompt lengths and generation lengths.

## Method

Continuous batching dynamically schedules new requests while existing requests are decoding.

## Why It Matters

It improves serving throughput and GPU utilization while supporting interactive workloads.

## Implementation Notes

- Decode scheduling is often memory-bandwidth bound.
- Request queues need fairness policies.
- Batching can improve throughput but hurt tail latency.
- Metrics should include time to first token and tokens per second.

## Interview Talking Points

- Continuous batching is critical for production LLM serving.
- It is a scheduling problem, not a model architecture change.
- Throughput optimization must be balanced against user latency.

