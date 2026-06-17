# LLM Eval Harness Example

这个 example 实现了一个无外部依赖的 tiny evaluation harness。

它展示：

- Versioned test cases。
- Deterministic model wrapper。
- Multiple evaluators。
- Pass/fail report。
- Latency tracking。
- Exact match、regex、citation、latency 和 cost checks。
- JSON report export。

## 运行

```bash
python3 examples/llm-eval-harness/run_eval.py
```

写入 JSON report：

```bash
python3 examples/llm-eval-harness/run_eval.py --report /tmp/llm-eval-report.json
```

## 文件

- `test_cases/cases.json`：示例评估用例。
- `model.py`：deterministic mock model。
- `evaluators.py`：keyword、exact match、regex、JSON schema、citation、refusal、latency 和 cost evaluators。
- `harness.py`：case runner 和 report builder。
- `run_eval.py`：可运行 CLI demo。

## 面试 talking points

- LLM 应用需要 regression tests，因为 prompts、models 和 data 都会变化。
- Evaluation 应把质量拆成任务相关检查。
- Deterministic evaluators 适合低成本、可靠地检查格式和策略。
- LLM-as-a-judge 可用于开放式语义检查，但需要校准。
- Release gates 应结合 quality、safety、latency 和 cost。

## 测试

```bash
python3 -m unittest discover examples/llm-eval-harness/tests
```

代码位于 [`examples/llm-eval-harness`](../../../examples/llm-eval-harness/)。
