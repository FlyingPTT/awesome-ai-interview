# 面试 Skills

## 三层回答 Skill

目的：把一个技术概念转换成高质量面试回答。

输出结构：

1. 简短回答：一到两句话。
2. 展开回答：解释机制和 tradeoffs。
3. 追问防守：回答面试官可能继续追问的问题。

示例主题：KV Cache。

简短回答：KV Cache 在自回归解码中缓存已经计算过的 keys 和 values，避免每生成一个 token 都重新计算历史 token。

展开回答：它减少 decoding 阶段的重复 attention 计算，提升延迟表现，但会增加显存占用。长上下文 serving 需要通过 batching、paging、quantization 或 eviction 管理 KV Cache。

追问防守：

- 它对 decode 的帮助大于 prefill。
- 它用显存换速度。
- 它是长上下文应用的主要瓶颈之一。

