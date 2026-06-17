# 50 道 RAG 面试题

本页整理 50 道 Retrieval-Augmented Generation 高频面试题，重点覆盖工程实践、debugging、评估和系统设计。

## 基础

### 1. RAG 是什么？

要点：

- RAG 将外部检索与 LLM 生成结合。
- 适合知识量大、私有、频繁变化或必须引用来源的场景。
- 典型 pipeline 包括 ingestion、parsing、chunking、embedding、retrieval、reranking、generation 和 evaluation。

追问：什么时候 RAG 不如 long-context prompt？

### 2. 为什么用 RAG，而不是 fine-tuning？

要点：

- RAG 更新知识不需要重新训练。
- RAG 可以引用来源。
- RAG 可以执行文档级权限控制。
- Fine-tuning 更适合行为、风格和任务策略。

追问：什么时候应该结合 RAG 和 fine-tuning？

### 3. RAG 系统有哪些主要组件？

要点：

- Data connectors。
- Parser and normalizer。
- Chunker。
- Embedding model。
- Vector and metadata index。
- Retriever。
- Reranker。
- Prompt builder。
- Generator。
- Evaluator and monitor。

### 4. Grounded generation 是什么？

要点：

- 答案必须被检索证据支撑。
- 模型应引用来源，并在证据不足时拒答。
- Grounding 质量依赖 retrieval、prompt design 和 evaluation。

### 5. RAG 和搜索有什么区别？

要点：

- 搜索返回文档或段落。
- RAG 用检索证据生成答案。
- RAG 需要处理 citation、synthesis、refusal 和 hallucination risk。

## Ingestion 与 Chunking

### 6. 为什么文档解析重要？

要点：

- 解析差会污染下游检索。
- PDF、表格、图、页眉页脚和代码块需要特殊处理。
- 应保留标题、章节、页码、权限和版本等 metadata。

### 7. Chunking 为什么难？

要点：

- 小 chunk 提升 precision，但可能丢上下文。
- 大 chunk 保留上下文，但稀释相关性。
- 结构化切分通常优于固定长度切分。

### 8. Parent-child chunking 是什么？

要点：

- 检索小 child chunks 提升 precision。
- 给 generation 提供更大的 parent chunks 保留上下文。
- 适合局部证据依赖上下文段落或章节的场景。

### 9. 如何切分表格？

要点：

- 保留表头和行列关系。
- 包含表格标题和附近解释文本。
- 可使用 table-aware parsing，或把行转换成结构化 records。

### 10. 如何处理代码文档？

要点：

- 按 symbols、functions、classes 或 files 切分。
- 保留 imports、signatures、comments 和 dependencies。
- 检索可能需要 lexical 和 semantic search 结合。

### 11. 如何处理重复文档？

要点：

- 去除 exact 和 near-duplicate 内容。
- 保留 canonical source ids。
- 避免返回多份重复证据。

### 12. 如何处理文档更新？

要点：

- 追踪文档版本。
- 只重新索引变更 chunks。
- 传播删除。
- 监控 freshness lag。

## Retrieval

### 13. Dense retrieval 是什么？

要点：

- 用 embedding similarity 检索语义相关 chunks。
- 擅长 paraphrases 和概念匹配。
- 对精确标识符、罕见词和数字较弱。

### 14. Sparse retrieval 是什么？

要点：

- 使用 BM25 等 lexical matching。
- 擅长精确词、名称、ID 和错误信息。
- 对语义改写较弱。

### 15. Hybrid retrieval 是什么？

要点：

- 结合 dense 和 sparse retrieval。
- 提升鲁棒性。
- 需要 score normalization 或 fusion strategy。

### 16. Metadata filtering 是什么？

要点：

- 按来源、用户权限、日期、产品、租户或文档类型过滤。
- 必须在 generation 前执行。
- filter bug 可能导致数据泄露或证据缺失。

### 17. Query rewriting 是什么？

要点：

- 把用户问题改写成更适合检索的 query。
- 帮助处理模糊、多轮或对话式问题。
- 必须保留用户意图。

### 18. Query expansion 是什么？

要点：

- 添加同义词、缩写、相关词或领域上下文。
- 可提升 recall。
- 过度扩展会降低 precision。

### 19. Multi-query retrieval 是什么？

要点：

- 为一个用户问题生成多个检索 query。
- 提升覆盖率。
- 需要 deduplication 和 reranking。

### 20. Multi-hop retrieval 是什么？

要点：

- 分多步检索证据。
- 适合需要组合多个事实的答案。
- 需要状态追踪和停止条件。

## Reranking 与 Context Building

### 21. 为什么用 reranking？

要点：

- 第一阶段检索优化速度。
- Reranking 优化最终相关性。
- 提高 context precision，但增加延迟。

### 22. Cross-encoder reranker 是什么？

要点：

- 联合编码 query-document pair 进行打分。
- 通常比 embedding similarity 更准确。
- 成本更高，因此只用于小候选集。

### 23. 如何选择 top-k？

要点：

- 大 k 提升 recall，但增加噪音和成本。
- 小 k 提升 precision，但可能漏证据。
- 用 retrieval 和 answer-level evaluation 调参。

### 24. 如何排序 retrieved context？

要点：

- 可按相关性、文档结构、时间或依赖顺序。
- 关键信息放在开头或结尾可能更容易被利用。
- 长上下文系统会遇到 lost-in-the-middle。

### 25. Context compression 是什么？

要点：

- 在 generation 前压缩检索内容。
- 适合长文档或上下文窗口有限场景。
- 风险是压缩掉关键证据。

## Generation 与 Refusal

### 26. RAG prompt 如何设计？

要点：

- 区分 system instructions、user question 和 retrieved evidence。
- 要求 citation。
- 告诉模型证据不足时拒答。
- 保留 source ids。

### 27. 如何让 citation 可靠？

要点：

- source ids 贯穿 pipeline。
- 让模型只引用提供的 source ids。
- generation 后验证 citation。
- citation 应能回到具体 chunk 或 page。

### 28. RAG 如何处理证据不足？

要点：

- 拒答或请求澄清。
- 说明缺少什么。
- 避免猜测。
- 可建议下一步查哪里。

### 29. 如何减少 hallucination？

要点：

- 提升 retrieval recall 和 precision。
- 增加 citation 和 refusal 要求。
- 用证据验证答案。
- 评估 faithfulness。

### 30. 如何处理冲突来源？

要点：

- 优先权威或更新来源。
- 暴露分歧。
- 引用双方。
- 使用 version、owner、date 等 metadata。

## Evaluation

### 31. 如何评估 retrieval？

要点：

- Recall@k。
- Precision@k。
- MRR。
- nDCG。
- Gold evidence coverage。
- Query-level failure analysis。

### 32. 如何评估 generation？

要点：

- Answer correctness。
- Faithfulness。
- Citation correctness。
- Refusal quality。
- Completeness。
- User usefulness。

### 33. Faithfulness 是什么？

要点：

- 答案是否被 retrieved context 支撑。
- 不同于一般事实正确性。
- 可通过人工、规则或 LLM judge 检查。

### 34. Context precision 是什么？

要点：

- 衡量检索上下文中真正相关内容比例。
- 低 precision 增加 hallucination risk 和 token cost。
- Reranking 和 filtering 可改善。

### 35. 如何构建 RAG evaluation set？

要点：

- 包含真实用户问题。
- 尽可能标注 gold evidence。
- 包含 unanswerable questions。
- 覆盖 edge cases、permissions 和 stale documents。

### 36. 如何在 RAG 中使用 LLM-as-a-judge？

要点：

- 用 rubric 评估 faithfulness、relevance 和 answer quality。
- 用人工标签校准。
- 不要给 judge 模型原模型没有的信息。

### 37. 常见 evaluation 坑有哪些？

要点：

- 只评估最终答案。
- 忽略 retrieval failure。
- 没有 unanswerable questions。
- Judge bias。
- Test data leakage。

## Production 与 Reliability

### 38. 如何监控生产 RAG？

要点：

- Query distribution。
- Retrieval hit rate。
- Top sources。
- Latency and cost。
- Refusal rate。
- User feedback。
- Citation errors。

### 39. 如何 debug 错误答案？

要点：

- 复现 query。
- 检查 parsed documents。
- 检查 retrieved chunks。
- 检查 reranker output。
- 检查 final prompt。
- 检查 citation 和 refusal behavior。

### 40. 如何处理权限？

要点：

- indexing 和 retrieval 时执行 ACL。
- 避免日志记录 restricted content。
- 测试 cross-tenant leakage。
- 权限 metadata 端到端保留。

### 41. 如何降低延迟？

要点：

- 缓存 embeddings 和 retrieval results。
- 限制 candidate count。
- 使用更快 rerankers。
- 并行 retrieval。
- Stream generation。
- 简单 query 走便宜路径。

### 42. 如何降低成本？

要点：

- 缩短 context。
- 使用小模型。
- 缓存常见 query。
- 调整 top-k。
- 压缩 context。
- 监控 cost per successful answer。

### 43. 如何支持 multi-turn RAG？

要点：

- 用 conversation state 改写 follow-up question。
- 不要盲目检索整个历史。
- 追踪用户意图和 referenced entities。
- 保留权限约束。

### 44. 如何处理 multilingual RAG？

要点：

- 使用 multilingual embeddings 或翻译 query/documents。
- 按语言评估。
- citation 保留原始来源语言。
- 注意 cross-lingual retrieval gaps。

### 45. 如何处理图片或扫描 PDF？

要点：

- OCR 或 multimodal parsing。
- 保留 layout 和 page coordinates。
- 评估表格、图和小字体。
- 必要时存储 visual references。

## 系统设计场景

### 46. 设计法律文档 RAG 系统。

要点：

- 强 citation。
- Versioning。
- Jurisdiction metadata。
- Access control。
- 证据不足时拒答。
- 高风险答案人工 review。

### 47. 设计客服 RAG 系统。

要点：

- Product/version metadata。
- Ticket context。
- Escalation policy。
- Tone control。
- 从 resolved tickets 建立 feedback loop。

### 48. 设计代码库 Q&A RAG 系统。

要点：

- Symbol-aware chunking。
- Hybrid retrieval。
- Repository structure metadata。
- 答案链接到文件和行号。
- 避免 stale code references。

### 49. 设计论文 RAG 系统。

要点：

- Section-aware parsing。
- Citation graph。
- Method and experiment extraction。
- 跨论文比较。
- 报告 uncertainty 和 limitations。

### 50. 如何判断 RAG 系统 production-ready？

要点：

- 清晰 evaluation set 和 passing thresholds。
- Permission tests。
- Monitoring and alerts。
- Freshness pipeline。
- Citation validation。
- Cost and latency budgets。
- Human escalation path。

