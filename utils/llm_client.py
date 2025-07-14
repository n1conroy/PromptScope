import os
from dotenv import load_dotenv

load_dotenv()

def get_llm_response(prompt: str, provider: str = "openai") -> str:
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        # Replace with real OpenAI call
        return f"[OpenAI mock] {prompt}"
    elif provider == "claude":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        # Replace with real Claude API call
        return f"[Claude mock] {prompt}"
    else:
        return "Unknown provider"
