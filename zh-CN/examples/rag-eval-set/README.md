# RAG Eval Set

一个用于本地 [RAG Mini System](../../../examples/rag-mini-system/) 的小型评估集。

它展示：

- Answerable 和 unanswerable questions。
- Expected source document checks。
- Citation checks。
- Retrieval hit checks。
- Keyword coverage checks。
- 针对 retrieval、citation、refusal 和 generation 问题的 failure analysis。
- JSON report export。

## 运行

```bash
python3 examples/rag-eval-set/evaluate.py
```

写入 report：

```bash
python3 examples/rag-eval-set/evaluate.py --report /tmp/rag-eval-report.json
```

## 测试

```bash
python3 -m unittest discover examples/rag-eval-set/tests
```

## 面试 talking points

- RAG evaluation 应包含 answerable 和 unanswerable cases。
- Retrieval quality 和 generation quality 应分开检查。
- Citation correctness 是一等产品指标。
- 小 eval set 可以成为 prompt、retrieval 和 chunking changes 的 regression gate。
- Failure analysis 应把症状映射到可能出问题的 pipeline component。
