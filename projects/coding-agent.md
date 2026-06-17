# Project: Coding Agent

## Goal

Build an agent that can inspect a repository, localize a bug, edit code, run tests, and summarize the patch.

## Architecture

- Issue parser.
- Repository search.
- File reader.
- Patch editor.
- Test runner.
- Repair loop.
- Diff summarizer.

## Technical Highlights

- Bounded retry loop.
- Test-first diagnosis.
- File-level change constraints.
- Human approval for risky commands.
- Patch summary with verification evidence.

## Resume Bullet

Implemented a coding agent that localizes repository issues, edits code, runs targeted tests, and produces verified patch summaries with bounded repair loops and command safety controls.

