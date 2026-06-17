# AI 面试常见坑

本页总结 LLM、RAG、AI Agent 和 AI 工程面试中候选人常见的失误。

## 1. 只背 Transformer 基础

弱回答：

- 能写 attention 公式，但讲不清 inference、serving、evaluation 或产品权衡。

更好回答：

- 先解释机制，再连接到 KV Cache、latency、long context 和 system design。

## 2. 把 RAG 当成“向量数据库”

弱回答：

- 认为 RAG 就是把文档 embedding 后放进 vector database。

更好回答：

- 讨论 parsing、chunking、hybrid retrieval、reranking、prompt construction、citations、refusal、evaluation 和 monitoring。

## 3. 忽略 Evaluation

弱回答：

- 说“可以让用户反馈答案好不好”。

更好回答：

- 定义 offline datasets、golden cases、rubrics、component metrics、human review 和 regression gates。

## 4. 混淆 Fine-Tuning 和 RAG

弱回答：

- 认为 fine-tuning 总是更好，因为它能让模型学领域知识。

更好回答：

- Fine-tuning 改变行为、风格或任务策略。RAG 更适合变化、可审计、带权限控制的知识。

## 5. 认为 Agent 只是 ReAct

弱回答：

- 只解释 thought-action-observation，不讲生产问题。

更好回答：

- 讨论 tool schemas、state、memory、verifier、stop conditions、permissions、audit logs 和 human approval。

## 6. 不理解 Tool Safety

弱回答：

- 让模型自由调用任何工具。

更好回答：

- 使用最小权限、schema validation、dry-run mode、高风险操作审批和日志。

## 7. 滥用 LLM-As-A-Judge

弱回答：

- 所有指标都用 LLM judge，且不校准。

更好回答：

- 能用 deterministic checks 就先用，judge 要用人工标签校准，并追踪 bias。

## 8. 不区分 Retrieval 和 Generation 失败

弱回答：

- RAG 答错时只改 prompt。

更好回答：

- 先看正确证据是否被检索到，再检查 generation、citation 和 refusal behavior。

## 9. 忽略 Latency 和 Cost

弱回答：

- 所有任务都用最强模型。

更好回答：

- 讨论 model routing、caching、batching、prompt length、streaming、quantization 和 success-cost metrics。

## 10. 项目没有指标

弱回答：

- “我做了一个 RAG chatbot。”

更好回答：

- “我构建了一个 RAG 系统，包含 hybrid retrieval、reranking、citation tracking，并用 recall、faithfulness、latency 和 cost 评估。”

## 11. 不知道 Failure Modes

弱回答：

- 只讲 happy path。

更好回答：

- 讨论 hallucination、stale documents、permission bugs、prompt injection、tool errors、infinite loops 和 evaluation leakage。

## 12. 把 Demo 当 Production System

弱回答：

- Demo 能跑，但讲不清如何上线。

更好回答：

- 解释 evaluation、monitoring、access control、rollback、human review 和 cost budgets。

## 快速自查

- 你能解释机制吗？
- 你能解释 tradeoffs 吗？
- 你能设计 evaluation 吗？
- 你能 debug failures 吗？
- 你能讨论 production constraints 吗？
- 你能把这个主题变成简历项目吗？

