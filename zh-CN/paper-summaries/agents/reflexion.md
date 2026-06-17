# Reflexion

论文：[arXiv:2303.11366](https://arxiv.org/abs/2303.11366)

## 问题

Agent 经常重复失败，因为不经过昂贵 fine-tuning 时，很难从先前尝试中学习。

## 方法

Reflexion 使用 verbal feedback 和 episodic memory。Agent 反思来自环境或自身的反馈，保存 lessons，并在后续尝试中使用。

## 为什么重要

它展示了 Agent 可以通过语言级 memory 改善后续尝试，而不需要更新模型权重。

## 实现注意事项

- Reflection 应有边界，避免循环。
- Memory 需要筛选，否则会保存坏经验。
- Feedback 可来自 tests、tools、humans 或 verifier models。

## 面试 Talking Points

- Reflexion 是 Agent 的 memory-and-feedback pattern。
- 它适合 coding 和 sequential decision tasks。
- Reflection 会增加成本，需要评估。

