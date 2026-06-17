#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

echo "Running minimal agent framework demo..."
python3 examples/minimal-agent-framework/run_demo.py

echo
echo "Running minimal agent framework tests..."
python3 -m unittest discover examples/minimal-agent-framework/tests

echo
echo "Running LLM eval harness demo..."
python3 examples/llm-eval-harness/run_eval.py

echo
echo "Running LLM eval harness report export..."
python3 examples/llm-eval-harness/run_eval.py --report /tmp/llm-eval-report.json

echo
echo "Running LLM eval harness tests..."
python3 -m unittest discover examples/llm-eval-harness/tests

echo
echo "All examples passed."
