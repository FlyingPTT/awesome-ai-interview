# LLM 评估面试笔记

## 为什么评估重要？

LLM 应用是概率系统。Prompt、模型版本、数据和检索策略的变化都可能引入回归。评估是安全上线的核心机制。

## 评估类型

### 精确评估

适合输出有确定答案的任务，例如分类、抽取或结构化字段。

### 语义评估

适合存在多个合理答案的任务，通常使用 embedding、rubric 或 LLM-as-a-judge。

### 人工评估

适合高风险、主观或产品关键场景。

### 系统评估

衡量 latency、cost、reliability、safety 和 user satisfaction。

## 常见指标

- Accuracy。
- Faithfulness。
- Relevance。
- Helpfulness。
- Refusal quality。
- Tool-call accuracy。
- Retrieval recall。
- Citation correctness。
- Cost per successful task。
- Human intervention rate。

## 面试题

- 没有唯一正确答案时如何评估 chatbot？
- 如何避免 LLM-as-a-judge bias？
- 如何评估 AI Agent？
- 如何构建 prompt regression test suite？
- 如何分别评估 RAG 的 retrieval 和 generation？

