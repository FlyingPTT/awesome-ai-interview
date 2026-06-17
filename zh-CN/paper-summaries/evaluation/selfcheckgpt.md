# SelfCheckGPT

论文：[arXiv:2303.08896](https://arxiv.org/abs/2303.08896)

## 问题

当无法访问 token probabilities 或模型内部状态时，black-box hallucination detection 很难。

## 方法

SelfCheckGPT 多次采样回答，并检查不同 generations 之间的一致性。不一致的 claims 更可能是 hallucination。

## 为什么重要

它提供了一种实用的 black-box hallucination detection 方法，适用于只暴露文本生成接口的模型。

## 实现注意事项

- 多次采样会增加成本。
- 一致性不等于真实性。
- 最适合可比较事实 claims 的任务。
- 可与 retrieval evidence checks 结合。

## 面试 Talking Points

- Hallucination 可通过 self-consistency 估计。
- Black-box evaluation 有 tradeoffs。
- Grounding 仍然需要 retrieval evidence。

