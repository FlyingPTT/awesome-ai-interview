# 100 道 LLM 面试题

本页整理 LLM、RAG、AI Agent 和 Applied AI Engineer 岗位常见的 100 道面试题。

适合用作：

- 复习清单。
- 模拟面试题库。
- 深入学习路线图。
- 简历项目 talking points 来源。

## 回答方式

每道题建议按三层回答：

1. 简短回答：一到两句话。
2. 展开回答：机制、tradeoffs 和例子。
3. 追问防守：准备面试官可能继续追问的问题。

## Transformer 与 Attention

### 1. Self-attention 解决了什么问题？

简短回答：Self-attention 让每个 token 能动态聚合序列中其他 token 的信息。

展开回答：相比把历史信息压缩进固定 hidden state，self-attention 通过 query、key、value 计算 token 间相关性，从而更灵活地建模长距离依赖，并支持并行计算。

追问：

- 为什么 attention 比 RNN 更容易并行？
- Self-attention 和 cross-attention 有什么区别？
- 为什么长上下文下 attention 很贵？

### 2. 为什么 attention score 要除以 key 维度的平方根？

简短回答：为了避免 dot product 过大导致 softmax 饱和。

展开回答：当 query/key 维度较大时，点积方差会变大，softmax 容易变得过于尖锐，导致梯度不稳定。除以 `sqrt(d_k)` 可以稳定训练。

追问：

- 如果不做 scaling 会怎样？
- scaling 是否影响推理？

### 3. Multi-head attention 是什么？

简短回答：Multi-head attention 并行运行多个 attention head，用于捕捉不同类型的关系。

展开回答：每个 head 有独立的 Q/K/V 投影，可能关注局部模式、语法、实体跟踪或长距离依赖。多个 head 的结果拼接后再投影回模型维度。

追问：

- head 越多一定越好吗？
- head 数和 head dimension 有什么权衡？

### 4. 位置编码是什么，为什么需要？

简短回答：位置编码给 Transformer 注入 token 顺序信息。

展开回答：原始 self-attention 对顺序不敏感。位置编码可以用 absolute embeddings、relative position bias、RoPE、ALiBi 等方式加入。不同方案会影响长上下文外推能力。

追问：

- Absolute position embedding 和 RoPE 有什么区别？
- 长上下文模型为什么关心位置编码？

### 5. Encoder-only、Decoder-only、Encoder-decoder 模型有什么区别？

简短回答：Encoder-only 适合理解，Decoder-only 适合生成，Encoder-decoder 适合序列到序列任务。

展开回答：BERT 类模型使用双向 attention；GPT 类模型使用 causal attention 做自回归生成；T5 类模型用 encoder 编码输入，再用 decoder 生成输出。

追问：

- 为什么现代通用 LLM 多数是 decoder-only？
- Encoder-decoder 什么时候仍然有优势？

### 6. 什么是 causal masking？

要点：

- 防止 token 看到未来 token。
- 让训练时 next-token prediction 与生成过程一致。
- 通常在 softmax 前 mask 掉 attention matrix 的上三角。

常见误区：认为 causal masking 只在推理时使用。它训练时也使用。

### 7. Layer normalization 的作用是什么？

要点：

- 对特征维度上的 hidden activations 做归一化。
- 稳定深层网络训练。
- 大模型中 pre-norm Transformer 通常比 post-norm 更容易训练。

追问：比较 pre-norm 和 post-norm residual block。

### 8. Transformer block 中 FFN 的作用是什么？

要点：

- Attention 负责 token 间信息混合，FFN 负责 token-wise 非线性变换。
- FFN hidden dimension 通常远大于 model dimension。
- 现代 LLM 常用 SwiGLU 等 gated variants。

### 9. 为什么残差连接重要？

要点：

- 改善梯度流动。
- 让很深的模型可训练。
- 让每层学习增量修正，而不是完整重建表示。

### 10. Attention 的计算复杂度是什么？

要点：

- 标准 full attention 对序列长度是 `O(n^2)`。
- KV Cache 改变生成阶段的计算方式，但长上下文仍有显存压力。
- 长上下文系统会使用 sparse attention、sliding window、retrieval、compression 或 memory 机制。

## 训练与对齐

### 11. Decoder-only LLM 的标准预训练目标是什么？

简短回答：Next-token prediction。

展开回答：模型根据前文预测下一个 token。这个目标简单、可扩展，能从大规模文本中学习语言模式、世界知识和任务形式。

追问：

- 为什么 next-token prediction 能产生广泛能力？
- 它的局限是什么？

### 12. 什么是 instruction tuning？

简短回答：Instruction tuning 用指令-回答数据训练模型，让模型更会遵循用户请求。

展开回答：预训练让模型学会语言建模，但不保证有帮助的助手行为。Instruction tuning 会强化任务理解、格式遵循和面向用户的回答方式。

追问：

- Instruction tuning 和 pretraining 有什么区别？
- 好的 instruction dataset 应具备什么特征？

### 13. 什么是 RLHF？

简短回答：RLHF 使用人类偏好反馈来对齐模型行为。

展开回答：常见流程是先用偏好比较训练 reward model，再用强化学习优化 policy，同时通过 KL penalty 限制模型偏离原始模型。它能提升 helpfulness 和 safety，但也可能引入 reward hacking。

追问：

- 为什么要用 KL penalty？
- Reward model 的局限是什么？

### 14. 什么是 DPO？

简短回答：DPO 直接用偏好对优化模型，不需要显式训练单独的 reward model。

展开回答：DPO 将 preference optimization 转换成监督式目标，利用 chosen/rejected pair 优化 policy probability。相比 PPO 式 RLHF 更简单，但仍高度依赖偏好数据质量。

追问：

- DPO 和 PPO-based RLHF 有什么区别？
- 为什么 preference data quality 很重要？

### 15. 什么是 supervised fine-tuning？

要点：

- 用输入-输出样例训练模型。
- 适合学习格式、领域风格和任务行为。
- 数据太窄或质量差会导致过拟合和能力退化。

### 16. 什么是 catastrophic forgetting？

要点：

- 模型在窄数据上 fine-tune 后，可能损失原本能力。
- 缓解方式包括混合数据、较低学习率、正则化、LoRA 和覆盖旧任务的评估集。

### 17. 什么是 data contamination？

要点：

- 评估样本出现在训练数据中。
- 会让 benchmark 分数虚高。
- 需要去重、过滤 benchmark、审计数据集。

### 18. Synthetic data 有什么用途？

要点：

- 扩展 instruction data。
- 生成 edge cases。
- 从强模型蒸馏行为。
- 启动领域任务数据。

常见误区：synthetic data 越多越好。质量、多样性和过滤更重要。

### 19. 什么是 model distillation？

要点：

- 用强 teacher 训练更小或更便宜的 student。
- 可蒸馏 logits、回答、rationales 或 preference signals。
- 常用于降低延迟、成本和部署难度。

### 20. 什么是 curriculum learning？

要点：

- 按某种难度或顺序组织训练样本。
- 可提高训练稳定性或效率。
- 在 LLM 中，数据 mixture 和 sampling strategy 往往比简单的 easy-to-hard 更关键。

## Fine-tuning 与参数高效适配

### 21. LoRA 是什么？

简短回答：LoRA 冻结 base model，只训练低秩 adapter 矩阵。

展开回答：LoRA 在部分线性层中注入可训练的低秩更新，显著降低显存和存储成本。适合在不全量 fine-tune 的情况下适配领域行为、格式或任务。

追问：

- LoRA adapter 应插在哪里？
- rank 和 alpha 如何影响效果？
- 推理时如何 merge LoRA 权重？

### 22. QLoRA 是什么？

简短回答：QLoRA 将量化 base model 与 LoRA adapters 结合，用更低显存 fine-tune 大模型。

展开回答：Base model 以低 bit 精度加载，小型 LoRA adapter 保持可训练。这让普通硬件上微调较大模型成为可能，但量化可能影响稳定性和质量。

### 23. 什么时候应该 fine-tune，而不是 RAG？

要点：

- 目标是行为、风格、格式或任务策略时，用 fine-tuning。
- 目标是外部知识或频繁变化知识时，用 RAG。
- 常见组合是 fine-tune 行为，RAG 提供知识。

### 24. 如何评估 fine-tuned model？

要点：

- Holdout task set。
- 通用能力回归集。
- Safety checks。
- Format adherence。
- Human preference evaluation。

### 25. Fine-tuning 常见失败模式有哪些？

要点：

- 过拟合。
- Forgetting。
- 数据质量差。
- 分布不匹配。
- 指令格式不一致。
- Evaluation leakage。

## 推理与 Serving

### 26. KV Cache 是什么？

简短回答：KV Cache 在自回归 decoding 中缓存已经计算过的 attention keys 和 values。

展开回答：生成每个新 token 时都要关注历史 token。没有 KV Cache 就会反复计算整个 prefix 的 key/value。KV Cache 用显存换速度，是长上下文 serving 的主要瓶颈之一。

追问：

- 为什么 KV Cache 对 decode 帮助更大？
- 长上下文为什么增加 KV Cache 压力？
- KV Cache 如何优化？

### 27. Prefill 和 decode 是什么？

简短回答：Prefill 并行处理 prompt，decode 顺序生成新 token。

展开回答：Prefill 消耗输入上下文并建立 KV Cache；decode 每次生成一个 token。Prefill 更偏 compute-heavy 且可并行，decode 往往 memory-bandwidth-bound 且对延迟敏感。

### 28. LLM serving 中的 batching 是什么？

要点：

- 把多个请求合并，提高 GPU 利用率。
- Static batching 简单但可能增加延迟。
- Continuous batching 在 decoding 中动态调度新请求。

### 29. 量化是什么？

要点：

- 降低权重或 activation 精度。
- 减少显存占用，可能提升吞吐。
- 过度量化会伤害质量。
- 常见格式包括 int8、int4 和 mixed precision。

### 30. Speculative decoding 是什么？

要点：

- 小 draft model 先提出 token。
- 大 target model 验证 token。
- draft 接受率高时可显著加速 decoding。

### 31. 为什么 LLM decoding 经常是 memory-bound？

要点：

- 每生成一个 token 都需要读取大量模型权重和 KV Cache。
- batch size 与 cache layout 会影响吞吐。
- 小 batch 下 GPU compute 可能无法充分利用。

### 32. 什么是 streaming output？

要点：

- token 生成后立即返回给用户。
- 改善感知延迟。
- 对部分结构化输出需要谨慎处理。

### 33. Temperature 和 top-p 如何影响生成？

要点：

- Temperature 控制分布尖锐程度。
- Top-p 从累计概率超过 p 的最小 token 集中采样。
- 降低随机性提高确定性，但不保证真实性。

### 34. 如何降低 LLM serving 成本？

要点：

- 简单任务用小模型。
- 缓存回答或检索结果。
- 缩短 prompt。
- Batch 请求。
- 量化模型。
- 按任务难度路由模型。
- 用质量-成本曲线选模型。

### 35. 如何降低延迟？

要点：

- 缩短 prompt。
- 优化 retrieval。
- 使用 streaming。
- 使用更快模型。
- 谨慎 batching。
- 缓存常见计算。
- 使用 speculative decoding 或优化推理引擎。

## RAG

### 36. RAG 是什么？

简短回答：RAG 检索外部证据并提供给 LLM，让答案基于来源文档生成。

展开回答：RAG 系统通常包括文档接入、切分、embedding、检索、reranking 和带引用的答案生成。它适合知识频繁变化或必须可审计的场景。

### 37. 什么时候 RAG 比 fine-tuning 更好？

要点：

- 知识频繁变化。
- 必须引用来源。
- 文档私有或规模很大。
- 需要 access control。
- 希望低成本更新知识。

### 38. Chunking 为什么难？

要点：

- chunk 太小会丢上下文。
- chunk 太大会稀释相关性。
- 表格、代码、标题和 PDF 需要结构化解析。
- Parent-child chunking 可兼顾检索精度和上下文完整性。

### 39. Hybrid retrieval 是什么？

要点：

- 结合 dense embedding retrieval 和 BM25 等 sparse retrieval。
- 对罕见词、名称、ID 和语义改写更稳健。
- 通常比 dense-only retrieval 更鲁棒。

### 40. Reranking 是什么？

要点：

- 用更准确的相关性模型对候选结果重新排序。
- 提升最终上下文质量。
- 增加延迟和成本。

### 41. 如何评估 retrieval quality？

要点：

- Recall@k。
- Precision@k。
- MRR。
- nDCG。
- Context relevance。
- Gold evidence coverage。

### 42. 如何评估 RAG generation quality？

要点：

- Faithfulness。
- Answer correctness。
- Citation correctness。
- Refusal quality。
- Completeness。
- User usefulness。

### 43. 如何 debug RAG hallucination？

要点：

- 检查正确证据是否被检索到。
- 若没有，修复 parsing、chunking、embedding、filters 或 query rewriting。
- 若有，修复 prompt、context ordering、citation instructions 或 refusal logic。

### 44. Query rewriting 是什么？

要点：

- 把模糊用户问题改写成更适合检索的 query。
- 可扩展缩写、补充上下文、拆解多跳问题。
- 不能改变用户意图。

### 45. Multi-hop RAG 是什么？

要点：

- 答案需要多个来源的证据。
- 检索可能需要迭代拆解。
- 评估更难，因为部分证据可能生成看似合理但错误的答案。

### 46. RAG 如何处理访问控制？

要点：

- 检索前执行权限过滤。
- 元数据贯穿 retrieval 和 generation。
- 避免 restricted chunks 在引用或日志中泄露。
- 用 adversarial users 测试。

### 47. 如何保持 RAG index 新鲜？

要点：

- 增量 ingestion。
- 文档版本管理。
- 删除传播。
- Re-embedding 策略。
- Freshness metrics 和 monitoring。

### 48. RAG 常见失败模式有哪些？

要点：

- 解析差。
- 切分差。
- Embedding mismatch。
- Metadata filter bug。
- Reranker 排序错误。
- Prompt 忽略证据。
- Citation mapping 错误。

### 49. Context compression 是什么？

要点：

- 在生成前压缩 retrieved content。
- 适合长文档或上下文窗口有限场景。
- 风险是压缩掉关键证据。

### 50. Grounded generation 是什么？

要点：

- 答案必须被提供的证据支撑。
- 模型应引用来源并拒绝无证据声明。
- 依赖 prompt、retrieval quality 和 evaluation。

## Agents 与工具使用

### 51. AI Agent 是什么？

简短回答：AI Agent 是用模型、工具、状态和控制逻辑一起完成目标的系统。

展开回答：相比普通 chatbot，Agent 可以规划、调用工具、观察结果、更新状态并持续执行。生产 Agent 还需要权限边界、日志、评估和失败恢复。

### 52. Tool calling 和文本生成有什么不同？

要点：

- Tool calling 需要结构化参数。
- 模型要决定是否调用、何时调用哪个工具。
- 工具输出会进入执行状态。
- 错误和重试需要显式处理。

### 53. ReAct 是什么？

要点：

- 交替进行 reasoning 和 acting。
- 模型思考、调用工具、观察结果，然后继续。
- 适合搜索和工具使用任务。
- 风险是冗长或无边界循环。

### 54. Plan-and-execute 是什么？

要点：

- 先生成计划，再执行步骤。
- 适合长任务。
- 观察结果与假设冲突时需要修改计划。

### 55. Agent memory 是什么？

要点：

- 短期状态保存当前任务上下文。
- 长期记忆保存可复用事实或偏好。
- 检索质量和遗忘策略很重要。
- Memory 会引入隐私和正确性风险。

### 56. 如何评估 Agent？

要点：

- Task success rate。
- Tool-call accuracy。
- Recovery rate。
- Human intervention rate。
- Cost per successful task。
- Latency。
- Safety violations。

### 57. 如何防止 Agent 无限循环？

要点：

- Step limits。
- Budget limits。
- Progress checks。
- Termination criteria。
- Verifier model 或 rule-based stop conditions。

### 58. 如何让工具使用更安全？

要点：

- 最小权限。
- 沙箱。
- Dry-run mode。
- 高风险操作人工审批。
- Audit logs。
- 幂等操作。

### 59. Agent 常见失败模式有哪些？

要点：

- Tool hallucination。
- 参数错误。
- Context drift。
- Over-planning。
- 忽略工具输出。
- 不安全副作用。
- Completion verification 弱。

### 60. Multi-agent collaboration 是什么？

要点：

- 多个 Agent 扮演不同角色。
- 可改善任务拆解和 review。
- 增加协调成本和失败复杂度。
- 需要清晰的状态和责任边界。

### 61. 设计一个 Coding Agent。

要点：

- 解析 issue。
- 搜索代码库。
- 阅读相关文件。
- 最小化编辑。
- 运行测试。
- 失败时修复。
- 总结 diff 和验证结果。
- 尊重用户修改和权限边界。

### 62. 设计一个研究助手 Agent。

要点：

- 接入论文。
- 提取 claims、methods 和 evidence。
- 构建 topic map。
- 比较论文。
- 生成总结和问题。
- 跟踪引用与不确定性。

### 63. Agent 系统中的 verifier 是什么？

要点：

- 检查输出是否满足要求。
- 可以是规则、测试、模型或人工。
- 防止过早宣布完成。
- Verifier 本身也需要评估。

### 64. Workflow orchestration 是什么？

要点：

- 在模型调用外定义确定性或半确定性的控制流。
- 通常比完全交给模型控制更可靠。
- 适合生产 Agent 中可预期的步骤。

### 65. Autonomy 和 automation 有什么区别？

要点：

- Automation 按预定义步骤执行。
- Autonomy 在不确定环境下动态决策。
- 自治程度越高，越需要 guardrails 和 evaluation。

## 评估、安全与可靠性

### 66. 为什么 LLM evaluation 很难？

简短回答：很多 LLM 任务是开放式输出，用户意图会变化，且没有唯一正确答案。

展开回答：评估需要结合自动指标、rubric、人工判断、adversarial tests 和生产监控。对 RAG 和 Agent，还需要 component-level metrics，因为最终答案好坏不能说明失败发生在哪里。

### 67. LLM-as-a-judge 是什么？

要点：

- 用模型按 rubric 评估输出。
- 比人工评估更易扩展。
- 可能受措辞、位置、模型家族和 verbosity 影响。
- 应用人类标注校准。

### 68. Faithfulness 是什么？

要点：

- 输出是否被提供证据支撑。
- 在 RAG 中尤其重要。
- 不等同于一般 correctness。

### 69. Prompt injection 是什么？

要点：

- 恶意或冲突文本试图覆盖系统指令。
- 常见于 RAG 和 browsing agents。
- 缓解方式包括 instruction hierarchy、content isolation、allowlisted tools 和 output validation。

### 70. Jailbreak testing 是什么？

要点：

- 测试模型是否会被诱导违反安全规则。
- 应包括 direct、indirect、encoded 和 multi-turn attacks。
- 模型或 prompt 变更后需要回归测试。

### 71. 如何设计 prompt regression test suite？

要点：

- 使用代表性样例。
- 加入 edge cases 和 adversarial cases。
- 追踪期望格式和行为。
- Prompt、模型、retrieval 变化时都运行。

### 72. LLM 应用的 observability 包括什么？

要点：

- 记录 prompts、responses、tool calls、retrieval results、latency、cost 和 user feedback。
- 必须保护敏感数据。
- 支持 debugging 和质量监控。

### 73. 如何处理模型升级？

要点：

- 运行 regression tests。
- 比较 quality、latency 和 cost。
- 检查 prompt 兼容性。
- 可行时使用 shadow traffic。
- 渐进 rollout。

### 74. Refusal quality 是什么？

要点：

- 该拒绝时拒绝。
- 不误拒 benign requests。
- 清晰解释限制。
- RAG 中证据不足时应触发拒答。

### 75. 如何评估 Agent 安全？

要点：

- 权限违规。
- 不安全工具调用。
- 数据泄露。
- 未请求审批。
- 副作用隔离。
- 可审计性。

## 系统设计

### 76. 设计企业知识助手。

要点：

- Document connectors。
- ACL-aware ingestion。
- Chunking and embedding。
- Hybrid retrieval and reranking。
- 带 citation 的 grounded generation。
- Evaluation and monitoring。
- Admin controls。

### 77. 设计 AI 客服助手。

要点：

- Knowledge base RAG。
- Ticket context。
- Escalation policy。
- Tone and brand control。
- 账户操作工具调用。
- Human handoff。
- Safety and audit logs。

### 78. 设计 AI 会议助手。

要点：

- Speech-to-text。
- Speaker diarization。
- Summarization。
- Action item extraction。
- Calendar/task integration。
- Privacy controls。

### 79. 设计 AI code review assistant。

要点：

- Diff parsing。
- Static analysis。
- Repository context retrieval。
- Risk classification。
- Comment generation。
- False positive control。

### 80. 设计 LLM evaluation platform。

要点：

- Dataset management。
- Prompt/model/version tracking。
- Batch evaluation。
- Human review。
- Judge calibration。
- Dashboards and regression alerts。

### 81. 如何设计 model routing？

要点：

- 按任务复杂度、风险、成本和延迟需求路由。
- 简单任务用小模型。
- 困难或高风险任务升级到强模型。
- 监控 routing errors。

### 82. 如何设计 LLM app caching？

要点：

- 缓存 deterministic outputs。
- 缓存 embeddings 和 retrieval results。
- 谨慎使用 semantic cache。
- 尊重用户权限和数据新鲜度。

### 83. 如何设计 rate limiting？

要点：

- Per-user、per-tenant、per-endpoint quotas。
- 保护昂贵模型调用和工具。
- 提供 graceful degradation。

### 84. 如何处理 PII？

要点：

- Redaction。
- Access controls。
- Encryption。
- Data retention policies。
- Audit logs。
- 避免不必要的 prompt logging。

### 85. 如何设计 human-in-the-loop review？

要点：

- 高风险任务触发 review。
- 提供 evidence 和模型 reasoning summary。
- 收集 reviewer feedback。
- 追踪 override rates。

## 多模态与长上下文

### 86. 多模态模型是什么？

要点：

- 处理 text、image、audio、video 等多种模态。
- 需要 modality encoders 和语言表示对齐。
- 用于文档理解、UI agents、机器人和视觉问答。

### 87. OCR-free document understanding 是什么？

要点：

- 模型直接消费文档图片或 layout-aware 表示。
- 可以保留空间信息。
- 对表格、表单和小字体仍需仔细评估。

### 88. 长上下文建模为什么难？

要点：

- Attention cost。
- KV Cache memory。
- 位置外推。
- Context 内检索。
- Lost-in-the-middle。

### 89. Lost-in-the-middle 是什么？

要点：

- 模型可能不充分利用长上下文中间位置的信息。
- 缓解方式包括 reranking、reordering、summarization 和 explicit citations。

### 90. 长上下文还是 RAG？

要点：

- 需要的信息范围有限且已知时，长上下文更简单。
- 对大规模、变化频繁、带权限的语料，RAG 更合适。
- 实际系统常结合 retrieval 和 long context。

## 实用工程

### 91. 如何为产品选择模型？

要点：

- Quality。
- Latency。
- Cost。
- Context window。
- Tool calling。
- Safety。
- Deployment constraints。
- Vendor reliability。

### 92. 如何 debug 糟糕的 LLM response？

要点：

- 复现问题。
- 检查 prompt。
- 检查 retrieved context。
- 检查 tool calls。
- 检查 model/version changes。
- 加入 regression test。

### 93. 如何控制输出格式？

要点：

- 尽量使用 structured outputs 或 JSON schema。
- 添加示例。
- 校验并修复输出。
- Prompt 保持简洁且无歧义。

### 94. Function calling schema design 是什么？

要点：

- 清晰的 function names。
- 精确的参数描述。
- 区分 required 与 optional fields。
- 参数校验。
- 避免过于宽泛的工具。

### 95. 如何构建可靠 AI workflow？

要点：

- 确定性步骤用确定性代码。
- 语言、推理、模糊判断交给模型。
- 加 validators。
- 记录中间状态。
- 做端到端和组件级测试。

### 96. 什么任务不该交给 LLM？

要点：

- 无审批的不可逆高风险操作。
- 不使用工具的精确计算。
- 无确定性校验的安全关键检查。
- 没有证据却要求保证真实的任务。

### 97. 如何向用户表达 LLM 不确定性？

要点：

- 引用来源。
- 说明限制。
- 谨慎提供 confidence signals。
- 拒绝无证据声明。
- 必要时提出澄清问题。

### 98. 如何把 AI demo 变成 production system？

要点：

- 加 evaluation。
- 加 monitoring。
- 加 data governance。
- 加 error handling。
- 加 cost controls。
- 加 security review。
- 加 user feedback loops。

### 99. 什么是强 AI 简历项目？

要点：

- 真实用户问题。
- 清晰架构。
- 非平凡 tradeoffs。
- Evaluation metrics。
- Failure analysis。
- 可复现 demo 或文档。

### 100. 如何在快速变化的 AI 领域持续学习？

要点：

- 跟踪论文、模型发布、框架和生产案例。
- 复现重要系统的小版本。
- 维护可复用笔记和 skills。
- 用实现和测量验证各种 claims。

