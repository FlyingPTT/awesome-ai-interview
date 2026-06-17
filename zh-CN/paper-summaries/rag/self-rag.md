# Self-RAG

论文：[arXiv:2310.11511](https://arxiv.org/abs/2310.11511)

## 问题

朴素 RAG 会固定检索若干段落，即使不需要检索，或检索证据质量很弱。

## 方法

Self-RAG 使用 reflection tokens 训练模型进行 retrieve、generate 和 critique。模型可以决定何时需要检索，并反思检索证据和自身生成。

## 为什么重要

它提出了更自适应的 RAG 视角：检索应该受控，证据应该被评估，生成应该能被 critique。

## 实现注意事项

- Retrieval 不应该总是无条件触发。
- Critique signals 可以提升 citation 和 factuality。
- 生产系统可以用 retrieval gating 和 answer verification 近似实现。

## 面试 Talking Points

- 固定 top-k retrieval 可能伤害质量。
- Adaptive retrieval 和 self-critique 是重要 RAG 设计思想。
- Reflection 可以通过模型 token、verifier model 或 workflow logic 实现。

