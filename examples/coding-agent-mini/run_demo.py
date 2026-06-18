from __future__ import annotations

import json
import tempfile
from pathlib import Path

from agent import MiniCodingAgent, create_toy_repo


def main() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = Path(tmpdir) / "toy-repo"
        create_toy_repo(repo)
        result = MiniCodingAgent(repo).repair("Fix add(a, b), which currently fails test_add.")
        print(
            json.dumps(
                {
                    "issue": result.issue,
                    "changed_file": result.changed_file,
                    "tests_passed": result.tests_passed,
                    "summary": result.summary,
                    "diff": result.diff,
                },
                indent=2,
            )
        )


if __name__ == "__main__":
    main()

