import os
from pypdf import PdfReader

def load_documents(folder_path="data"):
    documents = []
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return documents
        
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Read text files
        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())
                
        # Read PDF files
        elif filename.endswith(".pdf"):
            try:
                reader = PdfReader(file_path)
                pdf_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        pdf_text += text + "\n"
                if pdf_text.strip():
                    documents.append(pdf_text)
            except Exception as e:
                print(f"Error reading PDF {filename}: {e}")
                
    return documents
