# Coding Agent Skills

## Repository Repair Skill

Purpose: fix a failing test or issue in an existing codebase.

Workflow:

1. Inspect the failing command or issue.
2. Search for relevant files.
3. Read local conventions.
4. Implement the smallest reasonable fix.
5. Run focused tests.
6. Summarize the diff and verification.

Quality bar:

- Do not rewrite unrelated code.
- Do not silently ignore failing tests.
- Do not overwrite user changes.
- Explain remaining risk.

## Code Review Skill

Purpose: review a patch for bugs and regressions.

Workflow:

1. Inspect the diff.
2. Identify changed behavior.
3. Look for correctness, security, performance, and test gaps.
4. Prioritize findings by severity.
5. Provide file and line references.

Output:

- Findings first.
- Open questions.
- Short summary.

