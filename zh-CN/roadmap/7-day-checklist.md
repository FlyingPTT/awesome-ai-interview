# 7 天 AI 面试打卡清单

用这份 checklist 做一周冲刺，准备 LLM、RAG 和 AI Agent 面试。

## Day 1：LLM 基础

- [ ] 从 query、key、value 解释 self-attention。
- [ ] 解释为什么 Transformer 需要位置信息。
- [ ] 比较 encoder-only、decoder-only 和 encoder-decoder 模型。
- [ ] 解释 causal masking。
- [ ] 回答 [100 道 LLM 面试题](../interviews/100-llm-interview-questions.md) 的 1-20 题。

交付物：

- [ ] 录音或写下一个两分钟 Transformer attention 解释。

## Day 2：训练、对齐与推理

- [ ] 比较 pretraining、SFT、instruction tuning、RLHF 和 DPO。
- [ ] 解释 LoRA 和 QLoRA。
- [ ] 解释 KV Cache、prefill 和 decode。
- [ ] 解释 batching、quantization 和 speculative decoding。
- [ ] 回答 [100 道 LLM 面试题](../interviews/100-llm-interview-questions.md) 的 21-35 题。

交付物：

- [ ] 写一个短回答：如何降低 LLM serving 延迟和成本？

## Day 3：RAG

- [ ] 画出 RAG pipeline。
- [ ] 解释 chunking tradeoffs。
- [ ] 比较 dense、sparse 和 hybrid retrieval。
- [ ] 解释 reranking 和 context compression。
- [ ] 回答 [50 道 RAG 面试题](../interviews/50-rag-interview-questions.md)。

交付物：

- [ ] 写一份 hallucinated RAG answer 的 debug plan。

## Day 4：AI Agent

- [ ] 解释 model-tool-observation loop。
- [ ] 解释 tool schema validation。
- [ ] 比较 ReAct 和 plan-and-execute。
- [ ] 解释 memory、state、verifier 和 guardrails。
- [ ] 回答 [50 道 AI Agent 面试题](../interviews/50-agent-interview-questions.md)。

交付物：

- [ ] 运行 [Minimal Agent Framework](../../examples/minimal-agent-framework/)，并解释 trajectory 的每一步。

## Day 5：Evaluation 与 Safety

- [ ] 解释 exact、semantic、human 和 system evaluation。
- [ ] 解释 LLM-as-a-judge 及其 biases。
- [ ] 解释 faithfulness、citation correctness 和 refusal quality。
- [ ] 解释 prompt injection 和 tool safety。
- [ ] 运行 [LLM Eval Harness](../../examples/llm-eval-harness/)。

交付物：

- [ ] 为一个 LLM app 设计 release gate。

## Day 6：System Design

- [ ] 设计企业知识助手。
- [ ] 设计 AI 客服助手。
- [ ] 设计 Coding Agent。
- [ ] 讨论 latency、cost、monitoring 和 human review。
- [ ] 复习 [LLM 系统设计笔记](../interviews/system-design.md)。

交付物：

- [ ] 准备一个完整 system design 回答：包含 architecture、tradeoffs、metrics 和 failure modes。

## Day 7：简历项目与模拟面试

- [ ] 从 [可写进简历的 AI 项目](../projects/README.md) 选择一个项目。
- [ ] 写两个 resume bullets。
- [ ] 准备三分钟项目 pitch。
- [ ] 用题库做 45 分钟模拟面试。
- [ ] 列出下周要改进的三个弱点。

交付物：

- [ ] 定稿一个可写进简历的 AI 项目故事。

