import urllib.request
import json

def generate_answer(prompt, model_name="llama3.2:3b"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(data).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data.get("response", "No response generated.")
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}. Make sure Ollama is running!"
