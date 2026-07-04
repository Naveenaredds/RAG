import os

def load_documents(folder_path="data"):
    documents = []
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created empty '{folder_path}' directory. Please add some .txt files there!")
        return documents
        
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())
    return documents
