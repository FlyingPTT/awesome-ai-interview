# Efficient Inference Paper Map

This page tracks concepts useful for LLM inference, serving, latency, throughput, and cost optimization.

## Core Questions

- Why is LLM serving expensive?
- How do prefill and decode differ?
- How does KV cache affect memory?
- How do batching and scheduling improve throughput?
- How do quantization and speculative decoding change tradeoffs?

## Reading Order

### 1. Autoregressive Decoding

Study:

- Prefill and decode.
- KV cache.
- Token-by-token generation.
- Memory bandwidth bottlenecks.

Interview takeaway:

- Decode is often memory-bound, while prefill is more parallelizable.

### 2. Batching And Scheduling

Study:

- Static batching.
- Continuous batching.
- Request scheduling.
- Paged KV cache.

Interview takeaway:

- Serving systems optimize GPU utilization while controlling latency for individual users.

### 3. Quantization

Study:

- Weight quantization.
- Activation quantization.
- KV cache quantization.
- Accuracy-latency-memory tradeoffs.

Interview takeaway:

- Quantization reduces memory and can improve throughput, but must be validated against task quality.

### 4. Speculative Decoding

Study:

- Draft model.
- Target model verification.
- Acceptance rate.
- Latency tradeoffs.

Interview takeaway:

- Speculative decoding helps when the draft model is cheap and proposed tokens are often accepted.

### 5. Model Routing

Study:

- Small model for easy tasks.
- Large model for hard or risky tasks.
- Cascades.
- Confidence and evaluation.

Interview takeaway:

- Cost optimization is often a system design problem, not only a model compression problem.

## Implementation Notes

- Track time to first token and tokens per second.
- Separate prefill and decode metrics.
- Monitor KV cache memory.
- Evaluate quality after quantization.
- Use streaming to improve perceived latency.

## Interview Questions

- Why does KV cache trade memory for speed?
- How does continuous batching work?
- What is speculative decoding?
- How do you reduce serving cost?
- How do you choose between model compression and model routing?

