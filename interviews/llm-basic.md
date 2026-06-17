# High-Frequency LLM Interview Questions

## 1. What problem does attention solve?

Short answer: attention lets each token dynamically select relevant information from other tokens.

Expanded answer: In sequence modeling, not all previous tokens are equally useful. Attention computes similarity between query and key vectors, then uses the resulting weights to combine value vectors. This allows the model to capture long-range dependencies and context-specific relationships more flexibly than fixed recurrent states.

Follow-up questions:

- Why is attention parallelizable?
- What is the difference between self-attention and cross-attention?
- Why do we divide by the square root of the key dimension?

## 2. What is multi-head attention?

Short answer: multi-head attention runs several attention operations in parallel so the model can capture different relationship patterns.

Expanded answer: Each head projects hidden states into different query, key, and value spaces. Some heads may focus on syntax, others on entities, long-range dependencies, or local context. The outputs are concatenated and projected back into the model dimension.

Follow-up questions:

- Does more heads always mean better performance?
- How does head dimension affect computation?

## 3. What is KV cache?

Short answer: KV cache stores previously computed key and value tensors during autoregressive decoding.

Expanded answer: In decoder-only LLMs, generation happens token by token. Without KV cache, the model would recompute attention keys and values for all previous tokens at every decoding step. KV cache avoids this repeated work, reducing latency during decoding. It increases memory usage, so serving systems need to manage the tradeoff between speed and memory.

Follow-up questions:

- Why does KV cache mainly help decoding rather than prefill?
- How does long context affect KV cache memory?
- How can quantized KV cache help serving?

## 4. Compare fine-tuning and RAG.

Short answer: fine-tuning changes model behavior or domain style, while RAG injects external knowledge at inference time.

Expanded answer: Fine-tuning is suitable when the model needs to learn a task format, domain language, or behavioral preference. RAG is better when knowledge changes frequently, must be cited, or is too large to fit into model weights. In production, many systems combine both: fine-tune for behavior and use RAG for knowledge grounding.

Follow-up questions:

- When is fine-tuning worse than RAG?
- How would you evaluate a RAG system?
- How would you update knowledge in each approach?

## 5. What causes hallucination?

Short answer: hallucination happens when a model generates plausible text that is not grounded in reliable evidence.

Expanded answer: Causes include insufficient context, weak retrieval, ambiguous prompts, training data artifacts, overconfident decoding, and lack of verification. In production systems, hallucination is usually mitigated through better retrieval, citation, abstention, constrained decoding, evaluation, and human review for high-risk cases.

Follow-up questions:

- How do you detect hallucination automatically?
- Why does lower temperature not fully solve hallucination?
- How do you design a system that refuses unsupported answers?

