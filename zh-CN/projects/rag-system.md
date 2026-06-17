# 项目：生产级 RAG 系统

## 目标

构建一个能基于私有文档集合回答问题的 RAG 系统，要求提供引用并支持证据不足时拒答。

## 架构

- 文档接入。
- PDF 与 Markdown 解析。
- 按章节结构切分。
- Embedding 与向量索引。
- Hybrid retrieval。
- Reranking。
- Grounded answer generation。
- Evaluation dashboard。

## 技术亮点

- Parent-child chunking 提升上下文质量。
- Hybrid retrieval 提升鲁棒性。
- Reranking 提升 evidence precision。
- 从源文档到答案的 citation tracking。
- 针对 prompt 和 retrieval 变化的 regression set。

## 简历 Bullet

构建生产级私有文档 RAG 系统，实现 hybrid retrieval、reranking、citation tracking，并基于 answer faithfulness、retrieval recall、latency 和 cost 建立评估指标。

## 面试 talking points

- 为什么 chunking strategy 重要。
- 为什么 retrieval 和 generation 应分开评估。
- 如何处理过期文档。
- 如何降低 hallucination。

