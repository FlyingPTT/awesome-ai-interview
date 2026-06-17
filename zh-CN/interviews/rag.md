# RAG 面试笔记

## 系统设计模板

面试中设计 RAG 系统时，建议覆盖：

1. 使用场景和约束。
2. 数据来源和新鲜度。
3. 解析与切分。
4. Embedding 与索引。
5. 检索策略。
6. Reranking。
7. Prompt 构造。
8. 引用与拒答。
9. 评估。
10. 监控与迭代。

## 高频问题

### 如何 debug RAG 答案质量差？

先区分是 retrieval failure 还是 generation failure。

- 如果正确证据没有被检索到，检查解析、切分、embedding、filter、query rewriting 和 reranking。
- 如果正确证据已经被检索到但答案仍然错误，检查 prompt、上下文排序、引用要求和模型行为。
- 如果答案不稳定，加入回归测试，并分别追踪 retrieval 和 generation 指标。

### Chunking 为什么难？

Chunking 需要平衡 recall 和 precision。chunk 太小会丢上下文，chunk 太大会稀释相关证据并浪费上下文窗口。好的 chunking 通常需要利用标题、表格、段落和元数据等文档结构。

### 为什么使用 reranking？

Embedding retrieval 适合快速召回候选，不一定适合最终排序。Reranker 可以在较小候选集上使用更贵但更准确的相关性模型，提高 evidence precision，减少无关上下文。

### 如何评估 RAG？

分别评估检索和生成。

- 检索：recall、precision、MRR、nDCG、context relevance。
- 生成：faithfulness、answer correctness、citation accuracy、refusal quality。
- 系统：latency、cost、freshness、user satisfaction。

