# AI Agent Engineer Roadmap

AI agent engineering focuses on building systems that can plan, use tools, remember context, recover from failures, and complete tasks with bounded autonomy.

## Mental Model

An agent system usually contains:

- Model: the reasoning and language interface.
- Tools: external capabilities such as search, code execution, databases, browsers, and APIs.
- Planner: decomposes goals into executable steps.
- Executor: performs tool calls and updates state.
- Memory: stores useful information across turns or tasks.
- Verifier: checks outputs, constraints, and task completion.
- Guardrails: define permissions, safety, and operational boundaries.

## Core Topics

### Tool Use

- Function calling schema design.
- Tool selection.
- Tool result summarization.
- Idempotency and retries.
- Permission and sandbox design.

### Planning

- ReAct.
- Plan-and-execute.
- Reflection.
- Tree search.
- Task decomposition.
- Long-running task management.

### Memory

- Short-term conversation state.
- Long-term vector memory.
- Episodic memory.
- User preference memory.
- Memory retrieval and forgetting.

### Evaluation

- Task success rate.
- Tool-call accuracy.
- Human intervention rate.
- Cost per task.
- Latency per task.
- Recovery after failed tool calls.

## Common Failure Modes

- Tool call hallucination.
- Incorrect tool argument construction.
- Context pollution.
- Infinite planning loops.
- Hidden state drift.
- Over-permissioned tools.
- Evaluation leakage.

## Interview Prompts

- Design an agent that can debug a failing CI pipeline.
- Design a research assistant that reads papers and builds a literature map.
- How would you prevent an agent from deleting production data?
- How do you evaluate an agent if there is no single correct answer?
- How do you make a coding agent trustworthy enough for enterprise use?

