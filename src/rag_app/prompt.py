def build_prompt(retrieved_chunks, question):
    context = "\n---\n".join(retrieved_chunks)
    
    prompt = f"""
You are a helpful AI assistant. Answer the user's question using only the provided context below. If you do not know the answer based on the context, state that you don't know.

Context:
{context}

Question: {question}
Answer:
"""
    return prompt.strip()