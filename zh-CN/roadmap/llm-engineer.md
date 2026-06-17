# LLM 工程师路线图

这份路线图面向准备 LLM Engineer、Generative AI Engineer 和 Applied AI Engineer 岗位的候选人。

## 核心基础

### Transformer

- Self-attention、Multi-head attention、位置编码。
- Encoder-only、Decoder-only、Encoder-decoder 架构。
- Causal language modeling 与 masked language modeling。
- 残差连接、LayerNorm、Feed-forward network。

### 训练

- 预训练目标。
- Supervised fine-tuning。
- Instruction tuning。
- RLHF、DPO 和 preference optimization。
- 数据质量、去重、污染检测和 synthetic data。

### 推理

- KV Cache。
- Prefill 与 Decode。
- Batch inference。
- 量化。
- Speculative decoding。
- Serving 延迟与吞吐权衡。

## 应用工程

### Prompting

- Zero-shot、Few-shot、Chain-of-thought、结构化输出。
- Prompt injection 与 prompt leakage。
- Prompt 版本管理和评估。

### RAG

- 文档解析与切分。
- Embedding 模型。
- Dense retrieval、Sparse retrieval、Hybrid retrieval。
- Reranking 与 query rewriting。
- Grounded generation 与 citation。

### Agent Systems

- Tool calling。
- Planning 与 execution。
- Memory。
- Multi-agent workflows。
- Verification 与 recovery loops。

## 评估

- 离线评估集。
- Golden answers 与 rubrics。
- LLM-as-a-judge。
- Faithfulness、relevance、latency、cost、safety。
- Prompt 和 workflow 的回归测试。

## 面试检查表

- 从原理解释 Transformer attention。
- 解释 KV Cache 为什么能提升 decoding 效率。
- 设计一个企业文档 RAG 系统。
- 比较 fine-tuning 和 RAG。
- Debug 生产 LLM 应用中的 hallucination。
- 设计 AI Agent 的评估方案。
- 讨论成本和延迟优化。

