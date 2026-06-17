# 可运行 Examples

这些小型、无外部依赖的 examples，会把仓库中的面试笔记转换成可以直接运行的代码。

## Examples

- [Minimal Agent Framework](minimal-agent-framework/)：包含显式 state、tool registry、schema validation、step budget 和 trajectory logging 的模型-工具-observation 循环。
- [LLM Eval Harness](llm-eval-harness/)：包含 versioned test cases、deterministic model wrapper、evaluators、latency tracking 和 pass/fail report。

## 为什么这些示例重要？

这些 examples 故意做得很小，方便面试讲解：

- Agent 如何决定调用哪个工具？
- 如何校验 tool arguments？
- 如何防止 runaway loops？
- 如何重复评估 LLM 行为？
- 如何为 prompt 和模型变化构建 release gates？

代码位于仓库根目录的 [`examples/`](../../examples/)。

