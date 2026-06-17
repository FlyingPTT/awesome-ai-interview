# PagedAttention

论文：Efficient Memory Management for Large Language Model Serving with PagedAttention

参考：[vLLM project](https://github.com/vllm-project/vllm)

## 问题

LLM serving 中 KV Cache 内存很大且容易碎片化，从而限制吞吐。

## 方法

PagedAttention 借鉴 virtual memory paging，把 KV Cache 存储在 blocks 中，从而实现更灵活的内存管理和共享。

## 为什么重要

这是 vLLM 和现代高吞吐 LLM serving 系统的核心思想之一。

## 实现注意事项

- KV Cache 是主要 serving bottleneck。
- Block-based memory management 可以减少浪费。
- Serving throughput 取决于 scheduling 和 memory layout。
- Long context 会增加 KV Cache 压力。

## 面试 Talking Points

- PagedAttention 把 OS-style paging 应用到 KV Cache。
- Serving optimization 是系统问题。
- Throughput 和 latency 必须分开衡量。

