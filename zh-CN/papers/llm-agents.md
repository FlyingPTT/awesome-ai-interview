# LLM Agents 论文路线图

本页跟踪理解 AI Agents、工具使用、规划、reflection 和 multi-agent systems 所需的论文与概念。

## 核心问题

- 语言模型如何使用工具？
- Agent 应该如何规划和修改计划？
- Agent 如何验证进展？
- 哪些逻辑应该 deterministic，哪些可以交给模型自治？
- 如何评估 Agent trajectory？

## 阅读顺序

### 1. Tool Use

学习：

- Tool-augmented language models。
- Function calling。
- Program-aided reasoning。
- Retrieval 与 browsing tools。

面试要点：

- Tool use 把语言模型变成系统。Tool schema design、validation 和 permissions 都成为模型质量的一部分。

### 2. Reasoning And Acting

学习：

- ReAct-style reasoning and acting。
- Plan-and-execute agents。
- Reflection 与 self-critique。
- Verifier-guided execution。

面试要点：

- Planning 有用，但开放式 loop 需要 budgets、state 和 stop conditions。

### 3. Multi-Agent Systems

学习：

- Role-based collaboration。
- Debate and critique。
- Coordinator-worker patterns。
- Human-in-the-loop workflows。

面试要点：

- Multi-agent 可以改善拆解，但会增加协调成本和失败模式。

### 4. Coding Agents

学习：

- SWE-bench style tasks。
- Repository exploration。
- Patch generation。
- Test-based repair loops。

面试要点：

- Coding agent 应按 issue resolution、test pass rate、regression risk 和 human edit distance 评估。

## 实现注意事项

- Agent state 显式化。
- 存储 trajectory logs。
- 校验 tool arguments。
- 高风险操作需要审批。
- 区分可信指令和不可信内容。

## 面试题

- Agent 和 chatbot 有什么区别？
- 如何防止 infinite loops？
- 如何评估 Agent trajectory？
- 什么让 Coding Agent 安全？
- 什么时候 deterministic workflow 比 Agent 更好？

