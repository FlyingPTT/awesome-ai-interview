from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rag import MiniRAG, tokenize


class MiniRAGTests(unittest.TestCase):
    def setUp(self):
        self.rag = MiniRAG.from_directory(ROOT / "docs")

    def test_tokenize(self):
        self.assertEqual(tokenize("RAG, evaluation!"), ["rag", "evaluation"])

    def test_retrieve_rag_document(self):
        results = self.rag.retrieve("retrieval generation citations")
        self.assertEqual(results[0].document.doc_id, "rag")

    def test_retrieve_modes(self):
        sparse = self.rag.retrieve("retrieval generation citations", mode="sparse")
        dense = self.rag.retrieve("retrieval generation citations", mode="dense")
        hybrid = self.rag.retrieve("retrieval generation citations", mode="hybrid")

        self.assertTrue(sparse)
        self.assertTrue(dense)
        self.assertTrue(hybrid)
        self.assertGreaterEqual(hybrid[0].score, hybrid[0].sparse_score)

    def test_answer_has_citation(self):
        result = self.rag.answer("How should RAG systems be evaluated?")
        self.assertTrue(result["citations"])
        self.assertIn("[source:", result["answer"])
        self.assertEqual(result["retrieval_mode"], "hybrid")

    def test_refusal_when_no_evidence(self):
        result = self.rag.answer("What is Alice private salary?", min_score=1.0)
        self.assertEqual(result["citations"], [])
        self.assertIn("not have enough evidence", result["answer"])

    def test_unknown_retrieval_mode_raises(self):
        with self.assertRaises(ValueError):
            self.rag.retrieve("rag", mode="unknown")


if __name__ == "__main__":
    unittest.main()
