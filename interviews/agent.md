# AI Agent Interview Notes

## Agent System Design Template

A strong answer should cover:

1. User goal and task boundary.
2. Available tools and permissions.
3. State representation.
4. Planning strategy.
5. Execution loop.
6. Failure handling.
7. Verification.
8. Logging and observability.
9. Evaluation.
10. Security and governance.

## Example: Coding Agent

### Goal

Build an agent that can take a GitHub issue, inspect the codebase, implement a fix, run tests, and open a pull request.

### Components

- Repository reader.
- Search tool.
- Code editor.
- Shell executor.
- Test runner.
- Diff summarizer.
- Review loop.

### Failure Handling

- If tests fail, summarize failing cases and attempt a bounded repair loop.
- If a command needs external access, request approval.
- If requirements are ambiguous, ask a clarifying question.
- If the diff touches unrelated files, stop and explain.

### Evaluation

- Issue resolution rate.
- Test pass rate.
- Human edit distance after agent submission.
- Time to first working patch.
- Regression rate.

## Common Questions

### How is an agent different from a chatbot?

A chatbot mainly responds with text. An agent can use tools, update external state, decompose tasks, and verify progress toward a goal.

### Why are agents hard to evaluate?

Agent tasks often have multiple valid paths, external side effects, changing environments, and partial success states. Evaluation should combine task success, safety, cost, latency, and human review.

### How do you make agents safer?

Use least-privilege tools, explicit approvals for risky actions, sandboxing, audit logs, idempotent operations, dry-run modes, and bounded execution loops.

