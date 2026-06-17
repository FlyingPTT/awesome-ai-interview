# RAG 诊断 Skills

## RAG 失败诊断 Skill

目的：诊断 RAG 答案为什么错误。

工作流：

1. 检查答案是否被 retrieved context 支撑。
2. 如果没有支撑，检查 retrieval。
3. 如果有支撑但仍错误，检查 generation。
4. 如果检索不稳定，检查 indexing 和 metadata。
5. 如果应该拒答，检查 refusal policy。

诊断表：

| 现象 | 可能原因 | 修复 |
| --- | --- | --- |
| 相关文档缺失 | 切分差、query 弱、filter 错 | 改进切分、query rewrite、hybrid retrieval |
| 检索到了相关文档但被忽略 | Prompt 问题、上下文顺序问题 | 改进 prompt 和 context formatting |
| 答案引用错误来源 | Citation mapping bug | 在全 pipeline 追踪 source ids |
| 响应慢 | 候选太多、rerank 太贵 | Cache、减少候选数、优化模型 |

