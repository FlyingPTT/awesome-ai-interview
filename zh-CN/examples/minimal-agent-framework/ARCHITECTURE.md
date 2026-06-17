# Minimal Agent Framework 架构

这个 example 故意做得很小，但它覆盖了大型 Agent framework 的核心控制循环。

## 控制流

```text
goal
  |
  v
AgentState
  |
  v
ScriptedModel.decide(...)
  |
  +-- final answer -> stop
  |
  +-- tool action -> ToolRegistry.get(...)
                    |
                    v
              Tool.validate(...)
                    |
                    v
              Tool.run(...)
                    |
                    v
              observation appended to state.steps
                    |
                    v
              continue until final answer or step budget exhausted
```

## 核心组件

### `AgentState`

保存当前 goal、剩余 step budget、tool trajectory 和 final answer。

为什么重要：

- 让 Agent 可检查。
- 让长任务可恢复。
- 因为 trajectory 显式存在，所以可以评估。

### `ScriptedModel`

一个 deterministic LLM 替身，用来决定调用工具还是输出 final answer。

为什么重要：

- 不需要 API key 就能运行 example。
- 展示 model action 应该长什么样。
- 后续可以替换成真实 model client。

### `ToolRegistry`

保存可用工具，并把 schemas 暴露给模型。

为什么重要：

- 防止调用未知工具。
- 把工具描述和 validation 放在一个地方。
- 支持 `requires_approval` 这类权限元数据。

### `Tool`

用 name、description、argument schema 和 approval flag 包装 handler。

为什么重要：

- Tool schema validation 可以在副作用发生前拦截坏参数。
- Approval flags 为 human-in-the-loop 控制提供 hook。

## 状态转换

| 状态 | 事件 | 下一状态 |
| --- | --- | --- |
| Running | 模型返回 tool action | 校验并运行工具 |
| Running | 工具返回 observation | 追加 step 并继续 |
| Running | 模型返回 final answer | 停止 |
| Running | Budget 归零 | 用 budget message 停止 |
| Running | 工具需要 approval | 抛出 permission error |
| Running | 工具 validation 失败 | 抛出 validation error |

## 失败模式

- 未知工具名。
- 缺少或多余工具参数。
- 工具参数类型错误。
- 危险工具需要审批。
- Step budget 耗尽。
- 工具实现不安全。

## 面试 talking points

- Agent framework 本质是围绕模型调用的 orchestration system。
- 显式 state 是 demo 和可 debug workflow 的分界线。
- Tool schema 是安全边界的一部分。
- Stop conditions 防止失控自治。
- 风险操作应由 deterministic workflow logic 防护。

