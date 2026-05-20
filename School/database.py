import sqlite3
import student_table as stu
import course_table as course
import enrollments_table as enrollment
def setup():
    conn = connection()
    stu.student_table(conn)
    course.course_table(conn)
    enrollment.enrollments_table(conn)
    print("Tables created successfully")
    return conn

def connection():
    try:
       conn = sqlite3.connect('school.db')
       return conn
    except sqlite3.Error:
        print('Database error')
        raise
    except Exception:
        print('Main connection error unexpected')
        raise
