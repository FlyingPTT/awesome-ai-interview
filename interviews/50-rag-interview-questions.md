# 50 RAG Interview Questions

This page collects 50 interview questions for Retrieval-Augmented Generation systems. It focuses on practical engineering, debugging, evaluation, and system design.

## Foundations

### 1. What is RAG?

Key points:

- Retrieval-Augmented Generation combines external retrieval with LLM generation.
- It is useful when knowledge is large, private, changing, or must be cited.
- A typical pipeline includes ingestion, parsing, chunking, embedding, retrieval, reranking, generation, and evaluation.

Follow-up: when is RAG worse than a long-context prompt?

### 2. Why use RAG instead of fine-tuning?

Key points:

- RAG updates knowledge without retraining.
- RAG can cite sources.
- RAG can enforce document-level permissions.
- Fine-tuning is better for behavior, style, and task policy.

Follow-up: when should you combine RAG and fine-tuning?

### 3. What are the main components of a RAG system?

Key points:

- Data connectors.
- Parser and normalizer.
- Chunker.
- Embedding model.
- Vector and metadata index.
- Retriever.
- Reranker.
- Prompt builder.
- Generator.
- Evaluator and monitor.

### 4. What is grounded generation?

Key points:

- The answer must be supported by retrieved evidence.
- The model should cite sources and refuse unsupported claims.
- Grounding quality depends on retrieval, prompt design, and evaluation.

### 5. What is the difference between RAG and search?

Key points:

- Search returns documents or passages.
- RAG uses retrieved evidence to generate an answer.
- RAG must handle citation, synthesis, refusal, and hallucination risk.

## Ingestion And Chunking

### 6. Why is document parsing important?

Key points:

- Bad parsing corrupts downstream retrieval.
- PDFs, tables, figures, headers, footers, and code blocks need special handling.
- Preserve metadata such as title, section, page, permissions, and version.

### 7. What makes chunking difficult?

Key points:

- Small chunks improve precision but may lose context.
- Large chunks preserve context but dilute relevance.
- Structure-aware chunking is often better than fixed-size chunking.

### 8. What is parent-child chunking?

Key points:

- Retrieve small child chunks for precision.
- Provide larger parent chunks for generation context.
- Useful when local evidence depends on surrounding paragraphs or sections.

### 9. How do you chunk tables?

Key points:

- Preserve headers and row/column relationships.
- Include table captions and nearby explanatory text.
- Consider table-aware parsing or converting rows into structured records.

### 10. How do you handle code documents?

Key points:

- Chunk by symbols, functions, classes, or files.
- Preserve imports, signatures, comments, and dependencies.
- Retrieval may need both lexical and semantic search.

### 11. How do you handle duplicate documents?

Key points:

- Deduplicate exact and near-duplicate content.
- Preserve canonical source ids.
- Avoid returning many copies of the same evidence.

### 12. How do you handle document updates?

Key points:

- Track document versions.
- Re-index changed chunks.
- Propagate deletions.
- Monitor freshness lag.

## Retrieval

### 13. What is dense retrieval?

Key points:

- Uses embedding similarity to retrieve semantically related chunks.
- Good for paraphrases and conceptual matching.
- Weak for exact identifiers, rare terms, and numbers.

### 14. What is sparse retrieval?

Key points:

- Uses lexical matching such as BM25.
- Strong for exact terms, names, IDs, and error messages.
- Weak for semantic paraphrases.

### 15. What is hybrid retrieval?

Key points:

- Combines dense and sparse retrieval.
- Improves robustness.
- Requires score normalization or fusion strategy.

### 16. What is metadata filtering?

Key points:

- Filters by source, user permissions, date, product, tenant, or document type.
- Must be applied before generation.
- Filter bugs can cause data leakage or missing evidence.

### 17. What is query rewriting?

Key points:

- Converts user queries into better retrieval queries.
- Helps with vague, conversational, or multi-turn questions.
- Must preserve user intent.

### 18. What is query expansion?

Key points:

- Adds synonyms, acronyms, related terms, or domain context.
- Can improve recall.
- Can reduce precision if expansion is too broad.

### 19. What is multi-query retrieval?

Key points:

- Generates several retrieval queries for one user question.
- Improves coverage.
- Needs deduplication and reranking.

### 20. What is multi-hop retrieval?

Key points:

- Retrieves evidence in multiple steps.
- Useful when answer requires combining facts.
- Needs state tracking and stopping criteria.

## Reranking And Context Building

### 21. Why use reranking?

Key points:

- First-stage retrieval optimizes speed.
- Reranking optimizes final relevance.
- It improves context precision but adds latency.

### 22. What is a cross-encoder reranker?

Key points:

- Scores query-document pairs jointly.
- Usually more accurate than embedding similarity.
- More expensive, so it is applied to a small candidate set.

### 23. How do you choose top-k?

Key points:

- Larger k improves recall but increases noise and cost.
- Smaller k improves precision but may miss evidence.
- Tune k using retrieval and answer-level evaluation.

### 24. How do you order retrieved context?

Key points:

- By relevance, source structure, time, or dependency order.
- Important evidence near the beginning or end may be used better.
- Long-context systems can suffer lost-in-the-middle.

### 25. What is context compression?

Key points:

- Reduces retrieved content before generation.
- Useful for long documents and limited context windows.
- Risk: removing critical evidence.

## Generation And Refusal

### 26. How do you prompt a RAG model?

Key points:

- Separate system instructions, user question, and retrieved evidence.
- Require citations.
- Tell the model to refuse if evidence is insufficient.
- Keep source ids attached to evidence.

### 27. How do you make citations reliable?

Key points:

- Preserve source ids through the pipeline.
- Ask the model to cite only provided source ids.
- Validate citations after generation.
- Link citations back to exact chunks or pages.

### 28. How should RAG handle insufficient evidence?

Key points:

- Refuse or ask for clarification.
- State what is missing.
- Avoid guessing.
- Optionally suggest where to look next.

### 29. How do you reduce hallucination?

Key points:

- Improve retrieval recall and precision.
- Add citation and refusal requirements.
- Validate answers against evidence.
- Evaluate faithfulness.

### 30. How do you handle conflicting sources?

Key points:

- Prefer authoritative or recent sources.
- Expose disagreement.
- Cite both sides.
- Use metadata such as version, owner, and date.

## Evaluation

### 31. How do you evaluate retrieval?

Key points:

- Recall@k.
- Precision@k.
- MRR.
- nDCG.
- Gold evidence coverage.
- Query-level failure analysis.

### 32. How do you evaluate generation?

Key points:

- Answer correctness.
- Faithfulness.
- Citation correctness.
- Refusal quality.
- Completeness.
- User usefulness.

### 33. What is faithfulness?

Key points:

- The answer is supported by retrieved context.
- It is different from general factual correctness.
- It can be checked by human review, rules, or LLM judges.

### 34. What is context precision?

Key points:

- Measures how much retrieved context is actually relevant.
- Low precision increases hallucination risk and token cost.
- Reranking and filtering can improve it.

### 35. How do you build a RAG evaluation set?

Key points:

- Include real user questions.
- Label gold evidence when possible.
- Include unanswerable questions.
- Cover edge cases, permissions, and stale documents.

### 36. How do you use LLM-as-a-judge for RAG?

Key points:

- Judge faithfulness, relevance, and answer quality with rubrics.
- Calibrate against human labels.
- Avoid giving the judge information that the model did not have.

### 37. What are common evaluation pitfalls?

Key points:

- Only evaluating final answer quality.
- Ignoring retrieval failures.
- No unanswerable questions.
- Judge bias.
- Test data leakage.

## Production And Reliability

### 38. How do you monitor RAG in production?

Key points:

- Query distribution.
- Retrieval hit rate.
- Top sources.
- Latency and cost.
- Refusal rate.
- User feedback.
- Citation errors.

### 39. How do you debug a bad answer?

Key points:

- Reproduce the query.
- Inspect parsed documents.
- Inspect retrieved chunks.
- Inspect reranker output.
- Inspect final prompt.
- Check citation and refusal behavior.

### 40. How do you handle permissions?

Key points:

- Enforce ACLs during indexing and retrieval.
- Avoid logging restricted content.
- Test cross-tenant leakage.
- Preserve permission metadata end to end.

### 41. How do you reduce latency?

Key points:

- Cache embeddings and retrieval results.
- Limit candidate count.
- Use faster rerankers.
- Parallelize retrieval.
- Stream generation.
- Route simple queries to cheaper paths.

### 42. How do you reduce cost?

Key points:

- Reduce context length.
- Use smaller models.
- Cache common queries.
- Tune top-k.
- Compress context.
- Monitor cost per successful answer.

### 43. How do you support multi-turn RAG?

Key points:

- Rewrite follow-up questions using conversation state.
- Avoid blindly retrieving on the whole chat history.
- Track user intent and referenced entities.
- Preserve permissions.

### 44. How do you handle multilingual RAG?

Key points:

- Choose multilingual embeddings or translate queries/documents.
- Evaluate by language.
- Preserve original source language for citation.
- Beware cross-lingual retrieval gaps.

### 45. How do you handle images or scanned PDFs?

Key points:

- OCR or multimodal parsing.
- Preserve layout and page coordinates.
- Evaluate tables, figures, and small text.
- Store visual references when needed.

## System Design Scenarios

### 46. Design a RAG system for legal documents.

Key points:

- Strong citation.
- Versioning.
- Jurisdiction metadata.
- Access control.
- Refusal on insufficient evidence.
- Human review for high-risk answers.

### 47. Design a RAG system for customer support.

Key points:

- Product/version metadata.
- Ticket context.
- Escalation policy.
- Tone control.
- Feedback loop from resolved tickets.

### 48. Design a RAG system for codebase Q&A.

Key points:

- Symbol-aware chunking.
- Hybrid retrieval.
- Repository structure metadata.
- Link answers to files and line ranges.
- Avoid stale code references.

### 49. Design a RAG system for research papers.

Key points:

- Section-aware parsing.
- Citation graph.
- Method and experiment extraction.
- Comparison across papers.
- Uncertainty and limitation reporting.

### 50. How would you know your RAG system is production-ready?

Key points:

- Clear evaluation set and passing thresholds.
- Permission tests.
- Monitoring and alerts.
- Freshness pipeline.
- Citation validation.
- Cost and latency budgets.
- Human escalation path.

