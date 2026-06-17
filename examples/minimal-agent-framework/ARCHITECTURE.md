# Minimal Agent Framework Architecture

This example is intentionally small, but it models the core control loop used by larger agent frameworks.

## Control Flow

```text
goal
  |
  v
AgentState
  |
  v
ScriptedModel.decide(...)
  |
  +-- final answer -> stop
  |
  +-- tool action -> ToolRegistry.get(...)
                    |
                    v
              Tool.validate(...)
                    |
                    v
              Tool.run(...)
                    |
                    v
              observation appended to state.steps
                    |
                    v
              continue until final answer or step budget exhausted
```

## Core Components

### `AgentState`

Stores the current goal, remaining step budget, tool trajectory, and final answer.

Why it matters:

- Makes the agent inspectable.
- Makes long-running tasks resumable.
- Makes evaluation possible because the trajectory is explicit.

### `ScriptedModel`

A deterministic stand-in for an LLM. It decides whether to call a tool or produce a final answer.

Why it matters:

- Keeps the example runnable without API keys.
- Shows the expected shape of model actions.
- Can be replaced by a real model client later.

### `ToolRegistry`

Stores available tools and exposes schemas to the model.

Why it matters:

- Prevents calling unknown tools.
- Keeps tool descriptions and validation in one place.
- Supports permission metadata such as `requires_approval`.

### `Tool`

Wraps a handler with a name, description, argument schema, and approval flag.

Why it matters:

- Tool schema validation catches bad model arguments before side effects happen.
- Approval flags create a hook for human-in-the-loop control.

## State Transitions

| State | Event | Next State |
| --- | --- | --- |
| Running | Model returns tool action | Validate and run tool |
| Running | Tool returns observation | Append step and continue |
| Running | Model returns final answer | Stop |
| Running | Budget reaches zero | Stop with budget message |
| Running | Tool requires approval | Raise permission error |
| Running | Tool validation fails | Raise validation error |

## Failure Modes

- Unknown tool name.
- Missing or extra tool arguments.
- Wrong argument type.
- Dangerous tool requiring approval.
- Step budget exhausted.
- Unsafe tool implementation.

## Interview Talking Points

- Agent frameworks are orchestration systems around model calls.
- Explicit state is the difference between a demo and a debuggable workflow.
- Tool schemas are part of the safety boundary.
- Stop conditions prevent runaway autonomy.
- Deterministic workflow logic should guard risky actions.

