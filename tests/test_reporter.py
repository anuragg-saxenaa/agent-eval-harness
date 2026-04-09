"""Tests for agent_eval.reporter."""
import tempfile
import json
from pathlib import Path
from agent_eval.reporter import generate_report


class TestReporter:
    def test_generate_report_json(self):
        results = [
            {"id": "t1", "input": "a", "expected": "b", "actual": "b", "passed": True, "score": 1.0},
            {"id": "t2", "input": "c", "expected": "d", "actual": "x", "passed": False, "score": 0.0},
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            tmp = f.name
        try:
            report = generate_report(results, tmp)
            assert report["summary"]["total"] == 2
            assert report["summary"]["passed"] == 1
            assert report["summary"]["pass_rate"] == 0.5
            with open(tmp) as f:
                data = json.load(f)
            assert data["summary"]["total"] == 2
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_generate_report_html(self):
        results = [{"id": "t1", "input": "hello", "expected": "hi", "actual": "hi", "passed": True, "score": 1.0}]
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
            tmp = f.name
        try:
            generate_report(results, tmp)
            html = Path(tmp).read_text()
            assert "Agent Eval Report" in html
            assert "100.0%" in html
        finally:
            Path(tmp).unlink(missing_ok=True)
