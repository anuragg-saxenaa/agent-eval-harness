# agent-eval-harness

Lightweight evaluation framework for LLM agents. Define scenarios in YAML, run against any model, get pass/fail scores and HTML reports.

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

## Usage

```bash
# Run eval suite
python cli.py run --suite scenarios/ --model gpt-4o

# Dry run (no API calls)
python cli.py run --suite scenarios/ --dry-run

# Output HTML report
python cli.py run --suite scenarios/ --model gpt-4o --output report.html
```

## Scenario Format

```yaml
id: greet-alice
input: "Say hello to Alice"
expected: "Hello, Alice"
scoring:
  method: semantic_similarity   # or exact_match, contains
  threshold: 0.85
```

## Scoring Methods

| Method | Description |
|--------|-------------|
| `exact_match` | Exact string match (case-insensitive) |
| `contains` | Expected string appears in actual output |
| `semantic_similarity` | Sequence similarity ratio (0–1) |
