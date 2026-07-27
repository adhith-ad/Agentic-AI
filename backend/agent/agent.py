import ollama

def ask_agent(question):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]