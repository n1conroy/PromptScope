from google.cloud import bigquery, storage
import os
import json
from utils.config import get_config

def export_to_bigquery(session_data: dict):
    config = get_config()
    client = bigquery.Client(project=config["GCP_PROJECT_ID"])
    table_id = f"{config['GCP_PROJECT_ID']}.{config['BIGQUERY_DATASET']}.{config['BIGQUERY_TABLE']}"
    errors = client.insert_rows_json(table_id, [session_data])
    if errors:
        print("BigQuery insert errors:", errors)

def export_to_gcs(session_data: dict):
    config = get_config()
    client = storage.Client(project=config["GCP_PROJECT_ID"])
    bucket = client.bucket(config["GCP_BUCKET_NAME"])
    filename = f"echoprompt_{session_data['timestamp']}.json"
    blob = bucket.blob(filename)
    blob.upload_from_string(json.dumps(session_data), content_type="application/json")
