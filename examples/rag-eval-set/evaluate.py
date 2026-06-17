from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

RAG_ROOT = Path(__file__).resolve().parents[1] / "rag-mini-system"
sys.path.insert(0, str(RAG_ROOT))

from rag import MiniRAG


def load_cases(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_case(rag: MiniRAG, case: dict[str, Any]) -> dict[str, Any]:
    result = rag.answer(case["question"])
    checks = []

    if case["expected_behavior"] == "refuse":
        passed = not result["citations"] and "not have enough evidence" in result["answer"]
        checks.append({"name": "refusal", "passed": passed})
    else:
        citations = result["citations"]
        retrieved = result["retrieved"]
        expected_doc_id = case.get("expected_doc_id")
        cited_doc_ids = {citation["doc_id"] for citation in citations}
        retrieved_doc_ids = {item["doc_id"] for item in retrieved}
        answer_lower = result["answer"].lower()
        missing_keywords = [
            keyword for keyword in case.get("expected_keywords", []) if keyword.lower() not in answer_lower
        ]
        checks.extend(
            [
                {"name": "has_citation", "passed": bool(citations)},
                {"name": "cites_expected_doc", "passed": expected_doc_id in cited_doc_ids},
                {"name": "retrieves_expected_doc", "passed": expected_doc_id in retrieved_doc_ids},
                {"name": "keyword_coverage", "passed": not missing_keywords, "missing": missing_keywords},
            ]
        )

    return {
        "case_id": case["id"],
        "question": case["question"],
        "answer": result["answer"],
        "citations": result["citations"],
        "retrieved": result["retrieved"],
        "checks": checks,
        "passed": all(check["passed"] for check in checks),
    }


def run_eval(cases_path: Path, report_path: Path | None = None) -> dict[str, Any]:
    rag = MiniRAG.from_directory(RAG_ROOT / "docs")
    cases = load_cases(cases_path)
    results = [evaluate_case(rag, case) for case in cases]
    passed = sum(1 for result in results if result["passed"])
    report = {
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "pass_rate": round(passed / len(results), 3) if results else 0,
        "cases": results,
    }
    if report_path:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the RAG mini system.")
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path(__file__).parent / "test_cases" / "cases.json",
    )
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    report = run_eval(args.cases, args.report)
    print(json.dumps({k: report[k] for k in ["total", "passed", "failed", "pass_rate"]}, indent=2))
    if args.report:
        print(f"Report written to {args.report}")


if __name__ == "__main__":
    main()

