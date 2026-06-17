from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


@dataclass(frozen=True)
class ModelAction:
    type: Literal["tool", "final"]
    content: str
    tool_name: str | None = None
    arguments: dict[str, Any] | None = None


class ScriptedModel:
    """A deterministic stand-in for an LLM so the demo runs without API keys."""

    def decide(self, goal: str, history: list[dict[str, Any]], tools: list[dict[str, Any]]) -> ModelAction:
        goal_lower = goal.lower()

        if not history and any(word in goal_lower for word in ["rag", "agent", "eval"]):
            if "rag" in goal_lower:
                query = "rag"
            elif "eval" in goal_lower:
                query = "eval"
            else:
                query = "agent"
            return ModelAction(
                type="tool",
                content=f"I should search the local docs for {query}.",
                tool_name="search_docs",
                arguments={"query": query},
            )

        if not history and any(char.isdigit() for char in goal):
            return ModelAction(
                type="tool",
                content="I should calculate the numeric part.",
                tool_name="calculator",
                arguments={"expression": "2 + 3 * 4"},
            )

        observations = [step["observation"] for step in history]
        joined = "\n".join(observations)
        return ModelAction(
            type="final",
            content=f"Final answer based on observations:\n{joined}",
        )

