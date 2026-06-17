# Curated High-Star AI Repositories

This page tracks high-quality, high-star repositories that are useful for LLM, RAG, agent, evaluation, and AI engineering interviews.

Star counts are approximate snapshots and change over time. Use stars as a popularity signal, not as the only quality signal.

Snapshot date: 2026-06-17.

## How To Use This List

- Read the README to understand positioning.
- Inspect architecture, abstractions, and examples.
- Pick one repo per category and build a small clone or minimal version.
- Convert lessons into interview talking points.

## LLM Foundations And Model Tooling

| Repository | Why It Matters | Interview Angle |
| --- | --- | --- |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Core model-definition framework for modern text, vision, audio, and multimodal models. Around 162k stars in the 2026-06-17 snapshot. | Model loading, tokenization, generation config, fine-tuning, ecosystem compatibility. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Practical examples and guides for OpenAI API usage. Around 74.2k stars in the 2026-06-17 snapshot. | API integration, prompting, embeddings, tool use, structured outputs, production examples. |

## RAG And Data Frameworks

| Repository | Why It Matters | Interview Angle |
| --- | --- | --- |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Broad agent and LLM application framework. Around 139k stars in the 2026-06-17 snapshot. | Chains, tools, agents, RAG pipelines, abstractions, ecosystem tradeoffs. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Data framework for building LLM apps, document agents, OCR, parsing, indexing, and RAG. Around 50.2k stars in the 2026-06-17 snapshot. | Connectors, indices, retrievers, query engines, document parsing, RAG architecture. |

## Agent Frameworks

| Repository | Why It Matters | Interview Angle |
| --- | --- | --- |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Framework for resilient stateful agents and workflows. Around 35k stars in the 2026-06-17 snapshot. | State machines, durable execution, workflow orchestration, agent control flow. |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Programming framework for agentic AI. Around 59k stars in the 2026-06-17 snapshot. | Multi-agent conversation, orchestration, tool use, human-in-the-loop. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Multi-agent orchestration framework focused on role-playing agents, crews, and flows. Around 53.8k stars in the 2026-06-17 snapshot. | Role-based agents, task delegation, workflow automation, multi-agent design. |

## Coding Agents

| Repository | Why It Matters | Interview Angle |
| --- | --- | --- |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | AI-driven software development agent platform. Around 77.4k stars in the 2026-06-17 snapshot. | Sandbox execution, coding agent architecture, browsing, shell tools, evaluation. |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | Agent that takes GitHub issues and attempts to fix them. Around 19.5k stars in the 2026-06-17 snapshot. | SWE-bench style workflows, repository exploration, patch generation, test-driven repair. |

## LLM Serving And Inference

| Repository | Why It Matters | Interview Angle |
| --- | --- | --- |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | High-throughput, memory-efficient LLM inference and serving engine. Around 83.1k stars in the 2026-06-17 snapshot. | KV cache, batching, throughput, latency, serving architecture, GPU memory management. |

## What To Learn From These Repos

### Abstractions

- How tools are represented.
- How state is stored.
- How model calls are wrapped.
- How retrieval components are composed.
- How evaluation is integrated.

### Engineering Patterns

- Explicit schemas.
- Plugin and integration systems.
- Async execution.
- Callback and tracing hooks.
- Configuration management.
- Test fixtures and examples.

### Interview Exercises

1. Implement a minimal LangGraph-style state machine agent.
2. Implement a mini LlamaIndex-style document index.
3. Implement a tiny vLLM-inspired request scheduler.
4. Implement a simple SWE-agent-style repair loop.
5. Implement an evaluation harness for RAG answers.

## Selection Criteria

Repos are included when they satisfy several of these:

- Strong GitHub adoption.
- Clear relevance to LLM, RAG, agents, serving, or evaluation.
- Useful architecture to study.
- Practical examples.
- Active ecosystem or research influence.

