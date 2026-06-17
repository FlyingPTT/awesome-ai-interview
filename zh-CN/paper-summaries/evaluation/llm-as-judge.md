# Judging LLM-as-a-Judge With MT-Bench And Chatbot Arena

论文：[arXiv:2306.05685](https://arxiv.org/abs/2306.05685)

## 问题

开放式 chat assistant 质量很难用静态 benchmark 或 exact-match metrics 评估。

## 方法

论文研究强 LLM 作为 judge，提出 MT-Bench 和 Chatbot Arena，并分析 position、verbosity、self-enhancement 等 bias。

## 为什么重要

LLM-as-a-judge 已成为常见 evaluation pattern，但必须校准并关注 bias。

## 实现注意事项

- 使用 rubrics。
- 比较输出时打乱顺序。
- 用人工标签校准。
- 追踪 judge model version。
- 尽可能结合 deterministic checks。

## 面试 Talking Points

- LLM judge 可以扩展 semantic evaluation。
- Bias 让 judge calibration 必不可少。
- LLM-as-a-judge 不应替代所有 deterministic 或 human evaluation。

