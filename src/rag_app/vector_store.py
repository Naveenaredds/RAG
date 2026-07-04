import faiss
import numpy as np

def create_faiss_index(embeddings):
    if embeddings is None or len(embeddings) == 0:
        return None
    # Convert embeddings list to a regular float32 numpy array
    embeddings_array = np.array(embeddings).astype('float32')
    dimension = embeddings_array.shape[1]
    
    # Initialize and populate the FAISS Index
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_array)
    return index