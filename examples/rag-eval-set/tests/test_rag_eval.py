from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluate import run_eval


class RAGEvalSetTests(unittest.TestCase):
    def test_eval_set_passes(self):
        report = run_eval(ROOT / "test_cases" / "cases.json")
        self.assertEqual(report["total"], 3)
        self.assertEqual(report["failed"], 0)
        self.assertEqual(report["pass_rate"], 1.0)

    def test_report_export(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "rag-report.json"
            run_eval(ROOT / "test_cases" / "cases.json", path)
            loaded = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(loaded["passed"], 3)


if __name__ == "__main__":
    unittest.main()

