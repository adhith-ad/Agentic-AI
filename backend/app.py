from fastapi import FastAPI
from ollama import chat

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic AI is running"}

@app.get("/chat")
def chatbot(question: str):
    response = chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return {
        "answer": response["message"]["content"]
    }