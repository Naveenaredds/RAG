def chunk_documents(documents, chunk_size=500, overlap=50):
    chunks = []
    for doc in documents:
        words = doc.split()
        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i:i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)
    return chunks
