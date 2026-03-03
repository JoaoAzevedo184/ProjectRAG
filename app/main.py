from fastapi import FastAPI
from .chat import ask

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(data: dict):
    question = data.get("question")
    answer = ask(question)
    return {"answer": answer}