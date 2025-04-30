import streamlit as st
from app import load_resume, run_rag_pipeline  # Adjust based on app.py functions

st.title("📄 Smart Resume Generator")
st.markdown("This app generates optimized resumes using LLM + RAG.")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
uploaded_jd = st.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

if st.button("Generate Resume"):
    if uploaded_resume and uploaded_jd:
        resume_json = load_resume(uploaded_resume)
        result = run_rag_pipeline(resume_json, uploaded_jd)
        st.success("Resume generated successfully!")
        st.json(result)
    else:
        st.warning("Please upload both resume and job description.")

import json

if result:
    st.download_button(
        label="Download JSON",
        data=json.dumps(result, indent=2),
        file_name="optimized_resume.json",
        mime="application/json"
    )
