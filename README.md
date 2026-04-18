# agent-eval-harness

**YAML-defined LLM agent evaluation framework with regression detection.**

Define test scenarios in YAML, run against any model (OpenAI, Anthropic, or local), get pass/fail scores and HTML reports. Detects when agent quality degrades across runs.

## Install

```bash
pip install -r requirements.txt
# or
pip install -e ".[dev]"    # with test tooling
```

## Quick Start

```bash
# Set API key
export OPENAI_API_KEY=sk-...

# Run eval suite
python cli.py run --suite scenarios/ --model gpt-4o

# Dry run (no API calls, uses mock output)
python cli.py run --suite scenarios/ --dry-run

# HTML report
python cli.py run --suite scenarios/ --model gpt-4o --output report.html
```

## Scenario Format

```yaml
id: greet-alice
input: "Say hello to Alice"
expected: "Hello, Alice"
scoring:
  method: semantic_similarity   # exact_match | contains | semantic_similarity
  threshold: 0.85
```

```yaml
id: math-quick
input: "What is 17 * 23?"
expected: "391"
scoring:
  method: exact_match
```

## Scoring Methods

| Method | Description |
|--------|-------------|
| `exact_match` | Case-insensitive string match |
| `contains` | Expected substring appears in actual output |
| `semantic_similarity` | Sequence similarity ratio (0–1) via difflib |

## Architecture

```
agent_eval/
  loader.py    — YAML scenario loader
  runner.py    — LLM API runner (OpenAI + Anthropic)
  scorer.py    — Scoring engine (3 methods)
  reporter.py  — JSON + HTML report generator
scenarios/
  greet.yaml
  math.yaml
tests/
  test_*.py    — pytest suite
cli.py         — entry point
```

## Test

```bash
pytest tests/ -v
```

## License

MIT
