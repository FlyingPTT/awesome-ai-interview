# Speculative Decoding

论文：[arXiv:2211.17192](https://arxiv.org/abs/2211.17192)

## 问题

自回归 decoding 很慢，因为 token 必须顺序生成。

## 方法

较小的 draft model 提出多个 token，较大的 target model 并行验证它们，同时保持 target distribution 不变。

## 为什么重要

当 draft acceptance 较高时，speculative decoding 可以在不改变最终输出分布的情况下降低延迟。

## 实现注意事项

- Draft model 质量控制 speedup。
- Acceptance rate 是关键指标。
- Verification 必须保持输出分布。
- 收益取决于 workload 和 hardware。

## 面试 Talking Points

- Speculative decoding 用便宜模型加速强模型。
- 当许多 draft tokens 被接受时效果好。
- 它用额外 draft computation 换更少 target-model decoding steps。

