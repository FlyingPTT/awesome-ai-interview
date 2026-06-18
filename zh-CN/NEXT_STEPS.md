# 下一步扩充计划

这个文件用于保持仓库持续可维护。每次扩充都应该对面试有用、对 GitHub 访客可见，并且尽量能通过可运行 examples 验证。

## 近期 Backlog

- 将 coding-agent mini example 扩展为两步 repair loop：定位、修改、跑测试、分析失败、再次修改。
- 增加一个面向文档截图和表格 PDF 的 multimodal RAG 小示例。
- 增加 model-router evaluation report，对比 cheap-first、strong-only 和 cascade policies。
- 增加 RAG observability 笔记，覆盖 retrieval hit rate、citation precision、refusal quality 和 latency。
- 增加 multimodal models 和 VLM agents 的论文路线图。

## 维护节奏

1. 增加一个面试模块或一个可运行 example。
2. 每个 Markdown 页面都同步维护中文版本。
3. 在 README、docs index、roadmap 和 weekly digest 中加入入口。
4. 运行 `bash scripts/test_examples.sh`。
5. 使用简短、聚焦主题的 commit message 提交。

## 质量标准

- 每个 example 应该能在本地无付费 API 运行。
- 每个项目都应该能提炼成简历 talking point。
- 每份面试笔记都应该包含 tradeoffs、failure modes 和 production details。
- 每个新主题都应该连接到 LLM、RAG、Agent、Evaluation、Multimodal AI 或 AI Engineering 面试。

## 下一步 TODO

- 将 `examples/coding-agent-mini` 扩展成更真实的 harness，加入 tool registry、patch validation 和 execution sandbox。
- 增加 10 道 Coding Agent 系统设计题，把 mini example 和真实仓库自动化联系起来。
- 给 HTML docs 增加轻量导航区，覆盖 projects、interviews、papers 和 high-star repos。
