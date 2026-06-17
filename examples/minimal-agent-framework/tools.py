from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


class ToolValidationError(ValueError):
    pass


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    schema: dict[str, type]
    handler: Callable[..., str]
    requires_approval: bool = False

    def validate(self, arguments: dict[str, Any]) -> dict[str, Any]:
        missing = [key for key in self.schema if key not in arguments]
        if missing:
            raise ToolValidationError(f"missing required arguments: {missing}")

        extra = [key for key in arguments if key not in self.schema]
        if extra:
            raise ToolValidationError(f"unexpected arguments: {extra}")

        for key, expected_type in self.schema.items():
            if not isinstance(arguments[key], expected_type):
                raise ToolValidationError(
                    f"{key} must be {expected_type.__name__}, got {type(arguments[key]).__name__}"
                )
        return arguments

    def run(self, arguments: dict[str, Any]) -> str:
        validated = self.validate(arguments)
        return self.handler(**validated)


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        if name not in self._tools:
            raise KeyError(f"unknown tool: {name}")
        return self._tools[name]

    def schemas(self) -> list[dict[str, Any]]:
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "schema": {key: value.__name__ for key, value in tool.schema.items()},
                "requires_approval": tool.requires_approval,
            }
            for tool in self._tools.values()
        ]


DOCUMENTS = {
    "rag": "RAG systems combine retrieval, reranking, grounded generation, and evaluation.",
    "agent": "Agents use model decisions, tools, observations, memory, and stop conditions.",
    "eval": "LLM evaluation should track quality, safety, latency, cost, and regressions.",
}


def search_docs(query: str) -> str:
    matches = []
    query_lower = query.lower()
    for title, body in DOCUMENTS.items():
        if query_lower in title or query_lower in body.lower():
            matches.append(f"{title}: {body}")
    return "\n".join(matches) if matches else "no matching documents"


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if any(char not in allowed for char in expression):
        raise ToolValidationError("calculator only accepts arithmetic expressions")
    return str(eval(expression, {"__builtins__": {}}, {}))


def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(
        Tool(
            name="search_docs",
            description="Search a tiny local knowledge base.",
            schema={"query": str},
            handler=search_docs,
        )
    )
    registry.register(
        Tool(
            name="calculator",
            description="Evaluate a simple arithmetic expression.",
            schema={"expression": str},
            handler=calculator,
        )
    )
    return registry

