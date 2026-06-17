# RAG 论文路线图

本页跟踪帮助理解 Retrieval-Augmented Generation 系统的论文和技术主题。

## 核心问题

- 知识应该如何检索？
- 检索上下文应该如何排序和压缩？
- 如何评估 faithfulness？
- 如何处理 multi-hop questions？
- 如何构建可靠的生产 RAG 系统？

## 阅读顺序

### 1. Retrieval 基础

学习：

- BM25 等 sparse retrieval。
- Dual encoder dense retrieval。
- Hybrid retrieval。
- Query expansion 与 query rewriting。

面试要点：

- Dense retrieval 擅长语义匹配，sparse retrieval 擅长精确词。生产 RAG 往往两者结合。

### 2. RAG 架构

学习：

- Retrieval-augmented generation。
- Fusion-in-decoder 风格架构。
- Retrieve-then-read pipeline。
- Retrieval-augmented pretraining 与 inference-time retrieval。

面试要点：

- RAG 不是单一算法，而是一类连接数据 pipeline、retrieval、ranking、generation 和 evaluation 的系统。

### 3. Reranking 与 Context Selection

学习：

- Cross-encoder rerankers。
- Context compression。
- Lost-in-the-middle。
- Long-context retrieval strategies。

面试要点：

- 检索更多上下文不一定提升答案质量，context precision 很重要。

### 4. Evaluation

学习：

- Retrieval recall。
- Context relevance。
- Faithfulness。
- Citation correctness。
- Refusal quality。

面试要点：

- Retrieval 和 generation 要分开评估。正确最终答案可能掩盖检索失败，好的检索也可能生成坏答案。

## 实现注意事项

- 从 ingestion 到 citation 保留 metadata。
- Evaluation 中加入 unanswerable questions。
- 用 adversarial users 测试 access control。
- 监控文档 freshness。
- 记录 retrieved chunks 方便 debugging。

## 面试题

- 为什么 naive chunking 会失败？
- 没有 gold answers 时如何评估 RAG？
- 什么时候应该使用 reranking？
- 如何设计文档频繁变化的 RAG？
- 如何检测 unsupported claims？

