import sqlite3

def execute_query(query):
    conn = sqlite3.connect("database/company.db")
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return result