from sentence_transformers import SentenceTransformer

# Uses a small, high-performance local open-source embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    if not chunks:
        return [], None
    embeddings = model.encode(chunks)
    return chunks, embeddings
