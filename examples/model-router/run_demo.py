from __future__ import annotations

import json

from router import answer_with_route


def main() -> None:
    tasks = [
        "Format this JSON response.",
        "Design a multi-step RAG evaluation system.",
        "Answer a legal question about a contract.",
    ]
    for task in tasks:
        print(json.dumps(answer_with_route(task), indent=2))


if __name__ == "__main__":
    main()

