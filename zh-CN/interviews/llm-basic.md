# LLM 高频基础面试题

## 1. Attention 解决了什么问题？

简短回答：Attention 让每个 token 能动态选择序列中与自己最相关的信息。

展开回答：在序列建模中，并不是所有历史 token 都同等重要。Attention 通过 query 和 key 的相似度计算权重，再用这些权重聚合 value，从而更灵活地建模长距离依赖和上下文关系。

追问：

- 为什么 attention 容易并行？
- Self-attention 和 cross-attention 有什么区别？
- 为什么要除以 key 维度的平方根？

## 2. Multi-head attention 是什么？

简短回答：Multi-head attention 并行运行多个 attention head，让模型捕捉不同类型的关系。

展开回答：每个 head 会把 hidden states 投影到不同的 query、key、value 空间。有些 head 可能关注语法，有些关注实体，有些关注长距离依赖或局部上下文。最后把所有 head 的输出拼接并投影回模型维度。

追问：

- head 越多一定越好吗？
- head dimension 如何影响计算？

## 3. KV Cache 是什么？

简短回答：KV Cache 在自回归解码中缓存已经计算过的 key 和 value。

展开回答：Decoder-only LLM 逐 token 生成。如果没有 KV Cache，每生成一个 token 都要重新计算所有历史 token 的 key/value。KV Cache 避免重复计算，可以降低 decoding 延迟，但会增加显存占用。

追问：

- 为什么 KV Cache 主要帮助 decode，而不是 prefill？
- 长上下文如何影响 KV Cache 显存？
- 量化 KV Cache 有什么作用？

## 4. 比较 fine-tuning 和 RAG。

简短回答：Fine-tuning 改变模型行为或领域风格，RAG 在推理时注入外部知识。

展开回答：Fine-tuning 适合学习任务格式、领域语言或行为偏好。RAG 更适合频繁变化、需要引用、或规模过大无法写入模型参数的知识。生产中常见组合是：fine-tune 行为，RAG 提供知识。

追问：

- 什么时候 fine-tuning 不如 RAG？
- 如何评估 RAG 系统？
- 两种方式如何更新知识？

## 5. Hallucination 的原因是什么？

简短回答：Hallucination 是模型生成了看似合理但缺乏可靠证据支撑的内容。

展开回答：常见原因包括上下文不足、检索质量差、prompt 模糊、训练数据偏差、解码过度自信、缺乏验证机制。生产中通常通过更好的检索、引用、拒答、约束输出、评估和人工审核来缓解。

追问：

- 如何自动检测 hallucination？
- 为什么降低 temperature 不能彻底解决 hallucination？
- 如何设计证据不足时拒答的系统？

