# AI Agent 工程师路线图

AI Agent 工程关注的是构建能够规划、使用工具、记忆上下文、从失败中恢复，并在受控自治范围内完成任务的系统。

## 核心模型

一个 Agent 系统通常包含：

- Model：推理和语言接口。
- Tools：搜索、代码执行、数据库、浏览器、API 等外部能力。
- Planner：把目标拆成可执行步骤。
- Executor：执行工具调用并更新状态。
- Memory：跨轮次或跨任务保存有用信息。
- Verifier：检查输出、约束和任务完成情况。
- Guardrails：定义权限、安全边界和操作限制。

## 核心主题

### 工具使用

- Function calling schema 设计。
- 工具选择。
- 工具结果总结。
- 幂等性与重试。
- 权限和沙箱设计。

### 规划

- ReAct。
- Plan-and-execute。
- Reflection。
- Tree search。
- 任务拆解。
- 长任务管理。

### 记忆

- 短期对话状态。
- 长期向量记忆。
- Episodic memory。
- 用户偏好记忆。
- 记忆检索与遗忘策略。

### 评估

- Task success rate。
- Tool-call accuracy。
- Human intervention rate。
- Cost per task。
- Latency per task。
- 工具调用失败后的恢复能力。

## 常见失败模式

- 幻觉式工具调用。
- 工具参数构造错误。
- 上下文污染。
- 无限规划循环。
- 隐式状态漂移。
- 工具权限过大。
- Evaluation leakage。

## 面试题

- 设计一个能 debug CI 失败的 Agent。
- 设计一个能读论文并构建文献地图的研究助手。
- 如何防止 Agent 删除生产数据？
- 没有唯一正确答案时如何评估 Agent？
- 如何让 Coding Agent 达到企业可信水平？

