# Interview Skills

## Three-Layer Answer Skill

Purpose: convert a technical concept into a strong interview answer.

Output structure:

1. Short answer: one or two sentences.
2. Expanded answer: explain mechanism and tradeoffs.
3. Follow-up defense: answer likely interviewer probes.

Example topic: KV cache.

Short answer: KV cache stores previously computed keys and values during autoregressive decoding so the model does not recompute them for every generated token.

Expanded answer: It reduces repeated attention computation in decoding, improving latency, but increases memory usage. Long-context serving must carefully manage KV cache memory through batching, paging, quantization, or eviction.

Follow-up defense:

- It helps decoding more than prefill.
- It trades memory for speed.
- It becomes a major bottleneck for long-context applications.

