from __future__ import annotations

import json
import argparse
from pathlib import Path

from harness import EvalHarness, format_failures, load_cases, save_report
from model import MockModel


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local LLM evaluation harness demo.")
    parser.add_argument("--report", type=Path, default=None, help="Optional path to write JSON report.")
    args = parser.parse_args()

    root = Path(__file__).parent
    cases = load_cases(root / "test_cases" / "cases.json")
    report = EvalHarness(MockModel()).run_suite(cases)

    print("SUMMARY")
    print(json.dumps({k: report[k] for k in ["model", "total", "passed", "failed", "pass_rate"]}, indent=2))
    print("\nFAILURES")
    print(format_failures(report))
    if args.report:
        save_report(report, args.report)
        print(f"\nReport written to {args.report}")


if __name__ == "__main__":
    main()
