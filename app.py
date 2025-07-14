from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from utils.llm_client import get_llm_response
from visualizations.token_analysis import analyze_tokens
from visualizations.sentiment import get_sentiment
from utils.gcp_exporter import export_to_bigquery, export_to_gcs
from datetime import datetime

app = FastAPI(title="EchoPrompt")

class PromptRequest(BaseModel):
    prompt: str
    llm_provider: Optional[str] = "openai"
    style: Optional[str] = "neutral"
    user_id: Optional[str] = "anonymous"
    use_gcp_export: Optional[bool] = True

@app.post("/generate")
async def generate_response(req: PromptRequest):
    styled_prompt = f"[Style: {req.style}]\n{req.prompt}"
    response = get_llm_response(styled_prompt, provider=req.llm_provider)
    tokens = analyze_tokens(response)
    sentiment = get_sentiment(response)

    session_data = {
        "user_id": req.user_id,
        "prompt": req.prompt,
        "provider": req.llm_provider,
        "style": req.style,
        "response": response,
        "tokens": tokens,
        "sentiment": sentiment,
        "timestamp": datetime.utcnow().isoformat()
    }

    if req.use_gcp_export:
        export_to_bigquery(session_data)
        export_to_gcs(session_data)

    return session_data

@app.get("/")
async def root():
    return {"message": "EchoPrompt API is running"}
