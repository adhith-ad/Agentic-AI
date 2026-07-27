import sqlite3

conn = sqlite3.connect("database/company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

employees = [
    ("John", "IT", 70000, 6),
    ("Alice", "HR", 55000, 4),
    ("Bob", "Finance", 80000, 8),
    ("David", "IT", 65000, 5),
    ("Emma", "Sales", 60000, 3)
]

cursor.executemany(
    "INSERT INTO employees(name, department, salary, experience) VALUES (?, ?, ?, ?)",
    employees
)

conn.commit()
conn.close()

print("Database created successfully!")