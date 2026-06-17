# RAG Diagnosis Skills

## RAG Failure Diagnosis Skill

Purpose: diagnose why a RAG answer is wrong.

Workflow:

1. Check whether the answer is supported by retrieved context.
2. If not supported, inspect retrieval.
3. If supported but wrong, inspect generation.
4. If retrieval is unstable, inspect indexing and metadata.
5. If the answer should refuse, inspect refusal policy.

Diagnosis table:

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| Relevant document missing | Bad chunking, weak query, wrong filter | Improve chunking, query rewrite, hybrid retrieval |
| Relevant document retrieved but ignored | Prompt issue, context order | Improve prompt and context formatting |
| Answer cites wrong source | Citation mapping bug | Track source ids through the full pipeline |
| Slow response | Too many candidates, expensive rerank | Cache, reduce candidate count, optimize model |

