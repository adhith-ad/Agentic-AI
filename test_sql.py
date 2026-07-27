from tools.sql_tool import execute_query

result = execute_query(
    "SELECT * FROM employees WHERE experience > 5"
)

print(result)