from src.rag_app.llm import generate_answer

from src.rag_app.loader import load_documents
from src.rag_app.chunker import chunk_documents
from src.rag_app.embeddings import create_embeddings
from src.rag_app.vector_store import create_faiss_index
from src.rag_app.retriever import retrieve
from src.rag_app.prompt import build_prompt
# ------------------------
# Ingestion Phase
# ------------------------

documents = load_documents("data")

chunks = chunk_documents(documents)

texts, embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

print("Knowledge Base Loaded Successfully!")
# ------------------------
# Query Phase
# ------------------------

while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    retrieved_chunks = retrieve(
        question,
        index,
        texts,
        top_k=3
    )

    prompt = build_prompt(
        retrieved_chunks,
        question
    )

    print("\nPrompt sent to LLM:\n")
    print(prompt)
# Your existing code line:
    print("\nPrompt sent to LLM:\n", prompt)

# PASTE THESE TWO NEW LINES RIGHT HERE:
    print("\nGenerating final answer from Llama model...")
    answer = generate_answer(prompt)
    print(f"\nAnswer:\n{answer}\n" + "="*50)