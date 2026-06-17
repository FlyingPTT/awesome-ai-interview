from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from models import ModelAction, ScriptedModel
from tools import ToolRegistry


@dataclass
class AgentState:
    goal: str
    budget_remaining: int
    steps: list[dict[str, Any]] = field(default_factory=list)
    final_answer: str | None = None


class MinimalAgent:
    def __init__(self, model: ScriptedModel, tools: ToolRegistry, max_steps: int = 5) -> None:
        self.model = model
        self.tools = tools
        self.max_steps = max_steps

    def run(self, goal: str) -> AgentState:
        state = AgentState(goal=goal, budget_remaining=self.max_steps)

        while state.budget_remaining > 0 and state.final_answer is None:
            action = self.model.decide(
                goal=state.goal,
                history=state.steps,
                tools=self.tools.schemas(),
            )
            self._apply_action(state, action)
            state.budget_remaining -= 1

        if state.final_answer is None:
            state.final_answer = "Stopped because the step budget was exhausted."

        return state

    def _apply_action(self, state: AgentState, action: ModelAction) -> None:
        if action.type == "final":
            state.final_answer = action.content
            state.steps.append(
                {
                    "type": "final",
                    "thought": action.content,
                    "observation": "final answer produced",
                }
            )
            return

        if not action.tool_name or action.arguments is None:
            raise ValueError("tool action must include tool_name and arguments")

        tool = self.tools.get(action.tool_name)
        if tool.requires_approval:
            raise PermissionError(f"tool requires approval: {tool.name}")

        observation = tool.run(action.arguments)
        state.steps.append(
            {
                "type": "tool",
                "thought": action.content,
                "tool": action.tool_name,
                "arguments": action.arguments,
                "observation": observation,
            }
        )

