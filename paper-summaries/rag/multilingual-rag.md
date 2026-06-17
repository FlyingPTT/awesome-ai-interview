# Multilingual Retrieval-Augmented Generation

Paper: [arXiv:2504.03616](https://arxiv.org/abs/2504.03616)

## Problem

RAG works well in English-heavy settings, but multilingual retrieval introduces coverage, translation, and cross-lingual consistency issues.

## Method

The paper studies multilingual RAG strategies, including question translation, direct multilingual retrieval, and translating retrieved documents into a common language before generation.

## Why It Matters

Many production RAG systems serve multilingual users. Retrieval, citation, and grounding must be evaluated per language rather than assumed to transfer.

## Implementation Notes

- Evaluate retrieval by language.
- Preserve original source language for citation.
- Translation can improve generation but may introduce errors.
- Cross-lingual retrieval requires careful embedding and indexing choices.

## Interview Talking Points

- Multilingual RAG is not just English RAG plus translation.
- Cross-lingual retrieval can create inconsistent evidence.
- Language-specific evaluation is required.

