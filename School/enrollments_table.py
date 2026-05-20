import sqlite3

def enrollments_table(conn):
    try:
       c = conn.cursor()
       c.execute("""
       CREATE TABLE IF NOT EXISTS enrollments (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       student_id INTEGER,
       course_id INTEGER,
       FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
       FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
       )
       """)
       conn.commit()
       return conn
    except sqlite3.Error:
        print("Enrollment table error")
        raise
    except Exception:
        print("Unexpected error in enrollment table")
        raise