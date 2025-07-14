from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from utils.llm_client import get_llm_response
from visualizations.token_analysis import analyze_tokens
from visualizations.sentiment import get_sentiment

app = FastAPI(title="EchoPrompt")

class PromptRequest(BaseModel):
    prompt: str
    llm_provider: Optional[str] = "openai"
    style: Optional[str] = "neutral"

@app.post("/generate")
async def generate_response(req: PromptRequest):
    styled_prompt = f"[Style: {req.style}]\n{req.prompt}"
    response = get_llm_response(styled_prompt, provider=req.llm_provider)
    tokens = analyze_tokens(response)
    sentiment = get_sentiment(response)
    return {
        "response": response,
        "tokens": tokens,
        "sentiment": sentiment
    }

@app.get("/")
async def root():
    return {"message": "EchoPrompt API is live"}
