"""Tests for agent_eval.scorer."""
import pytest
from agent_eval.scorer import score


class TestScorer:
    def test_exact_match_pass(self):
        r = score("hello world", "Hello World", "exact_match", 0.85)
        assert r["passed"] is True
        assert r["score"] == 1.0

    def test_exact_match_fail(self):
        r = score("hello world", "Goodbye", "exact_match", 0.85)
        assert r["passed"] is False
        assert r["score"] == 0.0

    def test_contains_pass(self):
        r = score("The answer is 42", "42", "contains", 0.0)
        assert r["passed"] is True

    def test_contains_fail(self):
        r = score("The answer is 42", "43", "contains", 0.0)
        assert r["passed"] is False

    def test_semantic_similarity_pass(self):
        r = score("Hello, Alice!", "Hello Alice", "semantic_similarity", 0.6)
        assert r["passed"] is True
        assert 0.0 < r["score"] <= 1.0

    def test_semantic_similarity_fail(self):
        r = score("Goodbye forever", "Hello Alice", "semantic_similarity", 0.95)
        assert r["passed"] is False

    def test_unknown_method(self):
        r = score("foo", "bar", "unknown_method", 0.85)
        assert r["passed"] is False
        assert "error" in r
