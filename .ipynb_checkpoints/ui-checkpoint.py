import streamlit as st
import os
from src.rag_app.loader import load_documents
from src.rag_app.chunker import chunk_documents
from src.rag_app.embeddings import create_embeddings
from src.rag_app.vector_store import create_faiss_index
from src.rag_app.retriever import retrieve
from src.rag_app.prompt import build_prompt
from src.rag_app.llm import generate_answer

st.set_page_config(page_title="Local PDF RAG Assistant", layout="wide")
st.title("📚 Local Document RAG Assistant (Llama 3.2)")

if "index" not in st.session_state:
    st.session_state.index = None
if "texts" not in st.session_state:
    st.session_state.texts = []

with st.sidebar:
    st.header("Storage Settings")
    
    # 1. This forces a complete memory wipe
    if st.button("🧹 Clear Old Application Cache"):
        st.cache_data.clear()
        st.session_state.index = None
        st.session_state.texts = []
        st.success("App Cache Cleared Completely!")
        
    # 2. This reads the files clean from disk
    if st.button("🔄 Build/Refresh Knowledge Base"):
        with st.spinner("Re-reading data folder from disk..."):
            docs = load_documents("data")
            if not docs:
                st.warning("No files found in 'data/' folder!")
            else:
                chunks = chunk_documents(docs)
                texts, embeddings = create_embeddings(chunks)
                st.session_state.index = create_faiss_index(embeddings)
                st.session_state.texts = texts
                st.success(f"Success! Indexed {len(chunks)} total text fragments.")

st.write("Ask your local Llama model questions based on information inside your data documents.")
question = st.text_input("Enter your question here:")

if question:
    if st.session_state.index is None:
        st.error("Please click 'Build/Refresh Knowledge Base' in the sidebar first!")
    else:
        with st.spinner("Searching context and generating answer..."):
            retrieved = retrieve(question, st.session_state.index, st.session_state.texts)
            prompt = build_prompt(retrieved, question)
            answer = generate_answer(prompt)
            
            st.subheader("💡 AI Answer:")
            st.write(answer)
            
            with st.expander("🔍 View Retrieved Context Fragments Used"):
                for idx, chunk in enumerate(retrieved):
                    st.markdown(f"**Fragment {idx+1}:**\n{chunk}\n---")