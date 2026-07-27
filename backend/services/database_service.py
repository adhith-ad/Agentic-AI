import sqlite3

DB_PATH = "database/company.db"

def get_employees_by_experience(min_exp):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, department, salary, experience
        FROM employees
        WHERE experience > ?
    """, (min_exp,))

    rows = cursor.fetchall()
    conn.close()

    return rows
