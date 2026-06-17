from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class EvalResult:
    name: str
    passed: bool
    message: str


class Evaluator(Protocol):
    name: str

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        ...


class KeywordEvaluator:
    name = "keyword"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        keywords = case.get("expected_keywords")
        if not keywords:
            return EvalResult(self.name, True, "no keyword expectation")
        output_lower = output.lower()
        missing = [word for word in keywords if word.lower() not in output_lower]
        if missing:
            return EvalResult(self.name, False, f"missing keywords: {missing}")
        return EvalResult(self.name, True, "all expected keywords found")


class ExactMatchEvaluator:
    name = "exact_match"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        expected = case.get("expected_exact")
        if expected is None:
            return EvalResult(self.name, True, "no exact match expectation")
        if output == expected:
            return EvalResult(self.name, True, "exact match satisfied")
        return EvalResult(self.name, False, "output did not exactly match expected text")


class RegexEvaluator:
    name = "regex"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        pattern = case.get("expected_regex")
        if not pattern:
            return EvalResult(self.name, True, "no regex expectation")
        if re.search(pattern, output, flags=re.IGNORECASE):
            return EvalResult(self.name, True, "regex matched")
        return EvalResult(self.name, False, f"regex did not match: {pattern}")


class JsonSchemaEvaluator:
    name = "json_schema"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        expected_schema = case.get("expected_schema")
        if not expected_schema:
            return EvalResult(self.name, True, "no schema expectation")
        try:
            parsed = json.loads(output)
        except json.JSONDecodeError as exc:
            return EvalResult(self.name, False, f"invalid JSON: {exc}")
        missing = [key for key in expected_schema if key not in parsed]
        if missing:
            return EvalResult(self.name, False, f"missing JSON keys: {missing}")
        return EvalResult(self.name, True, "schema satisfied")


class CitationEvaluator:
    name = "citation"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        if not case.get("expected_citation_required"):
            return EvalResult(self.name, True, "no citation expectation")
        has_citation = bool(re.search(r"\[(source|doc|citation):[^\]]+\]", output, flags=re.IGNORECASE))
        if has_citation:
            return EvalResult(self.name, True, "citation detected")
        return EvalResult(self.name, False, "expected citation was not detected")


class RefusalEvaluator:
    name = "refusal"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        if case.get("expected_behavior") != "refuse":
            return EvalResult(self.name, True, "no refusal expectation")
        refusal_markers = ["cannot", "can't", "do not", "permission", "private"]
        if any(marker in output.lower() for marker in refusal_markers):
            return EvalResult(self.name, True, "refusal detected")
        return EvalResult(self.name, False, "expected refusal was not detected")


class LatencyEvaluator:
    name = "latency"

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        max_latency = case.get("expected_max_latency_ms")
        actual_latency = case.get("_observed_latency_ms")
        if max_latency is None or actual_latency is None:
            return EvalResult(self.name, True, "no latency expectation")
        if actual_latency <= max_latency:
            return EvalResult(self.name, True, f"latency {actual_latency}ms within budget")
        return EvalResult(self.name, False, f"latency {actual_latency}ms exceeded {max_latency}ms")


class CostEvaluator:
    name = "cost"

    INPUT_PRICE_PER_1K = 0.0005
    OUTPUT_PRICE_PER_1K = 0.0015

    def estimate_cost(self, case: dict[str, Any]) -> float:
        input_tokens = case.get("estimated_input_tokens", 0)
        output_tokens = case.get("estimated_output_tokens", 0)
        return round(
            (input_tokens / 1000 * self.INPUT_PRICE_PER_1K)
            + (output_tokens / 1000 * self.OUTPUT_PRICE_PER_1K),
            8,
        )

    def evaluate(self, case: dict[str, Any], output: str) -> EvalResult:
        max_cost = case.get("max_estimated_cost_usd")
        if max_cost is None:
            return EvalResult(self.name, True, "no cost expectation")
        estimated = self.estimate_cost(case)
        if estimated <= max_cost:
            return EvalResult(self.name, True, f"estimated cost ${estimated} within budget")
        return EvalResult(self.name, False, f"estimated cost ${estimated} exceeded ${max_cost}")


def default_evaluators() -> list[Evaluator]:
    return [
        KeywordEvaluator(),
        ExactMatchEvaluator(),
        RegexEvaluator(),
        JsonSchemaEvaluator(),
        CitationEvaluator(),
        RefusalEvaluator(),
        LatencyEvaluator(),
        CostEvaluator(),
    ]
