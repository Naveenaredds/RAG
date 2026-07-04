import faiss
import numpy as np

def create_faiss_index(embeddings):
    if embeddings is None or len(embeddings) == 0:
        return None
    embeddings_array = np.array(embeddings).astype('float32')
    
    if len(embeddings_array.shape) == 1:
        dimension = embeddings_array.shape[0]
        embeddings_array = np.expand_dims(embeddings_array, axis=0)
    else:
        dimension = embeddings_array.shape[1]
        
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_array)
    return index