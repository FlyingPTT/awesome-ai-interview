from __future__ import annotations

import json
from pathlib import Path

from harness import EvalHarness, format_failures, load_cases
from model import MockModel


def main() -> None:
    root = Path(__file__).parent
    cases = load_cases(root / "test_cases" / "cases.json")
    report = EvalHarness(MockModel()).run_suite(cases)

    print("SUMMARY")
    print(json.dumps({k: report[k] for k in ["model", "total", "passed", "failed", "pass_rate"]}, indent=2))
    print("\nFAILURES")
    print(format_failures(report))


if __name__ == "__main__":
    main()

