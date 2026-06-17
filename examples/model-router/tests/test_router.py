from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from router import LARGE_MODEL, SMALL_MODEL, ModelRouter, answer_with_route


class ModelRouterTests(unittest.TestCase):
    def test_simple_task_routes_to_small_model(self):
        decision = ModelRouter().route("Format this output")
        self.assertEqual(decision.model, SMALL_MODEL)

    def test_complex_task_routes_to_large_model(self):
        decision = ModelRouter().route("Design a multi-step agent architecture")
        self.assertEqual(decision.model, LARGE_MODEL)

    def test_high_risk_task_routes_to_large_model(self):
        decision = ModelRouter().route("Answer a legal contract question")
        self.assertEqual(decision.model, LARGE_MODEL)

    def test_cost_estimate_present(self):
        result = answer_with_route("Format this output")
        self.assertIn("estimated_cost_usd", result)
        self.assertGreater(result["estimated_latency_ms"], 0)


if __name__ == "__main__":
    unittest.main()

