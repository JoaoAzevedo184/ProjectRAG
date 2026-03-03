import os
import google.generativeai as genai
import requests

USE_LOCAL = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"

# GEMINI
def ask_gemini(prompt):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# OLLAMA LOCAL
def ask_local(prompt):
    response = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]