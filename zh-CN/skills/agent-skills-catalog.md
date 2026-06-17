# Agent Skills Catalog

本目录汇总可复用 AI Agent skills。每个 skill 都写成实用 workflow，可以转换成 prompt、system instruction 或 `SKILL.md` 包。

## Skill 设计原则

- Skill 范围要窄。
- 定义输入和输出。
- 指定允许工具。
- 明确验证步骤。
- 加入失败处理。
- 优先结构化输出。
- 避免隐藏副作用。

## 1. 论文阅读 Skill

目的：把研究论文转换成结构化学习笔记。

输入：

- 论文标题、URL 或 PDF。
- 目标主题或岗位。

工作流：

1. 提取 metadata。
2. 识别问题。
3. 总结方法。
4. 提取关键公式或算法。
5. 总结实验。
6. 识别局限。
7. 生成面试问题。

输出：

- 一句话总结。
- 方法拆解。
- 优点和局限。
- 实现注意事项。
- 面试 talking points。

## 2. 文献综述 Skill

目的：从多篇论文构建 topic map。

工作流：

1. 收集候选论文。
2. 按问题分组。
3. 按方法族分组。
4. 建立时间线。
5. 识别代表性论文。
6. 提取开放问题。

输出：

- Taxonomy。
- Paper table。
- Reading order。
- Trend summary。
- Open problems。

## 3. RAG 诊断 Skill

目的：识别 RAG 答案为什么错误。

工作流：

1. 检查正确证据是否被检索到。
2. 如果没有，检查 parsing、chunking、embeddings、filters 和 query rewriting。
3. 如果有，检查 prompt、context ordering、citations 和 refusal logic。
4. 创建 regression case。

输出：

- Failure category。
- Evidence。
- Likely root cause。
- Fix plan。
- Regression test。

## 4. Coding Repair Skill

目的：修复代码库中的 bug 或 failing test。

工作流：

1. 复现失败。
2. 搜索相关代码。
3. 阅读本地模式。
4. 实现 scoped fix。
5. 运行 focused tests。
6. 总结 diff 和验证。

质量标准：

- 不覆盖无关用户修改。
- 不无故扩大范围。
- 报告未运行的测试。

## 5. Code Review Skill

目的：审查 patch 中的 bug、回归和测试缺口。

工作流：

1. 检查 diff。
2. 识别行为变化。
3. 查找 correctness、security、performance 和 test risks。
4. 排序 findings。
5. 提供文件和行号引用。

输出：

- Findings first。
- Open questions。
- Brief summary。

## 6. Interview Answer Skill

目的：把技术主题转换成强面试回答。

工作流：

1. 写一句话答案。
2. 解释机制。
3. 讨论 tradeoffs。
4. 加具体例子。
5. 准备追问回答。

输出：

- Short answer。
- Expanded answer。
- Follow-up questions。
- Common pitfalls。

## 7. Hot Topic Tracker Skill

目的：把快速变化的 AI trend 转换成学习笔记。

工作流：

1. 收集模型发布、论文、框架和产品变化。
2. 按主题分组。
3. 识别为什么重要。
4. 提取面试题。
5. 提取项目 idea。

输出：

- Weekly trend digest。
- Interview talking points。
- Project opportunities。

## 8. Resume Project Generator Skill

目的：把技术主题转换成简历项目。

工作流：

1. 选择真实用户问题。
2. 设计最小架构。
3. 识别非平凡 tradeoffs。
4. 定义评估指标。
5. 写 resume bullets。
6. 准备面试 talking points。

输出：

- Project idea。
- Architecture。
- Milestones。
- Metrics。
- Resume bullet。

## 9. Evaluation Builder Skill

目的：为 LLM、RAG 或 Agent 系统设计评估计划。

工作流：

1. 定义成功标准。
2. 创建代表性 test cases。
3. 加入 edge 和 adversarial cases。
4. 选择 metrics。
5. 决定 human review policy。
6. 设置 regression thresholds。

输出：

- Dataset plan。
- Metrics。
- Rubric。
- Regression policy。

## 10. System Design Drill Skill

目的：准备 AI system design 面试。

工作流：

1. 澄清产品需求。
2. 定义约束。
3. 画架构。
4. 讨论数据流。
5. 讨论评估。
6. 讨论可靠性、成本、安全和监控。

输出：

- Design outline。
- Key tradeoffs。
- Failure modes。
- Evaluation plan。

