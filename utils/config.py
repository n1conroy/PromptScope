import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        "GCP_PROJECT_ID": os.getenv("GCP_PROJECT_ID"),
        "GCP_BUCKET_NAME": os.getenv("GCP_BUCKET_NAME"),
        "BIGQUERY_DATASET": os.getenv("BIGQUERY_DATASET"),
        "BIGQUERY_TABLE": os.getenv("BIGQUERY_TABLE"),
    }
