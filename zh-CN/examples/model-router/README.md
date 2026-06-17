# Model Router

一个无外部依赖的 model routing demo，在便宜快速模型和更强推理模型之间做选择。

它展示：

- 按风险和复杂度进行任务分类。
- 小模型 / 大模型路由。
- 成本估算。
- 延迟估算。
- 可解释 routing decision。

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

