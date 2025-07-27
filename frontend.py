import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8889"

st.title("🧠 Web Automation Dashboard")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

file_type = None
if uploaded_file:
    file_type = "csv" if uploaded_file.name.endswith(".csv") else "xlsx"

if st.button("🚀 Start Automating") and uploaded_file:
    with st.spinner("Running automation..."):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post(f"{API_URL}/upload-and-process/?file_type={file_type}", files={"file": uploaded_file})
        
        if res.status_code == 200:
            data = res.json()
            st.success(f"✅ Processed {data['processed_rows']} rows.")
            st.download_button(
                "📥 Download Updated File",
                requests.get(f"{API_URL}/download/").content,
                file_name="Updated.xlsx"
            )
        else:
            st.error("❌ Something went wrong. Check server logs.")
