import os
import streamlit as st
from document_parser import extract_text_from_pdf
from vector_store import build_faiss_store
from chat_engine import build_chat_chain

st.set_page_config(page_title="📚 StudySage - Offline AI Assistant")
st.title("📚 StudySage - Your Offline AI Study Assistant")

uploaded_file = st.file_uploader("Upload a PDF note/chapter", type="pdf")
query = st.text_input("Ask a question from your uploaded material")

if uploaded_file and query:
    with open(f"data/uploaded_docs/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf(f"data/uploaded_docs/{uploaded_file.name}")
    vs = build_faiss_store([text])
    qa = build_chat_chain(vs)
    answer = qa.run(query)
    st.success("💡 Answer: ")
    st.write(answer)