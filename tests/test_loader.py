"""Tests for agent_eval.loader."""
import tempfile
import os
from pathlib import Path
from agent_eval.loader import load_scenarios


class TestLoader:
    def test_load_scenarios(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir)
            (path / "test.yaml").write_text(
                "id: test-scenario\n"
                "input: 'Say hi'\n"
                "expected: 'Hi there'\n"
                "scoring:\n"
                "  method: exact_match\n"
                "  threshold: 0.9\n"
            )
            scenarios = load_scenarios(str(tmpdir))
            assert len(scenarios) == 1
            assert scenarios[0]["id"] == "test-scenario"
            assert scenarios[0]["expected"] == "Hi there"
            assert scenarios[0]["scoring"]["method"] == "exact_match"

    def test_load_multiple(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir)
            (path / "a.yaml").write_text("id: a\ninput: a\nexpected: a\nscoring:\n  method: exact_match\n")
            (path / "b.yaml").write_text("id: b\ninput: b\nexpected: b\nscoring:\n  method: exact_match\n")
            scenarios = load_scenarios(str(tmpdir))
            assert len(scenarios) == 2
            ids = {s["id"] for s in scenarios}
            assert ids == {"a", "b"}
