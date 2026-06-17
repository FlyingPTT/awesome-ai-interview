# Agent Skills Catalog

This catalog collects reusable AI agent skills. Each skill is written as a practical workflow that can be turned into a prompt, system instruction, or `SKILL.md` package.

## Skill Design Principles

- Keep the skill narrow.
- Define inputs and outputs.
- Specify allowed tools.
- Make verification explicit.
- Add failure handling.
- Prefer structured outputs.
- Avoid hidden side effects.

## 1. Paper Reading Skill

Purpose: turn a research paper into structured study notes.

Inputs:

- Paper title, URL, or PDF.
- Target topic or role.

Workflow:

1. Extract metadata.
2. Identify the problem.
3. Summarize the method.
4. Extract key equations or algorithms.
5. Summarize experiments.
6. Identify limitations.
7. Generate interview questions.

Output:

- One-sentence summary.
- Method breakdown.
- Strengths and limitations.
- Implementation notes.
- Interview talking points.

## 2. Literature Survey Skill

Purpose: build a topic map from multiple papers.

Workflow:

1. Collect candidate papers.
2. Group by problem.
3. Group by method family.
4. Build a timeline.
5. Identify representative papers.
6. Extract open problems.

Output:

- Taxonomy.
- Paper table.
- Reading order.
- Trend summary.
- Open problems.

## 3. RAG Diagnosis Skill

Purpose: identify why a RAG answer is wrong.

Workflow:

1. Check whether correct evidence was retrieved.
2. If not, inspect parsing, chunking, embeddings, filters, and query rewriting.
3. If yes, inspect prompt, context ordering, citations, and refusal logic.
4. Create a regression case.

Output:

- Failure category.
- Evidence.
- Likely root cause.
- Fix plan.
- Regression test.

## 4. Coding Repair Skill

Purpose: fix a bug or failing test in a codebase.

Workflow:

1. Reproduce the failure.
2. Search for relevant code.
3. Read local patterns.
4. Implement a scoped fix.
5. Run focused tests.
6. Summarize diff and verification.

Quality bar:

- Do not overwrite unrelated user changes.
- Do not broaden scope without reason.
- Report tests that were not run.

## 5. Code Review Skill

Purpose: review a patch for bugs, regressions, and missing tests.

Workflow:

1. Inspect diff.
2. Identify changed behavior.
3. Look for correctness, security, performance, and test risks.
4. Prioritize findings.
5. Provide file and line references.

Output:

- Findings first.
- Open questions.
- Brief summary.

## 6. Interview Answer Skill

Purpose: convert a technical topic into a strong interview answer.

Workflow:

1. Write a one-sentence answer.
2. Explain mechanism.
3. Discuss tradeoffs.
4. Add a concrete example.
5. Prepare follow-up answers.

Output:

- Short answer.
- Expanded answer.
- Follow-up questions.
- Common pitfalls.

## 7. Hot Topic Tracker Skill

Purpose: convert fast-moving AI trends into study notes.

Workflow:

1. Collect model releases, papers, frameworks, and product changes.
2. Group by theme.
3. Identify why each item matters.
4. Extract interview questions.
5. Extract project ideas.

Output:

- Weekly trend digest.
- Interview talking points.
- Project opportunities.

## 8. Resume Project Generator Skill

Purpose: turn a technical topic into a resume-ready project.

Workflow:

1. Choose a realistic user problem.
2. Design a minimal architecture.
3. Identify non-trivial tradeoffs.
4. Define evaluation metrics.
5. Write resume bullets.
6. Prepare interview talking points.

Output:

- Project idea.
- Architecture.
- Milestones.
- Metrics.
- Resume bullet.

## 9. Evaluation Builder Skill

Purpose: design an evaluation plan for an LLM, RAG, or agent system.

Workflow:

1. Define success criteria.
2. Create representative test cases.
3. Add edge and adversarial cases.
4. Choose metrics.
5. Decide human review policy.
6. Set regression thresholds.

Output:

- Dataset plan.
- Metrics.
- Rubric.
- Regression policy.

## 10. System Design Drill Skill

Purpose: prepare for AI system design interviews.

Workflow:

1. Clarify product requirements.
2. Define constraints.
3. Sketch architecture.
4. Discuss data flow.
5. Discuss evaluation.
6. Discuss reliability, cost, safety, and monitoring.

Output:

- Design outline.
- Key tradeoffs.
- Failure modes.
- Evaluation plan.

