from backend.agent.router import decide_tool

print(decide_tool("Show all employees - test_router.py:3"))
print(decide_tool("Explain AI - test_router.py:4"))