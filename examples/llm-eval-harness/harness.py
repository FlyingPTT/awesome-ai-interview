from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from evaluators import EvalResult, default_evaluators
from model import MockModel


class EvalHarness:
    def __init__(self, model: MockModel) -> None:
        self.model = model
        self.evaluators = default_evaluators()

    def run_case(self, case: dict[str, Any]) -> dict[str, Any]:
        start = time.perf_counter()
        output = self.model.generate(case["input"])
        latency_ms = round((time.perf_counter() - start) * 1000, 3)
        results = [evaluator.evaluate(case, output) for evaluator in self.evaluators]
        return {
            "case_id": case["id"],
            "tags": case.get("tags", []),
            "model": self.model.name,
            "input": case["input"],
            "output": output,
            "latency_ms": latency_ms,
            "results": [result.__dict__ for result in results],
            "passed": all(result.passed for result in results),
        }

    def run_suite(self, cases: list[dict[str, Any]]) -> dict[str, Any]:
        case_results = [self.run_case(case) for case in cases]
        passed = sum(1 for result in case_results if result["passed"])
        return {
            "model": self.model.name,
            "total": len(case_results),
            "passed": passed,
            "failed": len(case_results) - passed,
            "pass_rate": round(passed / len(case_results), 3) if case_results else 0,
            "cases": case_results,
        }


def load_cases(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def format_failures(report: dict[str, Any]) -> str:
    lines = []
    for case in report["cases"]:
        if case["passed"]:
            continue
        failed_checks = [
            EvalResult(**result).message for result in case["results"] if not result["passed"]
        ]
        lines.append(f"- {case['case_id']}: {'; '.join(failed_checks)}")
    return "\n".join(lines) if lines else "No failures."

