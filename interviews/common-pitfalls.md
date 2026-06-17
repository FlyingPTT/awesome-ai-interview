# Common AI Interview Pitfalls

This page summarizes common mistakes candidates make in LLM, RAG, AI agent, and AI engineering interviews.

## 1. Only Memorizing Transformer Basics

Weak answer:

- Explains attention formulas but cannot discuss inference, serving, evaluation, or product tradeoffs.

Better answer:

- Explain the mechanism, then connect it to KV cache, latency, long context, and system design.

## 2. Treating RAG As "Just A Vector Database"

Weak answer:

- Says RAG means embedding documents into a vector database.

Better answer:

- Discuss parsing, chunking, hybrid retrieval, reranking, prompt construction, citations, refusal, evaluation, and monitoring.

## 3. Ignoring Evaluation

Weak answer:

- Says "we can ask users if the answer is good."

Better answer:

- Define offline datasets, golden cases, rubrics, component metrics, human review, and regression gates.

## 4. Mixing Up Fine-Tuning And RAG

Weak answer:

- Says fine-tuning is always better because it teaches the model domain knowledge.

Better answer:

- Fine-tuning changes behavior, style, or task policy. RAG is better for changing, auditable, permissioned knowledge.

## 5. Saying Agents Are Just ReAct

Weak answer:

- Explains thought-action-observation but misses production concerns.

Better answer:

- Discuss tool schemas, state, memory, verifier, stop conditions, permissions, audit logs, and human approval.

## 6. Not Understanding Tool Safety

Weak answer:

- Lets the model freely call any tool.

Better answer:

- Use least privilege, schema validation, dry-run mode, approval for risky actions, and logs.

## 7. Overusing LLM-As-A-Judge

Weak answer:

- Uses an LLM judge for every metric without calibration.

Better answer:

- Use deterministic checks when possible, calibrate judges against human labels, and track bias.

## 8. Not Separating Retrieval And Generation Failures

Weak answer:

- When RAG output is wrong, only tweaks the prompt.

Better answer:

- First check whether correct evidence was retrieved. Then inspect generation, citation, and refusal behavior.

## 9. Ignoring Latency And Cost

Weak answer:

- Picks the strongest model for every task.

Better answer:

- Discuss model routing, caching, batching, prompt length, streaming, quantization, and success-cost metrics.

## 10. Giving Project Descriptions Without Metrics

Weak answer:

- "I built a RAG chatbot."

Better answer:

- "I built a RAG system with hybrid retrieval, reranking, citation tracking, and evaluation metrics for recall, faithfulness, latency, and cost."

## 11. Not Knowing Failure Modes

Weak answer:

- Only describes the happy path.

Better answer:

- Discuss hallucination, stale documents, permission bugs, prompt injection, tool errors, infinite loops, and evaluation leakage.

## 12. Confusing Demos With Production Systems

Weak answer:

- Shows a working demo but cannot explain release readiness.

Better answer:

- Explain evaluation, monitoring, access control, rollback, human review, and cost budgets.

## Quick Self-Check

- Can you explain the mechanism?
- Can you explain tradeoffs?
- Can you design evaluation?
- Can you debug failures?
- Can you discuss production constraints?
- Can you turn the topic into a resume project?

