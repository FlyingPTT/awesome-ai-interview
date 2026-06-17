from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path


TOKEN_RE = re.compile(r"[a-zA-Z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


@dataclass(frozen=True)
class Document:
    doc_id: str
    title: str
    text: str
    path: str


@dataclass(frozen=True)
class ScoredDocument:
    document: Document
    score: float


class MiniRAG:
    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents
        self.doc_tokens = {doc.doc_id: tokenize(doc.text) for doc in documents}
        self.document_frequency = self._document_frequency()

    @classmethod
    def from_directory(cls, path: Path) -> "MiniRAG":
        documents = []
        for file_path in sorted(path.glob("*.md")):
            text = file_path.read_text(encoding="utf-8")
            title = text.splitlines()[0].lstrip("# ").strip() if text.splitlines() else file_path.stem
            documents.append(
                Document(
                    doc_id=file_path.stem,
                    title=title,
                    text=text,
                    path=str(file_path),
                )
            )
        return cls(documents)

    def _document_frequency(self) -> dict[str, int]:
        df: dict[str, int] = {}
        for tokens in self.doc_tokens.values():
            for token in set(tokens):
                df[token] = df.get(token, 0) + 1
        return df

    def retrieve(self, query: str, top_k: int = 3) -> list[ScoredDocument]:
        query_tokens = tokenize(query)
        scored = []
        for doc in self.documents:
            score = self._score(query_tokens, self.doc_tokens[doc.doc_id])
            if score > 0:
                scored.append(ScoredDocument(doc, score))
        return sorted(scored, key=lambda item: item.score, reverse=True)[:top_k]

    def _score(self, query_tokens: list[str], doc_tokens: list[str]) -> float:
        if not query_tokens or not doc_tokens:
            return 0.0
        score = 0.0
        doc_len = len(doc_tokens)
        avg_len = sum(len(tokens) for tokens in self.doc_tokens.values()) / len(self.doc_tokens)
        for token in query_tokens:
            term_frequency = doc_tokens.count(token)
            if term_frequency == 0:
                continue
            df = self.document_frequency.get(token, 0)
            idf = math.log((len(self.documents) - df + 0.5) / (df + 0.5) + 1)
            numerator = term_frequency * 2.2
            denominator = term_frequency + 1.2 * (0.25 + 0.75 * doc_len / avg_len)
            score += idf * numerator / denominator
        return score

    def answer(self, query: str, min_score: float = 0.15) -> dict[str, object]:
        retrieved = self.retrieve(query)
        if not retrieved or retrieved[0].score < min_score:
            return {
                "answer": "I do not have enough evidence in the local documents to answer.",
                "citations": [],
                "retrieved": [],
            }

        best = retrieved[0].document
        answer = self._synthesize(query, best)
        return {
            "answer": f"{answer} [source:{best.doc_id}]",
            "citations": [{"doc_id": best.doc_id, "title": best.title, "path": best.path}],
            "retrieved": [
                {"doc_id": item.document.doc_id, "score": round(item.score, 4)}
                for item in retrieved
            ],
        }

    def _synthesize(self, query: str, doc: Document) -> str:
        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", doc.text) if part.strip()]
        body_sentences = [sentence for sentence in sentences if not sentence.startswith("#")]
        if body_sentences:
            return body_sentences[0]
        return doc.text.replace("\n", " ").strip()

