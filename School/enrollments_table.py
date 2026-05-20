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


def enroll_student(conn,student_id,course_id):
    try:
       c = conn.cursor()
       c.execute('SELECT id FROM students WHERE id = ?',(student_id,))
       if not c.fetchone():
          print('Student does not exists')
          return False
       c.execute('SELECT id FROM courses WHERE id = ? ',(course_id,))
       if not c.fetchone():
          print('Course does not exists')
          return False
       c.execute('SELECT id FROM enrollments WHERE student_id = ? AND course_id = ?',(student_id,course_id))
       if c.fetchone():
          print('Already enrolled')
          return False
       c.execute('INSERT INTO enrollments (student_id,course_id) VALUES (?,?)',(student_id,course_id))
       conn.commit()
       print('Enrolled')
       return True,c.lastrowid

    except sqlite3.Error:
        print("Error enrollment table")
        return False
    except Exception:
        print("Error Unexpected")
        return False

def get_enrollments(conn):
    try:
        c = conn.cursor()
        c.execute("""
        SELECT e.id , s.name, c.title 
        FROM enrollments as e
        JOIN students as s ON e.student_id = s.id
        JOIN course as c ON e.course_id = c.id
        """)
        return c.fetchall()

    except sqlite3.Error:
        print('Error viewing')
        return []
    except Exception:
        print('Unexpected Error')
        return []

def delete_enrollments(conn,enrollment_id):
    try:
        c = conn.cursor()
        c.execute("SELECT id FROM enrollments WHERE id = ?",(enrollment_id,))
        if not c.fetchone():
            print('Student is not enrolled')
            return 0

        c.execute('DELETE FROM enrollments WHERE id = ? ',(enrollment_id))
        conn.commit()
        print('Deleted successfully')
        return c.rowcount
    except sqlite3.Error:
        print('Delete query error')
        return 0
    except Exception:
        print('Unexpected error')
        return 0

def get_student_courses(conn,student_id):
    try:
        c = conn.cursor()
        c.execute("""
        SELECT  s.name, c.title
        FROM enrollments 
        JOIN courses as c ON enrollments.course_id = c.id
        JOIN students as s ON enrollments.student_id = s.id
        WHERE enrollments.student_id = ?
        """,(student_id,))
        return c.fetchall()
    except sqlite3.Error:
        print('Error on get student course')
        return []
    except Exception:
        print('Unexpected Error')
        return []