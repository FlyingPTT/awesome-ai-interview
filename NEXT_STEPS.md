# Next Expansion Plan

This file keeps the repository easy to maintain after each content burst. The goal is to add material that is useful for interviews, visible to GitHub visitors, and easy to verify with runnable examples.

## Immediate Backlog

- Extend the coding-agent mini example into a two-step repair loop: localize, patch, run tests, inspect failure, patch again.
- Add a small multimodal RAG example for document screenshots and table-heavy PDFs.
- Add a model-router evaluation report that compares cheap-first, strong-only, and cascade policies.
- Add a RAG observability note covering retrieval hit rate, citation precision, refusal quality, and latency.
- Add a paper map for multimodal models and VLM agents.

## Maintenance Cadence

1. Add one interview module or one runnable example.
2. Mirror every Markdown page in Chinese.
3. Link the new page from README, docs index, roadmap, and the weekly digest.
4. Run `bash scripts/test_examples.sh`.
5. Commit with a short, topic-focused message.

## Quality Bar

- Every example should run locally without paid APIs.
- Every project should have a resume talking point.
- Every interview note should include tradeoffs, failure modes, and production details.
- Every new topic should connect to LLM, RAG, agents, evaluation, multimodal AI, or AI engineering interviews.

## Next TODO

- Turn `examples/coding-agent-mini` into a more realistic harness with a tool registry, patch validation, and an execution sandbox.
- Add 10 coding-agent system design questions that connect the mini example to real repository automation.
- Add a lightweight HTML docs navigation section for projects, interviews, papers, and high-star repos.
