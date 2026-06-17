# Toolformer

论文：[arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

## 问题

语言模型能解决很多任务，但在算术、事实查询、翻译、日历访问等外部操作上仍然会输给简单系统。

## 方法

Toolformer 使用少量示例和 self-supervised data generation 教语言模型调用 API。模型学习何时调用工具、传什么参数，以及如何利用返回结果。

## 为什么重要

它把 tool use 视为可学习行为，而不只是手写 orchestration pattern。

## 实现注意事项

- Tool call 数据质量很重要。
- Tool APIs 应窄而清晰。
- 模型生成的 tool calls 需要 validation。
- Tool use 可以在不增大模型的情况下提升能力。

## 面试 Talking Points

- Toolformer 从 self-supervised signals 学习 tool use。
- Tool use 适合外部系统比模型更强的任务。
- 生产中仍需要 schema design 和 validation。

