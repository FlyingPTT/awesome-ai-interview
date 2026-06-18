# RAG Mini System

一个无外部依赖、基于本地 Markdown 文件的 mini RAG 系统。

它展示：

- 本地文档 ingestion。
- Tokenization。
- Sparse BM25 风格 retrieval。
- 基于 token-overlap similarity 的 dense mock retrieval。
- Hybrid score fusion。
- Grounded answer synthesis。
- Citations。
- 证据弱时 refusal。

## 运行

```bash
python3 examples/rag-mini-system/run_demo.py
```

## 测试

```bash
python3 -m unittest discover examples/rag-mini-system/tests
```

## 文件

- `docs/`：本地 Markdown knowledge base。
- `rag.py`：retrieval、scoring 和 answer synthesis。
- `run_demo.py`：可运行 demo。
- `tests/`：单元测试。

## 面试 talking points

- RAG 质量取决于 parsing、chunking、retrieval、reranking、generation、citation 和 evaluation。
- Retrieval failure 和 generation failure 应分开 debug。
- Refusal behavior 是产品需求，不只是 prompt trick。
- 即使是 tiny RAG system，也应该暴露 retrieved evidence 和 scores。
- Hybrid retrieval 往往更稳健，因为 sparse retrieval 擅长精确词，而 dense retrieval 擅长语义重叠。
