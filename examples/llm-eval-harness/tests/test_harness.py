from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluators import CitationEvaluator, CostEvaluator, ExactMatchEvaluator, RegexEvaluator
from harness import EvalHarness, save_report
from model import MockModel


class EvalHarnessTests(unittest.TestCase):
    def test_suite_passes_sample_cases(self):
        cases = json.loads((ROOT / "test_cases" / "cases.json").read_text(encoding="utf-8"))
        report = EvalHarness(MockModel()).run_suite(cases)

        self.assertEqual(report["total"], 4)
        self.assertEqual(report["failed"], 0)
        self.assertEqual(report["pass_rate"], 1.0)

    def test_exact_match_evaluator(self):
        result = ExactMatchEvaluator().evaluate({"expected_exact": "hello"}, "hello")
        self.assertTrue(result.passed)

    def test_regex_evaluator(self):
        result = RegexEvaluator().evaluate({"expected_regex": "rag .* evidence"}, "RAG uses external evidence")
        self.assertTrue(result.passed)

    def test_citation_evaluator(self):
        result = CitationEvaluator().evaluate(
            {"expected_citation_required": True},
            "Answer with source. [source:doc-1]",
        )
        self.assertTrue(result.passed)

    def test_cost_evaluator(self):
        result = CostEvaluator().evaluate(
            {
                "estimated_input_tokens": 10,
                "estimated_output_tokens": 10,
                "max_estimated_cost_usd": 0.001,
            },
            "output",
        )
        self.assertTrue(result.passed)

    def test_save_report(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "report.json"
            save_report({"passed": 1}, path)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["passed"], 1)


if __name__ == "__main__":
    unittest.main()
