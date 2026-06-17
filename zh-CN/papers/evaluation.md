# LLM Evaluation 论文路线图

本页跟踪评估 LLM、RAG 系统和 Agent 的概念与研究方向。

## 核心问题

- 如何评估开放式答案？
- 如何评估 faithfulness？
- Prompt 或模型变化后如何检测 regression？
- LLM-as-a-judge 可靠吗？
- 如何在 final answer 之外评估 Agent？

## 评估层级

### 1. Model-Level Evaluation

关注：

- 通用 benchmarks。
- Reasoning。
- Coding。
- Safety。
- Multilingual capability。

面试要点：

- Benchmarks 有用，但可能被污染，或与产品任务不一致。

### 2. Application-Level Evaluation

关注：

- Task-specific datasets。
- Rubrics。
- Human review。
- Regression tests。
- Product metrics。

面试要点：

- 生产 LLM 应用需要自己的评估集，而不只是公共 benchmark 分数。

### 3. RAG Evaluation

关注：

- Retrieval recall。
- Context precision。
- Answer faithfulness。
- Citation correctness。
- Refusal quality。

面试要点：

- RAG evaluation 必须把 retrieval quality 和 generation quality 分开。

### 4. Agent Evaluation

关注：

- Task success。
- Tool-call accuracy。
- Trajectory quality。
- Recovery from failure。
- Safety violations。
- Cost and latency。

面试要点：

- Final answer quality 不够。不安全或浪费的 trajectory 也重要。

## LLM-As-A-Judge Notes

优点：

- 扩展 semantic evaluation。
- 支持 rubric-based scoring。
- 适合比较输出。

风险：

- Position bias。
- Verbosity bias。
- Model-family bias。
- Prompt sensitivity。
- Calibration 弱。

缓解：

- 用人工标签校准。
- 合适时用 pairwise comparisons。
- 打乱输出顺序。
- Rubric 保持具体。
- 追踪 judge version。

## 面试题

- 如何评估开放式答案？
- 如何构建 golden set？
- 如何避免 LLM-as-a-judge bias？
- 如何评估 refusal quality？
- 如何为 LLM app 设计 release gate？

