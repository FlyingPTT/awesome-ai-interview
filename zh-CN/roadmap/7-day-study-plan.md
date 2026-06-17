# 7 天 AI 面试学习路线

这份计划面向希望用一周集中准备 LLM、RAG 和 AI Agent 面试的候选人。

## Day 1：Transformer 与 LLM 基础

阅读：

- [LLM 工程师路线图](llm-engineer.md)
- [LLM 高频基础面试题](../interviews/llm-basic.md)
- [100 道 LLM 面试题](../interviews/100-llm-interview-questions.md) 的 1-20 题

交付物：

- 不看笔记解释 attention、position encoding、decoder-only architecture 和 next-token prediction。

## Day 2：Fine-tuning、Alignment 与 Inference

阅读：

- [100 道 LLM 面试题](../interviews/100-llm-interview-questions.md) 的 21-35 题

练习：

- 比较 SFT、RLHF、DPO、LoRA、QLoRA、RAG 和 distillation。
- 解释 KV Cache、prefill/decode、batching、quantization 和 speculative decoding。

交付物：

- 写一个两分钟回答：如何降低 LLM serving 的成本和延迟？

## Day 3：RAG 工程

阅读：

- [RAG 工程师路线图](rag-engineer.md)
- [RAG 面试笔记](../interviews/rag.md)
- [50 道 RAG 面试题](../interviews/50-rag-interview-questions.md)

练习：

- 设计企业知识助手。
- Debug 一个 hallucinated RAG answer。

交付物：

- 画出 RAG pipeline，并分别列出 retrieval 和 generation 指标。

## Day 4：AI Agent

阅读：

- [AI Agent 工程师路线图](ai-agent-engineer.md)
- [AI Agent 面试笔记](../interviews/agent.md)
- [50 道 AI Agent 面试题](../interviews/50-agent-interview-questions.md)

练习：

- 设计 Coding Agent。
- 解释 tool calling、memory、planning、verifier 和 guardrails。

交付物：

- 写一份能运行 shell command 的 Agent 安全执行策略。

## Day 5：Evaluation 与 Safety

阅读：

- [LLM 评估笔记](../interviews/eval.md)
- [100 道 LLM 面试题](../interviews/100-llm-interview-questions.md) 的 66-75 题

练习：

- 为 prompt 构建 regression test plan。
- 设计 LLM-as-a-judge rubrics。
- 解释 prompt injection 和 refusal quality。

交付物：

- 创建一个包含 metrics、datasets 和 thresholds 的 evaluation table。

## Day 6：System Design

阅读：

- [LLM 系统设计笔记](../interviews/system-design.md)
- [100 道 LLM 面试题](../interviews/100-llm-interview-questions.md) 的 76-85 题

练习：

- 设计 AI 客服助手。
- 设计 LLM evaluation platform。
- 讨论成本、延迟、监控和 human review。

交付物：

- 准备一份完整 system design 回答：包含架构、tradeoffs、evaluation 和 failure modes。

## Day 7：简历项目与模拟面试

阅读：

- [可写进简历的 AI 项目](../projects/README.md)
- [Agent Skills Catalog](../skills/agent-skills-catalog.md)
- [简历项目模板](../templates/resume-project.md)

练习：

- 选择一个项目。
- 写 resume bullets。
- 用题库做 45 分钟 mock interview。

交付物：

- 一个打磨好的简历项目 pitch，以及后续改进计划。

