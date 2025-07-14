# EchoPrompt

**Visualize, structure, and export LLM insights for research and instruction.**

EchoPrompt is a practical toolkit designed for librarians, educators, and digital researchers exploring the capabilities of large language models (LLMs). It combines prompt analysis, natural language enrichment, and structured metadata output with integrations into Google Cloud services — supporting instructional use, research data management, and reproducibility.

---

## Use Cases

- **Librarians** developing programming around AI literacy and metadata design
- **Instructors** teaching responsible AI use in humanities, social science, or communications
- **Researchers** analyzing model behavior for transparency, ethics, or NLP education
- **Archivists and metadata professionals** prototyping automatic schema or subject classification tools

---

## 🔍 Features

- ✍️ Prompt styling (neutral, formal, casual)
- Multi-LLM provider support (OpenAI, Claude)
- Token-level response analysis
- Sentiment scoring for tone tracking
- **Export response metadata and analysis to BigQuery**
- Save and structure prompt history in GCS for reproducible workflows
- JSON, CSV, and GCP logging for digital scholarship audit trails
- Modular utilities for NLP, classification, and summarization (extendable)

---

## 🚀 Quickstart

```bash
git clone https://github.com/yourname/echoprompt
cd echoprompt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m textblob.download_corpora
uvicorn app:app --reload
