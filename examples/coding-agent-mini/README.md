# Coding Agent Mini

A dependency-light coding agent demo that repairs a toy repository in a temporary directory.

It demonstrates:

- Issue parsing.
- Code localization.
- Patch generation.
- Unified diff summary.
- Test execution.
- Verified repair output.

## Run

```bash
python3 examples/coding-agent-mini/run_demo.py
```

## Test

```bash
python3 -m unittest discover examples/coding-agent-mini/tests
```

## Interview Talking Points

- Coding agents should localize before editing.
- Patches should be scoped and reviewable.
- Tests are the strongest verifier for coding agents.
- Diff summaries and test output make the agent auditable.
- Real systems need sandboxing and permission controls.

