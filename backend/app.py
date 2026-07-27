from fastapi import FastAPI
from backend.agent.agent import ask_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic AI is running"}

@app.get("/chat")
def chat(question: str):
    answer = ask_agent(question)
    return {"answer": answer}