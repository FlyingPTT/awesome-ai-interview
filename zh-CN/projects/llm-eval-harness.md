# 项目：LLM Evaluation Harness

## 目标

构建一个小型 evaluation harness，用于把 prompts、models、tools 和 expected outputs 放入可重复测试用例中执行。这个项目很适合面试，因为它体现你理解 LLM 系统如何安全上线，而不只是做 demo。

## Harness 应该做什么

- 从 JSON 或 YAML 加载测试用例。
- 对指定 prompt 或 workflow 调用模型。
- 支持 deterministic checks 和 rubric-based checks。
- 比较不同模型版本输出。
- 记录 latency、token usage、cost 和 pass/fail。
- 导出 regression report。

## 架构

```text
test cases
   |
   v
case runner -> prompt/workflow executor -> model client
   |                                      |
   v                                      v
evaluators <------------------------ raw outputs
   |
   v
reporter
```

## 核心抽象

### Test Case

```json
{
  "id": "rag_refusal_001",
  "input": "What is the refund policy for enterprise plan?",
  "expected_behavior": "refuse_if_no_evidence",
  "tags": ["rag", "refusal", "policy"]
}
```

### Evaluator

Evaluator 检查输出的一个维度。

例子：

- Exact match evaluator。
- JSON schema evaluator。
- Citation evaluator。
- Faithfulness evaluator。
- LLM-as-a-judge evaluator。
- Safety evaluator。

### Report

Report 应包括：

- Pass rate。
- Failed cases。
- Latency distribution。
- Cost estimate。
- Model and prompt version。
- 与上次 run 的 diff。

## 最小伪代码

```python
class EvalHarness:
    def __init__(self, model, evaluators):
        self.model = model
        self.evaluators = evaluators

    def run_case(self, case):
        output = self.model.generate(case["input"])
        scores = [e.evaluate(case, output) for e in self.evaluators]
        return {
            "case_id": case["id"],
            "output": output,
            "scores": scores,
            "passed": all(score.passed for score in scores),
        }

    def run_suite(self, cases):
        return [self.run_case(case) for case in cases]
```

## 评估维度

- Correctness。
- Format validity。
- Faithfulness。
- Citation correctness。
- Refusal quality。
- Safety。
- Latency。
- Cost。

## 面试 talking points

- LLM 系统需要 regression tests，因为 prompts 和模型版本都会变化。
- 最终答案质量应拆解成任务相关指标。
- RAG evaluation 应分别测试 retrieval 和 generation。
- Agent evaluation 应包含 trajectory 和 tool-call correctness。
- LLM-as-a-judge 应用人工标签校准。

## 常见追问

- 如何避免 LLM-as-a-judge bias？
- 如何构建 golden dataset？
- 如何评估开放式答案？
- 如何比较两个模型版本？
- 如何决定 release gate？

## 简历 Bullet

构建 LLM evaluation harness，支持跨 prompt 和 model 版本运行测试套件，包含 deterministic 与 rubric-based evaluators，并报告 quality、latency、cost 和 regression metrics，用于 LLM 应用安全发布。

