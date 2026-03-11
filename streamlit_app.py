import os
import streamlit as st
import requests

API_URL = os.environ.get("API_URL", "https://mini-query-engine-1.onrender.com")
API_KEY = os.environ.get("API_KEY", "secure_api_key_123")

st.set_page_config(page_title="Mini Query Engine UI", page_icon="🔍")

st.title("Mini Data Query Simulation Engine")

st.markdown("Enter a natural language query and submit to see the pseudo-SQL and store it in the query log.")

query_input = st.text_area("Natural language query", height=120)

col1, col2 = st.columns(2)

with col1:
    if st.button("Submit Query"):
        if not query_input.strip():
            st.warning("Please enter a query.")
        else:
            try:
                headers = {"api_key": API_KEY, "api-key": API_KEY, "X-API-Key": API_KEY}
                payload = {"natural_language_query": query_input}
                resp = requests.post(f"{API_URL}/query", json=payload, headers=headers, timeout=5)
                resp.raise_for_status()
                data = resp.json()
                st.success("Query processed")
                st.code(data.get("pseudo_sql_query", ""))
            except Exception as e:
                st.error(f"Request failed: {e}")

with col2:
    st.markdown("Check saved query details by ID")
    qid = st.number_input("Query ID", min_value=1, value=1, step=1)
    if st.button("Explain Query"):
        try:
            headers = {"api_key": API_KEY, "api-key": API_KEY, "X-API-Key": API_KEY}
            resp = requests.get(f"{API_URL}/explain/{qid}", headers=headers, timeout=5)
            resp.raise_for_status()
            st.info(resp.json().get("explanation", "No explanation"))
        except Exception as e:
            st.error(f"Request failed: {e}")

    if st.button("Validate Query"):
        try:
            headers = {"api_key": API_KEY, "api-key": API_KEY, "X-API-Key": API_KEY}
            resp = requests.get(f"{API_URL}/validate/{qid}", headers=headers, timeout=5)
            resp.raise_for_status()
            st.success(resp.json().get("validation", "No validation info"))
        except Exception as e:
            st.error(f"Request failed: {e}")

st.markdown("---")
st.markdown("**Run instructions:** Start the backend API first, then click `Open app` to open Streamlit.")

st.markdown("**Backend**: `uvicorn app.main:app --reload`")
st.markdown("**Streamlit**: `streamlit run streamlit_app.py`")
