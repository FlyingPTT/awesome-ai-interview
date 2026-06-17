# 50 AI Agent Interview Questions

This page collects 50 practical interview questions for AI agent engineering roles. It focuses on tool use, planning, memory, workflow orchestration, evaluation, and safety.

## Foundations

### 1. What is an AI agent?

Key points:

- An agent combines a model with tools, state, and control logic to pursue a goal.
- It can observe, plan, act, and verify progress.
- Production agents need permissions, logging, evaluation, and failure handling.

### 2. How is an agent different from a chatbot?

Key points:

- A chatbot mainly generates responses.
- An agent can call tools and update external state.
- Agents need task boundaries and safety controls.

### 3. What are the core components of an agent?

Key points:

- Model.
- Tools.
- Planner.
- Executor.
- Memory.
- State store.
- Verifier.
- Guardrails.

### 4. What is tool calling?

Key points:

- The model selects a tool and produces structured arguments.
- The system executes the tool and returns observations.
- Tool schemas and validation strongly affect reliability.

### 5. What makes agent engineering hard?

Key points:

- Non-deterministic model behavior.
- External side effects.
- Long-horizon tasks.
- Tool failures.
- Ambiguous success criteria.
- Safety and permission risks.

## Tool Use

### 6. How do you design a good tool schema?

Key points:

- Clear name and description.
- Narrow responsibility.
- Explicit required fields.
- Strong argument validation.
- Idempotent behavior when possible.

### 7. What is tool hallucination?

Key points:

- The model invents a nonexistent tool or unsupported argument.
- Mitigate with explicit tool registry, schema validation, and error feedback.

### 8. How do you handle tool errors?

Key points:

- Return structured errors.
- Let the agent retry with bounded attempts.
- Distinguish transient and permanent failures.
- Escalate when needed.

### 9. Why is least privilege important for agents?

Key points:

- Agents can make mistakes at machine speed.
- Tools should expose only necessary capabilities.
- Dangerous actions should require approval.

### 10. What is a dry-run mode?

Key points:

- Simulates an action without side effects.
- Useful for destructive, expensive, or irreversible operations.
- Lets humans review before execution.

## Planning

### 11. What is ReAct?

Key points:

- Interleaves reasoning and acting.
- The agent thinks, calls a tool, observes, and continues.
- Useful for search and tool-use tasks.

### 12. What is plan-and-execute?

Key points:

- The agent first creates a plan, then executes steps.
- Works well for long tasks.
- Needs replanning when observations change assumptions.

### 13. What is reflection?

Key points:

- The agent critiques its own output or trajectory.
- Can improve quality.
- Can also add cost and unproductive loops.

### 14. How do you prevent infinite loops?

Key points:

- Step limits.
- Time and cost budgets.
- Progress checks.
- Verifier-based termination.
- Explicit stop conditions.

### 15. How do you decompose tasks?

Key points:

- Separate information gathering, planning, action, and verification.
- Keep steps observable.
- Avoid vague tasks like "improve everything."

## Memory And State

### 16. What is short-term memory?

Key points:

- Current conversation and task state.
- Usually stored in context or state objects.
- Must be summarized when long.

### 17. What is long-term memory?

Key points:

- Persistent facts, preferences, or past task outcomes.
- Often retrieved from a database or vector store.
- Needs privacy, freshness, and forgetting policies.

### 18. What is episodic memory?

Key points:

- Stores past interactions or task trajectories.
- Useful for personalization and learning from experience.
- Can reinforce mistakes if not curated.

### 19. How do you avoid context pollution?

Key points:

- Keep tool outputs structured.
- Summarize only relevant information.
- Separate trusted instructions from untrusted content.
- Prune stale state.

### 20. How should agent state be stored?

Key points:

- Use explicit state objects for long-running workflows.
- Store tool results, plan, decisions, and checkpoints.
- Make state inspectable and recoverable.

## Workflow Orchestration

### 21. When should workflow be deterministic?

Key points:

- Use deterministic code for routing, validation, permissions, and irreversible actions.
- Use models for language understanding, synthesis, and ambiguity.

### 22. What is a state machine agent?

Key points:

- The workflow has explicit states and transitions.
- Easier to test and monitor.
- Less flexible than fully open-ended agents.

### 23. What is human-in-the-loop control?

Key points:

- Humans review or approve high-risk steps.
- The agent should provide evidence and proposed action.
- Review outcomes become feedback.

### 24. How do you resume a long-running agent task?

Key points:

- Persist state and checkpoints.
- Store completed steps and pending actions.
- Make tool calls idempotent.
- Verify external state before continuing.

### 25. How do you coordinate multi-agent workflows?

Key points:

- Assign clear roles.
- Define shared state.
- Prevent duplicated work.
- Add a coordinator or verifier.

## Evaluation

### 26. How do you evaluate an agent?

Key points:

- Task success rate.
- Tool-call accuracy.
- Recovery rate.
- Human intervention rate.
- Safety violations.
- Cost and latency.

### 27. Why is final answer evaluation insufficient?

Key points:

- Agents can reach correct answers through unsafe paths.
- Tool misuse may be hidden.
- Partial failures matter.
- Side effects must be audited.

### 28. What is trajectory evaluation?

Key points:

- Evaluates the sequence of actions, observations, and decisions.
- Useful for diagnosing planning and tool errors.
- More informative than final output alone.

### 29. How do you build agent benchmarks?

Key points:

- Use realistic tasks.
- Provide controlled tools and environments.
- Define success criteria.
- Include failure and recovery cases.

### 30. What metrics matter for coding agents?

Key points:

- Issue resolution rate.
- Test pass rate.
- Patch correctness.
- Human edit distance.
- Regression rate.
- Time to working patch.

## Safety And Security

### 31. What is prompt injection in agent systems?

Key points:

- Untrusted content tries to override instructions.
- Dangerous when agents can browse, retrieve, or call tools.
- Mitigate with instruction hierarchy and tool constraints.

### 32. How do you isolate untrusted content?

Key points:

- Mark retrieved or browsed content as data.
- Do not treat it as instructions.
- Sanitize and validate outputs before tool use.

### 33. How do you protect secrets?

Key points:

- Do not expose secrets to prompts unless necessary.
- Use scoped credentials.
- Redact logs.
- Prevent tool outputs from leaking sensitive data.

### 34. How do you control destructive actions?

Key points:

- Require approval.
- Use dry-run.
- Show diff or impact summary.
- Make rollback possible.

### 35. How do you audit agent behavior?

Key points:

- Log prompts, tool calls, arguments, outputs, approvals, and final results.
- Keep logs searchable.
- Protect sensitive data in logs.

## Coding Agents

### 36. Design a coding agent.

Key points:

- Read issue.
- Search repository.
- Inspect relevant files.
- Edit narrowly.
- Run tests.
- Repair if needed.
- Summarize diff and verification.

### 37. How should a coding agent handle user changes?

Key points:

- Detect dirty worktree.
- Avoid overwriting unrelated changes.
- Explain conflicts.
- Work with existing edits when relevant.

### 38. How should a coding agent choose tests?

Key points:

- Start with focused tests.
- Run broader tests when shared behavior changes.
- Report tests not run.
- Use failures to guide repair.

### 39. How do you prevent broad, risky edits?

Key points:

- Read local patterns first.
- Keep changes scoped.
- Add abstractions only when justified.
- Review diff before finalizing.

### 40. What makes a coding agent enterprise-ready?

Key points:

- Permission model.
- Audit logs.
- Policy checks.
- Test integration.
- Code review workflow.
- Repository-specific instructions.

## Research And Productivity Agents

### 41. Design a paper reading agent.

Key points:

- Parse PDF.
- Extract problem, method, experiments, limitations.
- Build citation links.
- Generate study notes and interview questions.

### 42. Design a literature survey agent.

Key points:

- Search papers.
- Cluster by topic.
- Track chronology.
- Compare methods.
- Identify open problems.

### 43. Design a data analysis agent.

Key points:

- Inspect schema.
- Generate hypotheses.
- Run code.
- Validate results.
- Produce reproducible notebooks or reports.

### 44. Design a browser agent.

Key points:

- Navigate pages.
- Extract information.
- Avoid untrusted instructions.
- Verify important facts.
- Handle dynamic pages.

### 45. Design a personal productivity agent.

Key points:

- Calendar, email, task tools.
- Strong permissions.
- Confirmation for external messages.
- Preference memory.
- Audit trail.

## Production Readiness

### 46. How do you decide which tasks should be agentic?

Key points:

- Agentic tasks involve uncertainty, tools, and multi-step decisions.
- Simple deterministic tasks should stay deterministic.
- High-risk tasks need stronger controls.

### 47. How do you reduce agent cost?

Key points:

- Use smaller models for simple steps.
- Cache tool results.
- Limit reflection.
- Reduce context.
- Stop early when success is verified.

### 48. How do you reduce agent latency?

Key points:

- Parallelize independent tool calls.
- Use deterministic routing.
- Avoid unnecessary planning.
- Stream intermediate progress.

### 49. What should an agent report at the end?

Key points:

- What changed.
- Evidence of verification.
- Known limitations.
- Unrun tests or unresolved risks.
- Next recommended step.

### 50. How do you know an agent is production-ready?

Key points:

- Reliable task success.
- Bounded failures.
- Safe tool permissions.
- Evaluation suite.
- Monitoring and audit logs.
- Human escalation path.

