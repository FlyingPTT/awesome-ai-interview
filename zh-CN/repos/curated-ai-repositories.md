# 高 Star 高质量 AI 仓库汇总

本页汇总对 LLM、RAG、Agent、Evaluation 和 AI 工程面试有帮助的高质量、高 star 仓库。

Star 数是快照值，会随时间变化。Stars 可以作为热度信号，但不应该作为唯一质量标准。

快照日期：2026-06-17。

## 如何使用这个列表

- 先读 README，理解项目定位。
- 看架构、核心抽象和 examples。
- 每个类别选一个仓库，手写一个 mini 版本。
- 把学到的设计转换成面试 talking points。

## LLM 基础与模型工具链

| 仓库 | 为什么重要 | 面试角度 |
| --- | --- | --- |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 现代文本、视觉、音频和多模态模型的核心 model-definition framework。2026-06-17 快照约 162k stars。 | 模型加载、tokenization、generation config、fine-tuning、生态兼容性。 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | OpenAI API 的实践 examples 和 guides。2026-06-17 快照约 74.2k stars。 | API 集成、prompting、embeddings、tool use、structured outputs、生产示例。 |

## RAG 与数据框架

| 仓库 | 为什么重要 | 面试角度 |
| --- | --- | --- |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 广泛使用的 Agent 和 LLM 应用框架。2026-06-17 快照约 139k stars。 | Chains、tools、agents、RAG pipelines、抽象设计、生态权衡。 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 构建 LLM 应用、文档 Agent、OCR、解析、索引和 RAG 的数据框架。2026-06-17 快照约 50.2k stars。 | Connectors、indices、retrievers、query engines、文档解析、RAG 架构。 |

## Agent 框架

| 仓库 | 为什么重要 | 面试角度 |
| --- | --- | --- |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 用于 resilient stateful agents 和 workflows 的框架。2026-06-17 快照约 35k stars。 | 状态机、durable execution、workflow orchestration、agent control flow。 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Agentic AI 编程框架。2026-06-17 快照约 59k stars。 | Multi-agent conversation、orchestration、tool use、human-in-the-loop。 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 面向 role-playing agents、crews 和 flows 的多 Agent 编排框架。2026-06-17 快照约 53.8k stars。 | Role-based agents、task delegation、workflow automation、multi-agent design。 |

## Coding Agents

| 仓库 | 为什么重要 | 面试角度 |
| --- | --- | --- |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | AI-driven software development agent platform。2026-06-17 快照约 77.4k stars。 | 沙箱执行、coding agent 架构、浏览器、shell tools、evaluation。 |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | 接收 GitHub issue 并尝试自动修复的 Agent。2026-06-17 快照约 19.5k stars。 | SWE-bench workflow、仓库探索、patch generation、test-driven repair。 |

## LLM Serving 与推理

| 仓库 | 为什么重要 | 面试角度 |
| --- | --- | --- |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 高吞吐、内存高效的 LLM inference 和 serving engine。2026-06-17 快照约 83.1k stars。 | KV Cache、batching、throughput、latency、serving architecture、GPU 显存管理。 |

## 应该从这些仓库学什么

### 核心抽象

- Tool 如何表示。
- State 如何存储。
- Model call 如何封装。
- Retrieval components 如何组合。
- Evaluation 如何接入。

### 工程模式

- 显式 schemas。
- Plugin 和 integration systems。
- Async execution。
- Callback 和 tracing hooks。
- 配置管理。
- Test fixtures 和 examples。

### 面试练习

1. 手写一个 LangGraph 风格的最小状态机 Agent。
2. 手写一个 LlamaIndex 风格的 mini document index。
3. 手写一个 vLLM 风格的简单 request scheduler。
4. 手写一个 SWE-agent 风格的 repair loop。
5. 手写一个 RAG answer evaluation harness。

## 收录标准

仓库满足以下若干条件时会被收录：

- GitHub adoption 强。
- 与 LLM、RAG、Agent、Serving 或 Evaluation 明确相关。
- 架构值得学习。
- 有实践 examples。
- 生态活跃或研究影响力强。

