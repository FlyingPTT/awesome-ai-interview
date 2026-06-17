# AI Agent 面试笔记

## Agent 系统设计模板

高质量回答应覆盖：

1. 用户目标和任务边界。
2. 可用工具和权限。
3. 状态表示。
4. 规划策略。
5. 执行循环。
6. 失败处理。
7. 验证。
8. 日志和可观测性。
9. 评估。
10. 安全与治理。

## 示例：Coding Agent

### 目标

构建一个 Agent：可以接收 GitHub issue，检查代码库，实现修复，运行测试，并创建 PR。

### 组件

- Repository reader。
- Search tool。
- Code editor。
- Shell executor。
- Test runner。
- Diff summarizer。
- Review loop。

### 失败处理

- 测试失败时，总结失败用例并进行有边界的 repair loop。
- 需要外部权限时，请求用户批准。
- 需求模糊时，提出澄清问题。
- diff 触及无关文件时，停止并解释。

### 评估

- Issue resolution rate。
- Test pass rate。
- Agent 提交后人工修改距离。
- Time to first working patch。
- Regression rate。

## 高频问题

### Agent 和 chatbot 有什么区别？

Chatbot 主要生成文本回复。Agent 可以使用工具、更新外部状态、拆解任务，并验证自己是否接近目标。

### 为什么 Agent 难评估？

Agent 任务往往有多条有效路径、外部副作用、动态环境和部分成功状态。评估应结合任务成功率、安全性、成本、延迟和人工审查。

### 如何让 Agent 更安全？

使用最小权限工具、危险操作显式审批、沙箱、审计日志、幂等操作、dry-run 模式和有边界的执行循环。

