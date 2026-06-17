# Project: Minimal Agent Framework

## Goal

Build a small agent framework from scratch to understand how models are scheduled to follow instructions, call tools, observe results, update state, and stop safely.

This project is useful in interviews because it demonstrates the mechanics behind agent frameworks rather than only using a library.

Runnable example: [examples/minimal-agent-framework](../examples/minimal-agent-framework/).

## What The Framework Should Do

- Accept a user goal.
- Maintain explicit agent state.
- Choose tools through model output.
- Validate tool arguments.
- Execute tools.
- Feed observations back to the model.
- Stop when the task is complete or a budget is reached.
- Produce an auditable trajectory.

## Architecture

```text
user goal
   |
   v
agent loop
   |
   +--> planner/model call
   |
   +--> tool router
   |
   +--> tool executor
   |
   +--> observation store
   |
   +--> verifier / stop condition
   |
   v
final answer + trajectory log
```

## Core Abstractions

### Tool

```python
class Tool:
    name: str
    description: str
    schema: dict

    def run(self, **kwargs):
        raise NotImplementedError
```

### Agent State

```python
class AgentState:
    goal: str
    steps: list
    observations: list
    budget_remaining: int
    final_answer: str | None
```

### Agent Step

```json
{
  "thought": "I need to inspect the file list first.",
  "tool": "search_files",
  "arguments": {"query": "README"},
  "observation": "README.md found",
  "status": "completed"
}
```

## Minimal Agent Loop

```python
while not done and state.budget_remaining > 0:
    action = model.decide(
        goal=state.goal,
        history=state.steps,
        tools=tool_registry.schemas(),
    )

    if action.type == "final":
        state.final_answer = action.content
        break

    tool = tool_registry.get(action.tool_name)
    args = validate(action.arguments, tool.schema)
    observation = tool.run(**args)
    state.steps.append({
        "action": action,
        "observation": observation,
    })
    state.budget_remaining -= 1
```

## Safety Controls

- Tool schema validation.
- Step limit.
- Cost and time budget.
- Human approval for risky tools.
- Dry-run mode.
- Audit log.
- Permission-scoped tool registry.
- Explicit final verification.

## Tool Examples

- `search_files(query)`.
- `read_file(path)`.
- `write_patch(path, diff)`.
- `run_tests(command)`.
- `web_search(query)`.
- `calculator(expression)`.
- `ask_human(question)`.

## Interview Talking Points

- Agent reliability often depends more on tool design and control flow than raw model intelligence.
- The agent loop should expose state and trajectory for debugging.
- Dangerous actions should be deterministic, validated, and permissioned.
- Stop conditions are as important as planning.
- A small deterministic workflow is often better than a fully autonomous agent.

## Common Follow-Up Questions

- How do you prevent infinite loops?
- How do you validate tool arguments?
- How do you resume a long-running task?
- How do you evaluate trajectory quality?
- How do you handle prompt injection from tool outputs?

## Resume Bullet

Implemented a minimal agent framework with explicit state, tool registry, schema validation, iterative model-tool-observation loop, budgeted execution, human approval hooks, and trajectory logging for debuggable AI workflows.
