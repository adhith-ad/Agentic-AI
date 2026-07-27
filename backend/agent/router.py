def decide_tool(question):

    question = question.lower()

    if "employee" in question:
        return "database"

    return "llm"