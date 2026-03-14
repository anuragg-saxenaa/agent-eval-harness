import os


def run_scenario(scenario: dict, model: str = "gpt-4o") -> str:
    """Call LLM with scenario input and return actual output."""
    try:
        import openai
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": scenario["input"]}],
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR: {e}"
