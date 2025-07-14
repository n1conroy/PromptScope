import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="EchoPrompt", layout="wide")
st.title("🗣️ EchoPrompt")
st.markdown("**Visualize, structure, and export LLM insights for research and instruction.**")

with st.expander("⚙️ Prompt Settings"):
    prompt = st.text_area("Enter your prompt:", "Explain the importance of information literacy.")
    style = st.selectbox("Choose response style", ["neutral", "formal", "casual"])
    provider = st.selectbox("Select LLM Provider", ["openai", "claude"])
    user_id = st.text_input("User ID", "anonymous")
    use_gcp = st.checkbox("Export to GCP (BigQuery + GCS)", value=True)

if st.button("🚀 Generate"):
    with st.spinner("Waiting for EchoPrompt backend..."):
        try:
            res = requests.post("http://localhost:8000/generate", json={
                "prompt": prompt,
                "style": style,
                "llm_provider": provider,
                "user_id": user_id,
                "use_gcp_export": use_gcp
            })
            res.raise_for_status()
            data = res.json()

            st.subheader("📝 LLM Response")
            st.code(data["response"], language="markdown")

            st.subheader("🔠 Token Analysis")
            df = pd.DataFrame(data["tokens"])
            st.dataframe(df)

            st.subheader("📈 Sentiment")
            st.metric("Polarity", round(data["sentiment"]["polarity"], 3))
            st.metric("Subjectivity", round(data["sentiment"]["subjectivity"], 3))

        except Exception as e:
            st.error(f"Backend error: {e}")
