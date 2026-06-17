# LLM Agents Paper Map

This page tracks papers and concepts useful for understanding AI agents, tool use, planning, reflection, and multi-agent systems.

## Core Questions

- How can language models use tools?
- How should agents plan and revise plans?
- How can agents verify progress?
- What should be deterministic workflow logic versus model-driven autonomy?
- How do we evaluate agent trajectories?

## Reading Order

### 1. Tool Use

Study:

- Tool-augmented language models.
- Function calling.
- Program-aided reasoning.
- Retrieval and browsing tools.

Interview takeaway:

- Tool use turns language models into systems. Tool schema design, validation, and permissions become part of model quality.

### 2. Reasoning And Acting

Study:

- ReAct-style reasoning and acting.
- Plan-and-execute agents.
- Reflection and self-critique.
- Verifier-guided execution.

Interview takeaway:

- Planning is useful, but open-ended loops need budgets, state, and stop conditions.

### 3. Multi-Agent Systems

Study:

- Role-based collaboration.
- Debate and critique.
- Coordinator-worker patterns.
- Human-in-the-loop workflows.

Interview takeaway:

- Multi-agent systems can improve decomposition, but add coordination cost and failure modes.

### 4. Coding Agents

Study:

- SWE-bench style tasks.
- Repository exploration.
- Patch generation.
- Test-based repair loops.

Interview takeaway:

- Coding agents should be evaluated by issue resolution, test pass rate, regression risk, and human edit distance.

## Implementation Notes

- Keep agent state explicit.
- Store trajectory logs.
- Validate tool arguments.
- Require approval for risky actions.
- Separate trusted instructions from untrusted content.

## Interview Questions

- How is an agent different from a chatbot?
- How do you prevent infinite loops?
- How do you evaluate an agent trajectory?
- What makes a coding agent safe?
- When is a deterministic workflow better than an agent?

