# Multilingual Retrieval-Augmented Generation

论文：[arXiv:2504.03616](https://arxiv.org/abs/2504.03616)

## 问题

RAG 在英语场景中效果较好，但 multilingual retrieval 会引入 coverage、translation 和 cross-lingual consistency 问题。

## 方法

论文研究了多种 multilingual RAG 策略，包括 question translation、直接 multilingual retrieval，以及在 generation 前把 retrieved documents 翻译到同一语言。

## 为什么重要

许多生产 RAG 系统服务多语言用户。Retrieval、citation 和 grounding 必须按语言评估，不能假设自然迁移。

## 实现注意事项

- 按语言评估 retrieval。
- Citation 应保留原始来源语言。
- 翻译可能改善 generation，但也可能引入错误。
- Cross-lingual retrieval 需要谨慎选择 embedding 和 indexing。

## 面试 Talking Points

- Multilingual RAG 不只是 English RAG 加翻译。
- Cross-lingual retrieval 可能产生不一致证据。
- 必须做 language-specific evaluation。

