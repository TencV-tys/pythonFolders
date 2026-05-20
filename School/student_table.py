import sqlite3

def student_table(conn):
    try:
       c = conn.cursor()
       c.execute("""
       CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL
       )
       """)
       conn.commit()
       return conn
    except sqlite3.Error as e:
        print(f"Database error on student table: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error on student table: {e}")
        raise

