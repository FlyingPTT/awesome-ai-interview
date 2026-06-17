#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

echo "Running minimal agent framework demo..."
python3 examples/minimal-agent-framework/run_demo.py

echo
echo "Running LLM eval harness demo..."
python3 examples/llm-eval-harness/run_eval.py

echo
echo "All examples passed."

