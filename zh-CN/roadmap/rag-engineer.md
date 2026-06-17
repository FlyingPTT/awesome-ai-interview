# RAG 工程师路线图

RAG 工程的目标是让 LLM 应用具备可检索、可溯源、可审计、可维护的知识能力。

## Pipeline

1. 接入文档。
2. 解析并规范化内容。
3. 切分内容。
4. 生成 embeddings。
5. 建立向量索引和元数据索引。
6. 检索候选内容。
7. 重排结果。
8. 生成 grounded answers。
9. 评估质量。
10. 监控生产行为。

## 关键设计选择

### Chunking

- 固定长度切分。
- 语义切分。
- 按章节结构切分。
- Parent-child chunks。
- Sliding windows。

### Retrieval

- Dense retrieval。
- BM25。
- Hybrid retrieval。
- Metadata filtering。
- Query rewriting。
- Multi-hop retrieval。

### Generation

- Citation-aware prompting。
- 证据不足时拒答。
- 结构化答案。
- Context compression。

### Evaluation

- Retrieval recall。
- Answer faithfulness。
- Context precision。
- Citation correctness。
- Latency 与 cost。

## 面试题

- 为什么 naive chunking 经常伤害 RAG 质量？
- 如何 debug RAG 中的 hallucination？
- 如何选择 embedding 模型？
- 什么时候应该使用 reranking？
- 如何构建文档频繁变化的 RAG 系统？

