# PagedAttention

Paper: Efficient Memory Management for Large Language Model Serving with PagedAttention

Reference: [vLLM project](https://github.com/vllm-project/vllm)

## Problem

KV cache memory in LLM serving can be large and fragmented, limiting throughput.

## Method

PagedAttention stores KV cache in blocks inspired by virtual memory paging. This allows more flexible memory management and sharing.

## Why It Matters

It is one of the core ideas behind vLLM and modern high-throughput LLM serving systems.

## Implementation Notes

- KV cache is a major serving bottleneck.
- Block-based memory management reduces waste.
- Serving throughput depends on scheduling and memory layout.
- Long context increases KV cache pressure.

## Interview Talking Points

- PagedAttention applies OS-style paging to KV cache.
- Serving optimization is a systems problem.
- Throughput and latency must be measured separately.

