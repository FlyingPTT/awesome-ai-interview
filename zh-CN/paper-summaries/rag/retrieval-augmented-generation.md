# Retrieval-Augmented Generation For Knowledge-Intensive NLP Tasks

论文：[arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

## 问题

只依赖参数知识的语言模型很难更新知识，也很难追踪答案来源。

## 方法

论文把 seq2seq generator 和通过 dense retrieval 访问的非参数记忆结合起来，并比较了整段输出共享同一批检索段落与每个 token 可使用不同检索段落的变体。

## 为什么重要

这是现代 RAG 的基础论文之一。它把 retrieval 视为提升事实性、具体性和知识更新能力的方式。

## 实现注意事项

- Retrieval quality 会成为 generation quality 的一部分。
- Source provenance 对信任很重要。
- Retrieval 可以在不完整重训模型的情况下更新。
- Evaluation 应包含任务准确性和事实 grounding。

## 面试 Talking Points

- RAG 结合 parametric 和 non-parametric memory。
- RAG 有助于知识新鲜度和 provenance。
- Retrieval 和 generation 应分开评估。

