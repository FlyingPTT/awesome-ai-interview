# LLM 系统设计面试笔记

## 回答框架

遇到 LLM 系统设计题，可以按以下结构回答：

1. 澄清使用场景。
2. 定义用户和约束。
3. 画出高层架构。
4. 说明数据流。
5. 讨论模型和检索选择。
6. 讨论评估。
7. 讨论延迟、成本和可靠性。
8. 讨论安全和监控。

## 示例题

设计一个企业知识助手。

## 强回答大纲

### 需求

- 员工可以基于内部文档提问。
- 答案必须包含引用。
- 证据不足时应该拒答。
- 文档会频繁更新。
- 必须遵守访问控制。

### 架构

- Document connector。
- Parser。
- Chunker。
- Embedding service。
- Vector database。
- Metadata index。
- Retriever。
- Reranker。
- LLM answer generator。
- Evaluation and monitoring service。

### 关键权衡

- Chunk size 会影响检索精度和上下文完整性。
- Hybrid retrieval 通常比 dense retrieval 更稳健。
- Reranking 提升质量但增加延迟。
- Citation tracking 需要 source id 贯穿整个 pipeline。
- Access control 应在检索前和生成前都执行。

### 评估

- Retrieval recall。
- Answer faithfulness。
- Citation correctness。
- Refusal accuracy。
- Latency。
- Cost per query。

