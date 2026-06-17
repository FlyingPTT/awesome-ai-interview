# Model Router

一个无外部依赖的 model routing demo，在便宜快速模型和更强推理模型之间做选择。

它展示：

- 按风险和复杂度进行任务分类。
- 小模型 / 大模型路由。
- 成本估算。
- 延迟估算。
- 可解释 routing decision。
- 小模型置信度低时 fallback/cascade 到大模型。

## 运行

```bash
python3 examples/model-router/run_demo.py
```

## 测试

```bash
python3 -m unittest discover examples/model-router/tests
```

## 面试 talking points

- 成本优化通常是系统设计问题。
- 不是每个请求都需要最强模型。
- 高风险任务应该路由到更强模型或人工 review。
- Routing policy 需要评估，因为错误路由可能静默降低质量。
- Model router 应暴露 reason、cost 和 latency。
- Cascade 应暴露 route path，方便 debug 静默质量下降。

## Fallback Policy

这个 demo 会先把简单任务交给小模型。如果 `small_model_confidence` 低于 `0.7`，router 会升级到大模型，并记录 route path，例如：

```text
small-fast-model -> large-reasoning-model
```
