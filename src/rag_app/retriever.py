import numpy as np
from src.rag_app.embeddings import model

def retrieve(question, index, texts, top_k=3):
    if index is None or not texts:
        return ["No context available."]
        
    # Vectorize the user query
    query_vector = model.encode([question]).astype('float32')
    
    # Query FAISS index for closest matching chunks
    distances, indices = index.search(query_vector, min(top_k, len(texts)))
    
    retrieved_chunks = [texts[idx] for idx in indices[0] if idx != -1]
    return retrieved_chunks