from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelProfile:
    name: str
    quality: str
    input_price_per_1k: float
    output_price_per_1k: float
    latency_ms: int

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        return round(
            input_tokens / 1000 * self.input_price_per_1k
            + output_tokens / 1000 * self.output_price_per_1k,
            8,
        )


@dataclass(frozen=True)
class RouteDecision:
    model: ModelProfile
    reason: str
    estimated_cost_usd: float
    estimated_latency_ms: int
    route_path: tuple[str, ...]
    fallback_used: bool = False


SMALL_MODEL = ModelProfile(
    name="small-fast-model",
    quality="good for simple classification, formatting, and extraction",
    input_price_per_1k=0.0002,
    output_price_per_1k=0.0006,
    latency_ms=120,
)

LARGE_MODEL = ModelProfile(
    name="large-reasoning-model",
    quality="better for complex reasoning, ambiguous tasks, and high-risk answers",
    input_price_per_1k=0.002,
    output_price_per_1k=0.006,
    latency_ms=650,
)


class ModelRouter:
    def route(self, task: str, input_tokens: int = 200, output_tokens: int = 120) -> RouteDecision:
        task_lower = task.lower()
        high_risk_markers = ["medical", "legal", "financial", "private", "delete", "security"]
        complex_markers = ["design", "debug", "multi-step", "reason", "compare", "architecture"]

        if any(marker in task_lower for marker in high_risk_markers):
            model = LARGE_MODEL
            reason = "high-risk task needs stronger reasoning and safer behavior"
        elif any(marker in task_lower for marker in complex_markers):
            model = LARGE_MODEL
            reason = "complex task needs stronger reasoning"
        else:
            model = SMALL_MODEL
            reason = "simple task can use cheaper, faster model"

        return RouteDecision(
            model=model,
            reason=reason,
            estimated_cost_usd=model.estimate_cost(input_tokens, output_tokens),
            estimated_latency_ms=model.latency_ms,
            route_path=(model.name,),
        )

    def route_with_fallback(
        self,
        task: str,
        small_model_confidence: float = 0.8,
        input_tokens: int = 200,
        output_tokens: int = 120,
    ) -> RouteDecision:
        initial = self.route(task, input_tokens=input_tokens, output_tokens=output_tokens)
        if initial.model == LARGE_MODEL:
            return initial

        if small_model_confidence >= 0.7:
            return initial

        total_cost = SMALL_MODEL.estimate_cost(input_tokens, output_tokens) + LARGE_MODEL.estimate_cost(
            input_tokens, output_tokens
        )
        return RouteDecision(
            model=LARGE_MODEL,
            reason="small model confidence below threshold; escalated to stronger model",
            estimated_cost_usd=round(total_cost, 8),
            estimated_latency_ms=SMALL_MODEL.latency_ms + LARGE_MODEL.latency_ms,
            route_path=(SMALL_MODEL.name, LARGE_MODEL.name),
            fallback_used=True,
        )


def answer_with_route(task: str) -> dict[str, object]:
    decision = ModelRouter().route_with_fallback(task)
    return {
        "task": task,
        "model": decision.model.name,
        "reason": decision.reason,
        "estimated_cost_usd": decision.estimated_cost_usd,
        "estimated_latency_ms": decision.estimated_latency_ms,
        "model_quality": decision.model.quality,
        "route_path": list(decision.route_path),
        "fallback_used": decision.fallback_used,
    }
