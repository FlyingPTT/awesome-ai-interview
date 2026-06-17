# 高效推理论文路线图

本页跟踪理解 LLM inference、serving、latency、throughput 和 cost optimization 所需的概念。

## 核心问题

- 为什么 LLM serving 贵？
- Prefill 和 decode 有什么区别？
- KV Cache 如何影响显存？
- Batching 和 scheduling 如何提升吞吐？
- Quantization 和 speculative decoding 如何改变权衡？

## 阅读顺序

### 1. Autoregressive Decoding

学习：

- Prefill and decode。
- KV Cache。
- Token-by-token generation。
- Memory bandwidth bottlenecks。

面试要点：

- Decode 经常 memory-bound，而 prefill 更容易并行。

### 2. Batching And Scheduling

学习：

- Static batching。
- Continuous batching。
- Request scheduling。
- Paged KV Cache。

面试要点：

- Serving 系统要在控制单个用户延迟的同时优化 GPU 利用率。

### 3. Quantization

学习：

- Weight quantization。
- Activation quantization。
- KV Cache quantization。
- Accuracy-latency-memory tradeoffs。

面试要点：

- Quantization 降低内存并可能提升吞吐，但必须用任务质量验证。

### 4. Speculative Decoding

学习：

- Draft model。
- Target model verification。
- Acceptance rate。
- Latency tradeoffs。

面试要点：

- 当 draft model 足够便宜且 token 接受率高时，speculative decoding 有帮助。

### 5. Model Routing

学习：

- 小模型处理简单任务。
- 大模型处理困难或高风险任务。
- Cascades。
- Confidence and evaluation。

面试要点：

- 成本优化通常是系统设计问题，不只是模型压缩问题。

## 实现注意事项

- 追踪 time to first token 和 tokens per second。
- 分开 prefill 和 decode metrics。
- 监控 KV Cache memory。
- Quantization 后评估质量。
- 用 streaming 改善感知延迟。

## 面试题

- 为什么 KV Cache 是用显存换速度？
- Continuous batching 如何工作？
- Speculative decoding 是什么？
- 如何降低 serving cost？
- 如何在 model compression 和 model routing 之间选择？

