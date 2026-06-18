from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agent import MiniCodingAgent, create_toy_repo


class MiniCodingAgentTests(unittest.TestCase):
    def test_repair_passes_tests(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "toy-repo"
            create_toy_repo(repo)
            result = MiniCodingAgent(repo).repair("Fix add")

            self.assertTrue(result.tests_passed)
            self.assertIn("return a + b", (repo / "calculator.py").read_text(encoding="utf-8"))
            self.assertIn("-    return a - b", result.diff)
            self.assertIn("+    return a + b", result.diff)


if __name__ == "__main__":
    unittest.main()

