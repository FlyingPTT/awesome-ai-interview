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
echo "Running RAG mini system demo..."
python3 examples/rag-mini-system/run_demo.py

echo
echo "Running RAG mini system tests..."
python3 -m unittest discover examples/rag-mini-system/tests

echo
echo "Running model router demo..."
python3 examples/model-router/run_demo.py

echo
echo "Running model router tests..."
python3 -m unittest discover examples/model-router/tests

echo
echo "Running RAG eval set..."
python3 examples/rag-eval-set/evaluate.py --report /tmp/rag-eval-report.json

echo
echo "Running RAG eval set tests..."
python3 -m unittest discover examples/rag-eval-set/tests

echo
echo "Running coding agent mini demo..."
python3 examples/coding-agent-mini/run_demo.py

echo
echo "Running coding agent mini tests..."
python3 -m unittest discover examples/coding-agent-mini/tests

echo
echo "All examples passed."
