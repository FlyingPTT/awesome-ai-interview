# G-Eval

论文：[arXiv:2303.16634](https://arxiv.org/abs/2303.16634)

## 问题

传统 NLG metrics 对开放式生成的质量与人工判断相关性较弱。

## 方法

G-Eval 使用 LLM、任务特定 rubrics 和 chain-of-thought-style evaluation steps 对生成结果评分。

## 为什么重要

它推动了 rubric-driven LLM evaluation 在 summarization 和开放式生成任务中的使用。

## 实现注意事项

- Rubric design 很重要。
- Judge prompts 应版本化。
- 分数应与人工标签校准。
- Evaluation prompts 本身也可能 regression。

## 面试 Talking Points

- LLM evaluation 应 rubric-based。
- Judge prompts 是 evaluation system 的一部分。
- 必须测量与人工评分的相关性。

