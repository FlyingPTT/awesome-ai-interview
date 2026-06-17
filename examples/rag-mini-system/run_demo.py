from __future__ import annotations

import json
from pathlib import Path

from rag import MiniRAG


def main() -> None:
    rag = MiniRAG.from_directory(Path(__file__).parent / "docs")
    result = rag.answer("How should RAG systems be evaluated?")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

