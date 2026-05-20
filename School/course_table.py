import sqlite3

def course_table(conn):
    try:
      c = conn.cursor()
      c.execute("""
      CREATE TABLE IF NOT EXISTS courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL
      )
      """)
      conn.commit()
      return conn

    except sqlite3.Error:
        print(f'course table error')
        raise
    except Exception:
        print(f"Unexpected error on Course table")
        raise

