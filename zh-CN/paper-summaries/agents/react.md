# ReAct

论文：[arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

## 问题

过去 reasoning 和 acting 经常被分开研究：模型要么在文本中推理，要么在环境中行动，但很少干净地结合二者。

## 方法

ReAct 交替生成 reasoning traces 和 actions。模型思考、调用工具或采取行动、观察结果，然后继续。

## 为什么重要

ReAct 成为 tool-using agents 的核心心智模型之一。它让 trajectory 更可解释，并支持外部信息获取。

## 实现注意事项

- Tool observations 应结构化。
- Reasoning/action loops 需要 step budgets。
- Tool outputs 可能带来 prompt injection 风险。
- ReAct 有用，但不足以保证生产安全。

## 面试 Talking Points

- ReAct 结合 reasoning 和 acting。
- 它通过可见 trajectory 提升可解释性。
- 生产 Agent 需要 ReAct prompting 之外的 guardrails。

