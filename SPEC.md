# agent-eval-harness — SPEC.md

## Overview
An automated evaluation framework for LLM agents. Define test scenarios with expected outputs and scoring rubrics, then run regression suites against any agent.

## Problem
LLM agent quality degrades silently:
- No standard way to test agent behavior changes
- Prompt tweaks break other scenarios unexpectedly
- Manual testing doesn't scale
- Hard to measure "did this agent get better?"

## Solution
A Python framework for defining, running, and scoring agent evaluations.

## Features
- **Test scenarios** — YAML-defined inputs + expected outputs
- **Scoring rubrics** — exact match, contains, semantic similarity
- **Multi-provider support** — OpenAI + Anthropic
- **HTML + JSON reports** — visual pass/fail breakdown
- **CI integration** — exit code reflects regression, GitHub Actions ready

## Tech Stack
- Python 3.10+
- openai + anthropic (API clients)
- PyYAML (scenario definitions)
- MIT license

## Scenario Format
```yaml
id: greet-user
input: "Say hello to Alice"
expected: "Hello, Alice"
scoring:
  method: semantic_similarity
  threshold: 0.85
```

## Scoring Methods
| Method | Description |
|--------|-------------|
| `exact_match` | Exact string match (case-insensitive) |
| `contains` | Expected string appears in actual output |
| `semantic_similarity` | Sequence similarity ratio via difflib (0–1) |

## CLI
```bash
# Run eval suite against OpenAI
python cli.py run --suite scenarios/ --model gpt-4o

# Dry run (no API calls, uses mock output)
python cli.py run --suite scenarios/ --dry-run

# Output HTML or JSON report
python cli.py run --suite scenarios/ --model gpt-4o --output report.html
```

## MVP Scope
- [x] YAML scenario loader
- [x] Runner for OpenAI + Anthropic
- [x] Exact match + contains + semantic similarity scoring
- [x] CLI: `agent-eval run --suite scenarios/ --model gpt-4o`
- [x] JSON + HTML report output
- [x] GitHub Actions CI workflow
- [x] pytest suite

## Ready: Yes
