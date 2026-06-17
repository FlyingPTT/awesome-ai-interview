from __future__ import annotations

import json

from agent import MinimalAgent
from models import ScriptedModel
from tools import build_default_registry


def main() -> None:
    agent = MinimalAgent(
        model=ScriptedModel(),
        tools=build_default_registry(),
        max_steps=4,
    )
    state = agent.run("Explain what an agent is using the local docs.")

    print("FINAL ANSWER")
    print(state.final_answer)
    print("\nTRAJECTORY")
    print(json.dumps(state.steps, indent=2))


if __name__ == "__main__":
    main()

