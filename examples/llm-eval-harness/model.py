from __future__ import annotations

import json


class MockModel:
    """A deterministic model client for local evaluation harness demos."""

    name = "mock-model-v1"

    def generate(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        if "json" in prompt_lower:
            return json.dumps({"answer": "RAG combines retrieval and generation.", "confidence": 0.87})
        if "private salary" in prompt_lower:
            return "I cannot provide private personal information without a valid source and permission."
        if "rag" in prompt_lower:
            return "RAG combines retrieval with generation so answers can be grounded in external evidence."
        return "I do not have enough information to answer."

