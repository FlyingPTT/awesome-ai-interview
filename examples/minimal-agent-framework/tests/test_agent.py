from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agent import MinimalAgent
from models import ModelAction, ScriptedModel
from tools import Tool, ToolRegistry, ToolValidationError, build_default_registry, calculator


class LoopingModel(ScriptedModel):
    def decide(self, goal, history, tools):
        return ModelAction(
            type="tool",
            content="keep searching",
            tool_name="search_docs",
            arguments={"query": "agent"},
        )


class UnknownToolModel(ScriptedModel):
    def decide(self, goal, history, tools):
        return ModelAction(
            type="tool",
            content="call missing tool",
            tool_name="missing_tool",
            arguments={},
        )


class MinimalAgentTests(unittest.TestCase):
    def test_agent_produces_trajectory(self):
        agent = MinimalAgent(ScriptedModel(), build_default_registry(), max_steps=4)
        state = agent.run("Explain agent from local docs")

        self.assertIn("Final answer", state.final_answer)
        self.assertEqual(state.steps[0]["tool"], "search_docs")
        self.assertEqual(state.steps[-1]["type"], "final")

    def test_budget_stop(self):
        agent = MinimalAgent(LoopingModel(), build_default_registry(), max_steps=1)
        state = agent.run("loop forever")

        self.assertEqual(state.final_answer, "Stopped because the step budget was exhausted.")
        self.assertEqual(len(state.steps), 1)

    def test_unknown_tool_raises(self):
        agent = MinimalAgent(UnknownToolModel(), build_default_registry(), max_steps=1)

        with self.assertRaises(KeyError):
            agent.run("call missing tool")

    def test_tool_validation_rejects_missing_argument(self):
        registry = build_default_registry()
        tool = registry.get("search_docs")

        with self.assertRaises(ToolValidationError):
            tool.run({})

    def test_calculator_rejects_unsafe_expression(self):
        with self.assertRaises(ToolValidationError):
            calculator("__import__('os').system('echo bad')")

    def test_approval_tool_raises_permission_error(self):
        registry = ToolRegistry()
        registry.register(
            Tool(
                name="delete_file",
                description="Dangerous delete operation.",
                schema={"path": str},
                handler=lambda path: f"deleted {path}",
                requires_approval=True,
            )
        )

        class ApprovalModel(ScriptedModel):
            def decide(self, goal, history, tools):
                return ModelAction(
                    type="tool",
                    content="delete file",
                    tool_name="delete_file",
                    arguments={"path": "important.txt"},
                )

        agent = MinimalAgent(ApprovalModel(), registry, max_steps=1)
        with self.assertRaises(PermissionError):
            agent.run("delete a file")


if __name__ == "__main__":
    unittest.main()

