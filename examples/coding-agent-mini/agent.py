from __future__ import annotations

import difflib
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RepairResult:
    issue: str
    changed_file: str
    diff: str
    tests_passed: bool
    test_output: str
    summary: str


def create_toy_repo(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "calculator.py").write_text(
        "def add(a, b):\n"
        "    return a - b\n",
        encoding="utf-8",
    )
    (root / "test_calculator.py").write_text(
        "from calculator import add\n\n"
        "def test_add():\n"
        "    assert add(2, 3) == 5\n",
        encoding="utf-8",
    )


class MiniCodingAgent:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root

    def repair(self, issue: str) -> RepairResult:
        candidate = self._localize(issue)
        before = candidate.read_text(encoding="utf-8")
        after = self._patch(before)
        candidate.write_text(after, encoding="utf-8")
        diff = self._diff(candidate.name, before, after)
        tests_passed, test_output = self._run_tests()
        return RepairResult(
            issue=issue,
            changed_file=candidate.name,
            diff=diff,
            tests_passed=tests_passed,
            test_output=test_output,
            summary=(
                "Changed add(a, b) to return a + b and verified with a deterministic smoke test."
                if tests_passed
                else "Applied patch but tests still failed."
            ),
        )

    def _localize(self, issue: str) -> Path:
        for path in self.repo_root.glob("*.py"):
            if path.name.startswith("test_"):
                continue
            text = path.read_text(encoding="utf-8")
            if "def add" in text:
                return path
        raise FileNotFoundError("could not localize add implementation")

    def _patch(self, text: str) -> str:
        if "return a - b" not in text:
            raise ValueError("expected buggy implementation was not found")
        return text.replace("return a - b", "return a + b")

    def _run_tests(self) -> tuple[bool, str]:
        completed = subprocess.run(
            ["python3", "-c", "from calculator import add; assert add(2, 3) == 5"],
            cwd=self.repo_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        output = completed.stdout or "smoke test passed"
        return completed.returncode == 0, output

    def _diff(self, filename: str, before: str, after: str) -> str:
        return "".join(
            difflib.unified_diff(
                before.splitlines(keepends=True),
                after.splitlines(keepends=True),
                fromfile=f"a/{filename}",
                tofile=f"b/{filename}",
            )
        )
