"""Tests for agent_eval.runner."""
import pytest
from unittest.mock import patch
from agent_eval.runner import run_scenario


class TestRunner:
    @patch("openai.OpenAI")
    def test_run_scenario_success(self, mock_client):
        mock_resp = type("obj", (), {"choices": [type("obj", (), {"message": type("obj", (), {"content": "42"})()})()]})()
        mock_client.return_value.chat.completions.create.return_value = mock_resp

        scenario = {"id": "test", "input": "What is 2+2?"}
        result = run_scenario(scenario, "gpt-4o")
        assert result == "42"

    @patch("openai.OpenAI")
    def test_run_scenario_api_error(self, mock_client):
        mock_client.return_value.chat.completions.create.side_effect = Exception("API error")

        scenario = {"id": "test", "input": "What is 2+2?"}
        result = run_scenario(scenario, "gpt-4o")
        assert "ERROR" in result
