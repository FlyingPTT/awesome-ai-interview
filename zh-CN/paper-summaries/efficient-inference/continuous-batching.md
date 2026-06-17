# Continuous Batching

参考：vLLM 和现代 LLM serving systems。

## 问题

当请求 prompt 长度和 generation 长度不同，static batching 会浪费 GPU 能力。

## 方法

Continuous batching 在已有请求 decoding 的同时动态调度新请求。

## 为什么重要

它能在支持交互式 workload 的同时，提高 serving throughput 和 GPU utilization。

## 实现注意事项

- Decode scheduling 经常 memory-bandwidth bound。
- Request queues 需要 fairness policies。
- Batching 可提升 throughput，但可能伤害 tail latency。
- Metrics 应包含 time to first token 和 tokens per second。

## 面试 Talking Points

- Continuous batching 对生产 LLM serving 很关键。
- 它是 scheduling 问题，不是模型架构变化。
- Throughput optimization 必须与用户 latency 平衡。

