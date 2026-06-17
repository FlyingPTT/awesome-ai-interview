# 项目：Minimal Agent Framework

## 目标

从零构建一个小型 Agent framework，理解模型如何被调度去遵循指令、调用工具、观察结果、更新状态并安全停止。

这个项目适合面试，因为它展示你理解 Agent framework 背后的机制，而不只是会使用现成库。

## Framework 应该做什么

- 接收用户目标。
- 维护显式 agent state。
- 通过模型输出选择工具。
- 校验工具参数。
- 执行工具。
- 将 observation 反馈给模型。
- 在任务完成或预算耗尽时停止。
- 输出可审计 trajectory。

## 架构

```text
user goal
   |
   v
agent loop
   |
   +--> planner/model call
   |
   +--> tool router
   |
   +--> tool executor
   |
   +--> observation store
   |
   +--> verifier / stop condition
   |
   v
final answer + trajectory log
```

## 核心抽象

### Tool

```python
class Tool:
    name: str
    description: str
    schema: dict

    def run(self, **kwargs):
        raise NotImplementedError
```

### Agent State

```python
class AgentState:
    goal: str
    steps: list
    observations: list
    budget_remaining: int
    final_answer: str | None
```

### Agent Step

```json
{
  "thought": "I need to inspect the file list first.",
  "tool": "search_files",
  "arguments": {"query": "README"},
  "observation": "README.md found",
  "status": "completed"
}
```

## 最小 Agent Loop

```python
while not done and state.budget_remaining > 0:
    action = model.decide(
        goal=state.goal,
        history=state.steps,
        tools=tool_registry.schemas(),
    )

    if action.type == "final":
        state.final_answer = action.content
        break

    tool = tool_registry.get(action.tool_name)
    args = validate(action.arguments, tool.schema)
    observation = tool.run(**args)
    state.steps.append({
        "action": action,
        "observation": observation,
    })
    state.budget_remaining -= 1
```

## 安全控制

- Tool schema validation。
- Step limit。
- Cost and time budget。
- 高风险工具需要人工审批。
- Dry-run mode。
- Audit log。
- Permission-scoped tool registry。
- 显式 final verification。

## 工具例子

- `search_files(query)`。
- `read_file(path)`。
- `write_patch(path, diff)`。
- `run_tests(command)`。
- `web_search(query)`。
- `calculator(expression)`。
- `ask_human(question)`。

## 面试 talking points

- Agent 可靠性往往更多取决于工具设计和控制流，而不只是模型智能。
- Agent loop 应暴露 state 和 trajectory，方便 debugging。
- 危险操作应该 deterministic、validated、permissioned。
- Stop conditions 和 planning 同样重要。
- 小而确定的 workflow 往往比完全自治 Agent 更可靠。

## 常见追问

- 如何防止 infinite loops？
- 如何校验 tool arguments？
- 如何恢复长任务？
- 如何评估 trajectory quality？
- 如何处理 tool output 中的 prompt injection？

## 简历 Bullet

实现最小 Agent framework，包含显式 state、tool registry、schema validation、模型-工具-observation 循环、budgeted execution、人工审批 hooks 和 trajectory logging，用于可 debug 的 AI workflows。

