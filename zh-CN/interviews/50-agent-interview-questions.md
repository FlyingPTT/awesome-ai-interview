# 50 道 AI Agent 面试题

本页整理 50 道 AI Agent 工程面试题，重点覆盖工具使用、规划、记忆、工作流编排、评估和安全。

## 基础

### 1. AI Agent 是什么？

要点：

- Agent 将模型、工具、状态和控制逻辑结合，用于完成目标。
- 它可以观察、规划、行动并验证进展。
- 生产 Agent 需要权限、日志、评估和失败处理。

### 2. Agent 和 chatbot 有什么区别？

要点：

- Chatbot 主要生成回答。
- Agent 可以调用工具并更新外部状态。
- Agent 需要任务边界和安全控制。

### 3. Agent 的核心组件有哪些？

要点：

- Model。
- Tools。
- Planner。
- Executor。
- Memory。
- State store。
- Verifier。
- Guardrails。

### 4. Tool calling 是什么？

要点：

- 模型选择工具并生成结构化参数。
- 系统执行工具并返回 observation。
- 工具 schema 和 validation 强烈影响可靠性。

### 5. Agent 工程难在哪里？

要点：

- 模型行为非确定性。
- 外部副作用。
- 长任务。
- 工具失败。
- 成功标准模糊。
- 安全与权限风险。

## 工具使用

### 6. 如何设计好的 tool schema？

要点：

- 清晰 name 和 description。
- 职责窄。
- required fields 明确。
- 强参数校验。
- 尽量幂等。

### 7. Tool hallucination 是什么？

要点：

- 模型编造不存在的工具或 unsupported argument。
- 用 explicit tool registry、schema validation 和 error feedback 缓解。

### 8. 如何处理工具错误？

要点：

- 返回结构化错误。
- 允许有边界重试。
- 区分 transient 和 permanent failure。
- 必要时升级给人。

### 9. 为什么最小权限对 Agent 重要？

要点：

- Agent 会以机器速度犯错。
- 工具只暴露必要能力。
- 危险操作需要审批。

### 10. Dry-run mode 是什么？

要点：

- 模拟操作但不产生副作用。
- 适合破坏性、昂贵或不可逆操作。
- 让人类能在执行前 review。

## 规划

### 11. ReAct 是什么？

要点：

- 交替 reasoning 和 acting。
- Agent 思考、调用工具、观察，然后继续。
- 适合搜索和工具使用任务。

### 12. Plan-and-execute 是什么？

要点：

- 先制定计划，再执行步骤。
- 适合长任务。
- observation 改变假设时需要 replanning。

### 13. Reflection 是什么？

要点：

- Agent 评审自己的输出或轨迹。
- 可提升质量。
- 也会增加成本和无效循环。

### 14. 如何防止无限循环？

要点：

- Step limits。
- Time and cost budgets。
- Progress checks。
- Verifier-based termination。
- Explicit stop conditions。

### 15. 如何拆解任务？

要点：

- 分离信息收集、规划、行动和验证。
- 每一步都应可观察。
- 避免“优化所有东西”这类模糊任务。

## Memory 与 State

### 16. Short-term memory 是什么？

要点：

- 当前对话和任务状态。
- 通常存于 context 或 state objects。
- 过长时需要 summarize。

### 17. Long-term memory 是什么？

要点：

- 持久化事实、偏好或历史任务结果。
- 通常从数据库或 vector store 检索。
- 需要 privacy、freshness 和 forgetting policies。

### 18. Episodic memory 是什么？

要点：

- 存储过去交互或任务轨迹。
- 有助于个性化和经验复用。
- 如果不筛选，可能强化错误。

### 19. 如何避免 context pollution？

要点：

- 工具输出结构化。
- 只总结相关信息。
- 区分可信指令和不可信内容。
- 清理 stale state。

### 20. Agent state 应如何存储？

要点：

- 长任务使用显式 state objects。
- 存储 tool results、plan、decisions 和 checkpoints。
- State 应可检查、可恢复。

## Workflow Orchestration

### 21. 什么时候 workflow 应该 deterministic？

要点：

- Routing、validation、permissions 和 irreversible actions 用确定性代码。
- 语言理解、综合和模糊判断交给模型。

### 22. State machine agent 是什么？

要点：

- Workflow 有显式 states 和 transitions。
- 更容易测试和监控。
- 灵活性低于完全开放式 Agent。

### 23. Human-in-the-loop control 是什么？

要点：

- 人类 review 或审批高风险步骤。
- Agent 应提供 evidence 和 proposed action。
- Review 结果可作为反馈。

### 24. 如何恢复长任务？

要点：

- 持久化 state 和 checkpoints。
- 存储已完成步骤和 pending actions。
- 工具调用保持幂等。
- 继续前验证外部状态。

### 25. 如何协调 multi-agent workflow？

要点：

- 分配清晰角色。
- 定义 shared state。
- 防止重复工作。
- 增加 coordinator 或 verifier。

## Evaluation

### 26. 如何评估 Agent？

要点：

- Task success rate。
- Tool-call accuracy。
- Recovery rate。
- Human intervention rate。
- Safety violations。
- Cost and latency。

### 27. 为什么只评估最终答案不够？

要点：

- Agent 可能用不安全路径得到正确答案。
- 工具误用可能被隐藏。
- 部分失败也重要。
- 副作用必须审计。

### 28. Trajectory evaluation 是什么？

要点：

- 评估 action、observation 和 decisions 的序列。
- 有助于诊断 planning 和 tool errors。
- 比只看最终输出信息更多。

### 29. 如何构建 Agent benchmark？

要点：

- 使用真实任务。
- 提供受控工具和环境。
- 定义成功标准。
- 包含 failure 和 recovery cases。

### 30. Coding Agent 关注哪些指标？

要点：

- Issue resolution rate。
- Test pass rate。
- Patch correctness。
- Human edit distance。
- Regression rate。
- Time to working patch。

## 安全

### 31. Agent 系统中的 prompt injection 是什么？

要点：

- 不可信内容试图覆盖指令。
- 当 Agent 能浏览、检索或调用工具时尤其危险。
- 可用 instruction hierarchy 和 tool constraints 缓解。

### 32. 如何隔离不可信内容？

要点：

- 标记 retrieved 或 browsed content 为 data。
- 不把它当成 instructions。
- 工具使用前 sanitize 和 validate outputs。

### 33. 如何保护 secrets？

要点：

- 非必要不把 secrets 暴露给 prompt。
- 使用 scoped credentials。
- Redact logs。
- 防止工具输出泄露敏感数据。

### 34. 如何控制破坏性操作？

要点：

- 要求审批。
- 使用 dry-run。
- 展示 diff 或 impact summary。
- 尽量可 rollback。

### 35. 如何审计 Agent 行为？

要点：

- 记录 prompts、tool calls、arguments、outputs、approvals 和 final results。
- 日志可搜索。
- 保护日志中的敏感数据。

## Coding Agents

### 36. 设计一个 Coding Agent。

要点：

- 读取 issue。
- 搜索仓库。
- 检查相关文件。
- 窄范围编辑。
- 运行测试。
- 必要时修复。
- 总结 diff 和验证。

### 37. Coding Agent 如何处理用户修改？

要点：

- 检测 dirty worktree。
- 避免覆盖无关修改。
- 解释冲突。
- 相关时与已有修改协作。

### 38. Coding Agent 如何选择测试？

要点：

- 从 focused tests 开始。
- 共享行为变化时运行更广测试。
- 报告未运行测试。
- 用失败指导 repair。

### 39. 如何防止宽泛危险编辑？

要点：

- 先阅读本地模式。
- 控制变更范围。
- 只有必要时增加抽象。
- 最终 review diff。

### 40. 什么让 Coding Agent enterprise-ready？

要点：

- Permission model。
- Audit logs。
- Policy checks。
- Test integration。
- Code review workflow。
- Repository-specific instructions。

## 研究与生产力 Agent

### 41. 设计论文阅读 Agent。

要点：

- 解析 PDF。
- 提取 problem、method、experiments、limitations。
- 构建 citation links。
- 生成学习笔记和面试问题。

### 42. 设计文献综述 Agent。

要点：

- 搜索论文。
- 按主题聚类。
- 追踪时间线。
- 比较方法。
- 识别开放问题。

### 43. 设计数据分析 Agent。

要点：

- 检查 schema。
- 生成假设。
- 运行代码。
- 验证结果。
- 输出可复现 notebook 或 report。

### 44. 设计浏览器 Agent。

要点：

- 导航页面。
- 抽取信息。
- 避免不可信指令。
- 验证重要事实。
- 处理动态页面。

### 45. 设计个人效率 Agent。

要点：

- Calendar、email、task tools。
- 强权限控制。
- 对外消息需要确认。
- Preference memory。
- Audit trail。

## Production Readiness

### 46. 如何判断哪些任务应该 agentic？

要点：

- Agentic tasks 涉及不确定性、工具和多步决策。
- 简单确定性任务应保持 deterministic。
- 高风险任务需要更强控制。

### 47. 如何降低 Agent 成本？

要点：

- 简单步骤用小模型。
- 缓存工具结果。
- 限制 reflection。
- 缩短 context。
- 验证成功后尽早停止。

### 48. 如何降低 Agent 延迟？

要点：

- 并行独立工具调用。
- 使用 deterministic routing。
- 避免不必要 planning。
- Stream intermediate progress。

### 49. Agent 最终应该报告什么？

要点：

- 做了什么。
- 验证证据。
- 已知限制。
- 未运行测试或未解决风险。
- 下一步建议。

### 50. 如何判断 Agent production-ready？

要点：

- 可靠 task success。
- 失败有边界。
- 安全工具权限。
- Evaluation suite。
- Monitoring and audit logs。
- Human escalation path。

