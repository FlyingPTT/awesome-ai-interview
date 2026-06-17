from __future__ import annotations

import json

from router import ModelRouter, answer_with_route


def main() -> None:
    tasks = [
        "Format this JSON response.",
        "Design a multi-step RAG evaluation system.",
        "Answer a legal question about a contract.",
    ]
    for task in tasks:
        print(json.dumps(answer_with_route(task), indent=2))

    fallback = ModelRouter().route_with_fallback(
        "Format this JSON response.",
        small_model_confidence=0.42,
    )
    print(
        json.dumps(
            {
                "task": "Format this JSON response with low confidence.",
                "model": fallback.model.name,
                "reason": fallback.reason,
                "route_path": list(fallback.route_path),
                "fallback_used": fallback.fallback_used,
                "estimated_cost_usd": fallback.estimated_cost_usd,
                "estimated_latency_ms": fallback.estimated_latency_ms,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
