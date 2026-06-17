# Coding Agent Skills

## 仓库修复 Skill

目的：修复已有代码库中的 failing test 或 issue。

工作流：

1. 检查失败命令或 issue。
2. 搜索相关文件。
3. 阅读本地代码风格。
4. 实现最小合理修复。
5. 运行聚焦测试。
6. 总结 diff 和验证结果。

质量标准：

- 不重写无关代码。
- 不静默忽略失败测试。
- 不覆盖用户修改。
- 解释剩余风险。

## Code Review Skill

目的：审查 patch 中的 bug 和回归风险。

工作流：

1. 检查 diff。
2. 识别行为变化。
3. 查找 correctness、security、performance 和 test gaps。
4. 按严重程度排序 findings。
5. 提供文件和行号引用。

输出：

- Findings 优先。
- Open questions。
- 简短总结。

