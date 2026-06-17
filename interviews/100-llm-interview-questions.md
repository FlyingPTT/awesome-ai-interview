# 100 LLM Interview Questions

This page collects 100 high-frequency interview questions for LLM, RAG, AI agent, and applied AI engineer roles.

Use it as:

- A study checklist.
- A mock interview question bank.
- A roadmap for deeper notes.
- A source of resume project talking points.

## How To Answer

For each question, try to answer in three layers:

1. Short answer: one or two sentences.
2. Expanded answer: mechanism, tradeoffs, and examples.
3. Follow-up defense: likely interviewer probes.

## Transformer And Attention

### 1. What problem does self-attention solve?

Short answer: self-attention lets each token dynamically gather information from other tokens in the same sequence.

Expanded answer: Instead of compressing all previous context into a fixed hidden state, self-attention computes token-to-token relevance using query, key, and value projections. This enables parallel computation and flexible long-range dependency modeling.

Follow-up questions:

- Why is attention more parallelizable than RNNs?
- What is the difference between self-attention and cross-attention?
- Why does attention become expensive for long context?

### 2. Why do we divide attention scores by the square root of the key dimension?

Short answer: scaling prevents dot products from becoming too large and pushing softmax into saturated regions.

Expanded answer: If query and key vectors have large dimensions, their dot products can have high variance. Large logits make softmax overly peaked, causing unstable gradients. Dividing by `sqrt(d_k)` stabilizes training.

Follow-up questions:

- What happens if this scaling is removed?
- Does scaling affect inference?

### 3. What is multi-head attention?

Short answer: multi-head attention runs several attention operations in parallel so the model can capture different relation types.

Expanded answer: Each head has separate projections for queries, keys, and values. Different heads can specialize in local patterns, syntax, entity tracking, or long-range dependencies. The head outputs are concatenated and projected back to the model dimension.

Follow-up questions:

- Does increasing the number of heads always improve performance?
- What is the tradeoff between head count and head dimension?

### 4. What is positional encoding and why is it needed?

Short answer: positional encoding injects token order information into attention-based models.

Expanded answer: Vanilla self-attention is permutation-invariant; it does not know token order by itself. Positional information can be added through absolute embeddings, relative position bias, RoPE, or ALiBi. Different approaches affect extrapolation to longer context.

Follow-up questions:

- Compare absolute position embeddings and RoPE.
- Why do long-context models care about positional encoding?

### 5. What is the difference between encoder-only, decoder-only, and encoder-decoder models?

Short answer: encoder-only models are strong for understanding, decoder-only models are strong for generation, and encoder-decoder models are strong for sequence-to-sequence tasks.

Expanded answer: Encoder-only models such as BERT use bidirectional attention. Decoder-only models such as GPT use causal attention for autoregressive generation. Encoder-decoder models such as T5 encode input bidirectionally and decode output autoregressively.

Follow-up questions:

- Why are most modern general-purpose LLMs decoder-only?
- When would an encoder-decoder model still be useful?

### 6. What is causal masking?

Key points:

- Prevents a token from attending to future tokens during autoregressive training and decoding.
- Makes next-token prediction consistent with generation.
- Implemented by masking attention scores above the diagonal before softmax.

Common pitfall: saying causal masking is only an inference trick. It is used during training too.

### 7. What is layer normalization?

Key points:

- Normalizes hidden activations across feature dimensions.
- Stabilizes deep network training.
- Pre-norm Transformers are usually easier to train at scale than post-norm Transformers.

Follow-up: compare pre-norm and post-norm residual blocks.

### 8. What is the role of the feed-forward network in a Transformer block?

Key points:

- Applies token-wise nonlinear transformation after attention mixing.
- Often has a much larger hidden dimension than the model dimension.
- Modern LLMs often use gated variants such as SwiGLU.

### 9. Why are residual connections important?

Key points:

- Improve gradient flow.
- Make very deep models trainable.
- Let layers learn refinements rather than full transformations.

### 10. What is the computational complexity of attention?

Key points:

- Standard full attention is `O(n^2)` in sequence length for attention scores.
- KV cache changes generation cost but not the memory pressure of long contexts.
- Long-context systems use sparse attention, sliding windows, retrieval, compression, or memory mechanisms.

## Training And Alignment

### 11. What is the standard pretraining objective for decoder-only LLMs?

Short answer: next-token prediction.

Expanded answer: The model is trained to predict the next token given previous tokens. This simple objective scales well with large datasets and produces models that can generate coherent text, follow patterns, and learn broad world and language knowledge from data.

Follow-up questions:

- Why does next-token prediction lead to broad capabilities?
- What are its limitations?

### 12. What is instruction tuning?

Short answer: instruction tuning trains a pretrained model on instruction-response examples so it better follows user requests.

Expanded answer: Pretraining teaches broad language modeling, but not necessarily helpful assistant behavior. Instruction tuning shifts the model toward following natural-language tasks, formatting answers, and responding in a user-aligned way.

Follow-up questions:

- How is instruction tuning different from pretraining?
- What makes a good instruction dataset?

### 13. What is RLHF?

Short answer: RLHF aligns model behavior using human preference feedback.

Expanded answer: A common RLHF pipeline trains a reward model from human preference comparisons, then optimizes the policy model against that reward while constraining deviation from the original model. It can improve helpfulness and safety, but may introduce reward hacking or over-optimization.

Follow-up questions:

- Why use a KL penalty?
- What are the limitations of reward models?

### 14. What is DPO?

Short answer: Direct Preference Optimization trains from preference pairs without explicitly training a separate reward model.

Expanded answer: DPO turns preference optimization into a supervised objective derived from the relationship between policy probabilities and preference labels. It is simpler than classic RLHF pipelines and often easier to implement, though it still depends heavily on preference data quality.

Follow-up questions:

- How is DPO different from PPO-based RLHF?
- Why does preference data quality matter?

### 15. What is supervised fine-tuning?

Key points:

- Trains the model on input-output examples.
- Useful for format following, domain style, and task behavior.
- Can overfit or degrade generality if data is narrow or low quality.

### 16. What is catastrophic forgetting?

Key points:

- Fine-tuning on a narrow dataset can reduce performance on previously learned tasks.
- Mitigations include mixed data, lower learning rates, regularization, LoRA, and evaluation across old tasks.

### 17. What is data contamination?

Key points:

- Evaluation examples appear in training data.
- Makes benchmark results overestimate real generalization.
- Requires deduplication, benchmark filtering, and careful dataset audits.

### 18. What is synthetic data used for?

Key points:

- Scaling instruction data.
- Generating edge cases.
- Distilling behavior from stronger models.
- Bootstrapping domain tasks.

Common pitfall: assuming more synthetic data is always better. Quality, diversity, and filtering matter.

### 19. What is model distillation?

Key points:

- Trains a smaller or cheaper model to imitate a stronger teacher.
- Can use logits, responses, rationales, or preference signals.
- Useful for latency, cost, and deployment constraints.

### 20. What is curriculum learning?

Key points:

- Presents training examples in a deliberate order or difficulty schedule.
- Can improve stability or efficiency.
- In LLM training, data mixture and sampling strategy often matter more than simple easy-to-hard order.

## Fine-Tuning And Parameter-Efficient Adaptation

### 21. What is LoRA?

Short answer: LoRA fine-tunes low-rank adapter matrices while keeping the base model frozen.

Expanded answer: Instead of updating all model weights, LoRA injects trainable low-rank updates into selected linear layers. This reduces memory and storage cost, making adaptation easier. It is useful when you need domain behavior or task formatting without full fine-tuning.

Follow-up questions:

- Where should LoRA adapters be inserted?
- How do rank and alpha affect quality?
- How do you merge LoRA weights for inference?

### 22. What is QLoRA?

Short answer: QLoRA combines quantized base model weights with LoRA adapters to reduce fine-tuning memory.

Expanded answer: The base model is loaded in low-bit precision while small LoRA adapters remain trainable. This makes fine-tuning large models possible on much smaller hardware, though quantization can affect stability and quality.

### 23. When should you fine-tune instead of using RAG?

Key points:

- Fine-tune when the target is behavior, style, format, or task policy.
- Use RAG when the target is external or frequently changing knowledge.
- Combine both when the model needs domain behavior and grounded knowledge.

### 24. How do you evaluate a fine-tuned model?

Key points:

- Holdout task set.
- General capability regression set.
- Safety checks.
- Format adherence.
- Human preference evaluation.

### 25. What are common fine-tuning failure modes?

Key points:

- Overfitting.
- Forgetting.
- Poor data quality.
- Distribution mismatch.
- Instruction format mismatch.
- Evaluation leakage.

## Inference And Serving

### 26. What is KV cache?

Short answer: KV cache stores previously computed attention keys and values during autoregressive decoding.

Expanded answer: During generation, each new token attends to all previous tokens. Without KV cache, the model would recompute keys and values for the entire prefix at every step. KV cache trades memory for speed and is a major serving bottleneck for long-context models.

Follow-up questions:

- Why does KV cache help decode more than prefill?
- Why does long context increase KV cache pressure?
- How can KV cache be optimized?

### 27. What are prefill and decode?

Short answer: prefill processes the prompt in parallel, while decode generates new tokens sequentially.

Expanded answer: Prefill consumes the input context and builds KV cache. Decode generates one token at a time using the cache. Prefill is compute-heavy and parallelizable; decode is often memory-bandwidth-bound and latency-sensitive.

### 28. What is batching in LLM serving?

Key points:

- Groups requests to improve GPU utilization.
- Static batching is simple but can increase latency.
- Continuous batching schedules new requests dynamically during decoding.

### 29. What is quantization?

Key points:

- Reduces weight or activation precision.
- Lowers memory footprint and can improve throughput.
- May reduce quality if applied aggressively.
- Common formats include int8, int4, and mixed precision.

### 30. What is speculative decoding?

Key points:

- A smaller draft model proposes tokens.
- A larger target model verifies them.
- Improves decoding speed when draft acceptance rate is high.

### 31. Why is LLM decoding often memory-bound?

Key points:

- Each generated token requires reading large model weights and KV cache.
- Batch size and cache layout strongly affect throughput.
- GPU compute may be underutilized for small batches.

### 32. What is streaming output?

Key points:

- Sends tokens to the user as they are generated.
- Improves perceived latency.
- Requires careful handling of partial structured outputs.

### 33. How do temperature and top-p affect generation?

Key points:

- Temperature controls distribution sharpness.
- Top-p samples from the smallest token set whose cumulative probability exceeds `p`.
- Lower randomness improves determinism but does not guarantee truthfulness.

### 34. How would you reduce LLM serving cost?

Key points:

- Use smaller models for simple tasks.
- Cache responses or retrieval results.
- Reduce prompt length.
- Batch requests.
- Quantize models.
- Route by task difficulty.
- Evaluate model quality against cost.

### 35. How would you reduce latency?

Key points:

- Shorten prompts.
- Optimize retrieval.
- Use streaming.
- Use faster models.
- Use batching carefully.
- Cache common computations.
- Use speculative decoding or optimized inference engines.

## RAG

### 36. What is RAG?

Short answer: RAG retrieves external evidence and provides it to an LLM so answers can be grounded in source documents.

Expanded answer: A RAG system usually ingests documents, chunks them, embeds them, retrieves relevant chunks for a query, optionally reranks them, and generates an answer with citations. It is useful when knowledge changes often or must be auditable.

### 37. When is RAG better than fine-tuning?

Key points:

- Knowledge changes frequently.
- Sources must be cited.
- Documents are private or large.
- You need access control.
- You want cheaper updates than model retraining.

### 38. What makes chunking difficult?

Key points:

- Small chunks lose context.
- Large chunks dilute relevance.
- Tables, code, headings, and PDFs require structure-aware parsing.
- Parent-child chunking can balance retrieval precision and context completeness.

### 39. What is hybrid retrieval?

Key points:

- Combines dense embedding retrieval with sparse lexical retrieval such as BM25.
- Helps with rare terms, names, IDs, and semantic paraphrases.
- Often improves robustness over dense-only retrieval.

### 40. What is reranking?

Key points:

- Reorders retrieved candidates with a more accurate relevance model.
- Improves final context quality.
- Adds latency and cost.

### 41. How do you evaluate retrieval quality?

Key points:

- Recall@k.
- Precision@k.
- MRR.
- nDCG.
- Context relevance.
- Coverage of gold evidence.

### 42. How do you evaluate generation quality in RAG?

Key points:

- Faithfulness.
- Answer correctness.
- Citation correctness.
- Refusal quality.
- Completeness.
- User usefulness.

### 43. How do you debug hallucination in RAG?

Key points:

- Check whether the right evidence was retrieved.
- If not, fix parsing, chunking, embedding, filters, or query rewriting.
- If yes, fix prompt, context ordering, citation instructions, or refusal logic.

### 44. What is query rewriting?

Key points:

- Rewrites vague user queries into better retrieval queries.
- Can expand acronyms, add context, or decompose multi-hop questions.
- Must avoid changing user intent.

### 45. What is multi-hop RAG?

Key points:

- Answers require evidence from multiple sources.
- Retrieval may need iterative decomposition.
- Evaluation is harder because partial evidence can produce plausible but wrong answers.

### 46. How should RAG handle access control?

Key points:

- Enforce permissions before retrieval.
- Carry metadata through retrieval and generation.
- Avoid leaking restricted chunks in citations or logs.
- Test with adversarial users.

### 47. How do you keep a RAG index fresh?

Key points:

- Incremental ingestion.
- Document versioning.
- Deletion propagation.
- Re-embedding strategy.
- Freshness metrics and monitoring.

### 48. What are common RAG failure modes?

Key points:

- Bad parsing.
- Bad chunking.
- Embedding mismatch.
- Metadata filter bugs.
- Reranker misordering.
- Prompt ignores evidence.
- Citation mapping errors.

### 49. What is context compression?

Key points:

- Reduces retrieved content before generation.
- Useful for long documents or limited context windows.
- Risk: compression may remove critical evidence.

### 50. What is grounded generation?

Key points:

- The answer must be supported by supplied evidence.
- The model should cite sources and refuse unsupported claims.
- Requires prompt design, retrieval quality, and evaluation.

## Agents And Tool Use

### 51. What is an AI agent?

Short answer: an AI agent is a system that uses a model plus tools, state, and control logic to pursue a goal.

Expanded answer: Unlike a simple chatbot, an agent can plan, call tools, observe results, update state, and continue execution. Production agents also need permission boundaries, logging, evaluation, and failure recovery.

### 52. How is tool calling different from text generation?

Key points:

- Tool calling requires structured arguments.
- The model must choose whether and when to call a tool.
- Tool outputs become part of the execution state.
- Errors and retries must be handled explicitly.

### 53. What is ReAct?

Key points:

- Interleaves reasoning and acting.
- The model thinks, calls a tool, observes results, and continues.
- Useful for search and tool-use tasks.
- Risk: verbose or unbounded reasoning loops.

### 54. What is plan-and-execute?

Key points:

- First produces a plan, then executes steps.
- Useful for long tasks.
- Plans must be revised when observations contradict assumptions.

### 55. What is agent memory?

Key points:

- Short-term state stores current task context.
- Long-term memory stores reusable facts or preferences.
- Retrieval quality and forgetting policy matter.
- Memory can introduce privacy and correctness risks.

### 56. How do you evaluate an agent?

Key points:

- Task success rate.
- Tool-call accuracy.
- Recovery rate.
- Human intervention rate.
- Cost per successful task.
- Latency.
- Safety violations.

### 57. How do you prevent infinite agent loops?

Key points:

- Step limits.
- Budget limits.
- Progress checks.
- Termination criteria.
- Verifier model or rule-based stop conditions.

### 58. How do you make tool use safe?

Key points:

- Least privilege.
- Sandboxing.
- Dry-run mode.
- Human approval for risky actions.
- Audit logs.
- Idempotent operations.

### 59. What are common agent failure modes?

Key points:

- Tool hallucination.
- Bad arguments.
- Context drift.
- Over-planning.
- Ignoring tool output.
- Unsafe side effects.
- Weak completion verification.

### 60. What is multi-agent collaboration?

Key points:

- Multiple agents specialize in different roles.
- Can improve decomposition and review.
- Adds coordination overhead and failure complexity.
- Needs clear state and responsibility boundaries.

### 61. Design a coding agent.

Key points:

- Parse issue.
- Search codebase.
- Read relevant files.
- Edit minimally.
- Run tests.
- Repair if needed.
- Summarize diff and verification.
- Respect user changes and permissions.

### 62. Design a research assistant agent.

Key points:

- Ingest papers.
- Extract claims, methods, and evidence.
- Build topic map.
- Compare papers.
- Generate summaries and questions.
- Track citations and uncertainty.

### 63. What is a verifier in agent systems?

Key points:

- Checks whether output satisfies requirements.
- Can be rule-based, test-based, model-based, or human.
- Prevents premature completion.
- Must be evaluated itself.

### 64. What is workflow orchestration?

Key points:

- Defines deterministic or semi-deterministic control flow around model calls.
- Often more reliable than letting the model control everything.
- Useful for production agents with predictable steps.

### 65. What is the difference between autonomy and automation?

Key points:

- Automation follows predefined steps.
- Autonomy involves dynamic decisions under uncertainty.
- More autonomy requires stronger guardrails and evaluation.

## Evaluation, Safety, And Reliability

### 66. Why is LLM evaluation hard?

Short answer: many LLM tasks have open-ended outputs, changing user intents, and no single correct answer.

Expanded answer: Evaluation must combine automatic metrics, rubrics, human judgment, adversarial tests, and production monitoring. For RAG and agents, you also need component-level metrics because final answer quality alone does not reveal where failures happen.

### 67. What is LLM-as-a-judge?

Key points:

- Uses a model to evaluate outputs according to a rubric.
- Scales better than human evaluation.
- Can be biased by wording, position, model family, or verbosity.
- Should be calibrated against human labels.

### 68. What is faithfulness?

Key points:

- Output is supported by provided evidence.
- Especially important in RAG.
- Different from general correctness.

### 69. What is prompt injection?

Key points:

- Malicious or conflicting text attempts to override system instructions.
- Common in RAG and browsing agents.
- Mitigations include instruction hierarchy, content isolation, allowlisted tools, and output validation.

### 70. What is jailbreak testing?

Key points:

- Tests whether the model can be induced to violate safety rules.
- Should include direct, indirect, encoded, and multi-turn attacks.
- Needs regression testing after model or prompt changes.

### 71. How do you design a prompt regression test suite?

Key points:

- Use representative examples.
- Include edge cases and adversarial cases.
- Track expected format and behavior.
- Run on prompt, model, and retrieval changes.

### 72. What is observability for LLM applications?

Key points:

- Logs prompts, responses, tool calls, retrieval results, latency, cost, and user feedback.
- Must protect sensitive data.
- Enables debugging and quality monitoring.

### 73. How do you handle model upgrades?

Key points:

- Run regression tests.
- Compare quality, latency, and cost.
- Check prompt compatibility.
- Shadow traffic when possible.
- Roll out gradually.

### 74. What is refusal quality?

Key points:

- The model refuses when it should.
- It avoids refusing benign requests.
- It explains limitations clearly.
- In RAG, refusal should trigger when evidence is insufficient.

### 75. How do you evaluate safety in agent systems?

Key points:

- Permission violations.
- Unsafe tool calls.
- Data leakage.
- Failure to ask approval.
- Side-effect containment.
- Auditability.

## System Design

### 76. Design an enterprise knowledge assistant.

Key points:

- Document connectors.
- ACL-aware ingestion.
- Chunking and embedding.
- Hybrid retrieval and reranking.
- Grounded generation with citations.
- Evaluation and monitoring.
- Admin controls.

### 77. Design an AI customer support assistant.

Key points:

- Knowledge base RAG.
- Ticket context.
- Escalation policy.
- Tone and brand control.
- Tool calls for account actions.
- Human handoff.
- Safety and audit logs.

### 78. Design an AI meeting assistant.

Key points:

- Speech-to-text.
- Speaker diarization.
- Summarization.
- Action item extraction.
- Calendar/task integration.
- Privacy controls.

### 79. Design an AI code review assistant.

Key points:

- Diff parsing.
- Static analysis.
- Repository context retrieval.
- Risk classification.
- Comment generation.
- False positive control.

### 80. Design an LLM evaluation platform.

Key points:

- Dataset management.
- Prompt/model/version tracking.
- Batch evaluation.
- Human review.
- Judge calibration.
- Dashboards and regression alerts.

### 81. How do you design model routing?

Key points:

- Route by task complexity, risk, cost, and latency needs.
- Use small models for simple tasks.
- Escalate to stronger models for hard or risky cases.
- Monitor routing errors.

### 82. How do you design caching for LLM apps?

Key points:

- Cache deterministic outputs.
- Cache embeddings and retrieval results.
- Use semantic cache cautiously.
- Respect user permissions and data freshness.

### 83. How do you design rate limiting?

Key points:

- Per-user, per-tenant, and per-endpoint quotas.
- Protect expensive model calls and tools.
- Provide graceful degradation.

### 84. How do you handle PII?

Key points:

- Redaction.
- Access controls.
- Encryption.
- Data retention policies.
- Audit logs.
- Avoid unnecessary prompt logging.

### 85. How do you design human-in-the-loop review?

Key points:

- Trigger review for high-risk tasks.
- Provide evidence and model reasoning summary.
- Capture reviewer feedback for improvement.
- Track override rates.

## Multimodal And Long Context

### 86. What is a multimodal model?

Key points:

- Processes multiple modalities such as text, image, audio, or video.
- Needs modality encoders and alignment with language representation.
- Useful for document understanding, UI agents, robotics, and visual QA.

### 87. What is OCR-free document understanding?

Key points:

- Model directly consumes document images or layout-aware representations.
- Can preserve spatial information.
- Still needs careful evaluation on tables, forms, and small text.

### 88. Why is long-context modeling hard?

Key points:

- Attention cost.
- KV cache memory.
- Positional extrapolation.
- Retrieval within context.
- Lost-in-the-middle behavior.

### 89. What is lost-in-the-middle?

Key points:

- Models may underuse information placed in the middle of long contexts.
- Mitigations include reranking, reordering, summarization, and explicit citations.

### 90. Long context or RAG?

Key points:

- Long context is simple when the needed information is bounded and available.
- RAG is better for large, changing, permissioned corpora.
- Hybrid systems often use retrieval plus long context.

## Practical Engineering

### 91. How do you choose a model for a product?

Key points:

- Quality.
- Latency.
- Cost.
- Context window.
- Tool calling.
- Safety.
- Deployment constraints.
- Vendor reliability.

### 92. How do you debug a bad LLM response?

Key points:

- Reproduce.
- Inspect prompt.
- Inspect retrieved context.
- Inspect tool calls.
- Check model/version changes.
- Add regression test.

### 93. How do you control output format?

Key points:

- Use structured outputs or JSON schema when available.
- Add examples.
- Validate and repair output.
- Keep prompts concise and unambiguous.

### 94. What is function calling schema design?

Key points:

- Clear function names.
- Precise argument descriptions.
- Required vs optional fields.
- Validation.
- Avoid overly broad tools.

### 95. How do you build a reliable AI workflow?

Key points:

- Use deterministic code for deterministic steps.
- Use models for language, reasoning, and ambiguity.
- Add validators.
- Log intermediate state.
- Test end-to-end and by component.

### 96. What should not be delegated to an LLM?

Key points:

- Irreversible high-risk actions without approval.
- Exact arithmetic without tools.
- Security-critical checks without deterministic validation.
- Tasks requiring guaranteed truth without evidence.

### 97. How do you explain LLM uncertainty to users?

Key points:

- Cite sources.
- State limits.
- Offer confidence signals carefully.
- Refuse unsupported claims.
- Ask clarifying questions when needed.

### 98. How do you convert an AI demo into a production system?

Key points:

- Add evaluation.
- Add monitoring.
- Add data governance.
- Add error handling.
- Add cost controls.
- Add security review.
- Add user feedback loops.

### 99. What makes a strong AI resume project?

Key points:

- Realistic user problem.
- Clear architecture.
- Non-trivial tradeoffs.
- Evaluation metrics.
- Failure analysis.
- Reproducible demo or documentation.

### 100. How do you keep learning in a fast-moving AI field?

Key points:

- Track papers, model releases, frameworks, and production case studies.
- Rebuild small versions of important systems.
- Maintain reusable notes and skills.
- Evaluate claims by implementation and measurement.

