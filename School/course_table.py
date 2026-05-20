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

def add_course(conn,title):
    try:
        c = conn.cursor()
        c.execute('SELECT title FROM courses WHERE title = ? ',(title,))
        if c.fetchone():
            print('Course exists')
            return None
        c.execute('INSERT INTO courses (title) VALUES (?)',(title,))
        conn.commit()
        print("New Course added")
        return c.lastrowid
        
    except sqlite3.Error:
        print('Course table add error')
        return None
    except Exception:
        print('Unexpected error in course table')
        return None

def update_course_title(conn,id,title):
    try:
        c = conn.cursor()
        c.execute('SELECT id FROM courses WHERE id = ?',(id,))
        if not c.fetchone():
            print('Course does not exists')
            return 0
        c.execute('UPDATE courses SET title = ? WHERE id = ?',(title,id))
        conn.commit()
        print("Updated sucessfully")
        return c.rowcount
    except sqlite3.Error:
        print('Update query error')
        return 0
    except Exception:
        print('Unexpected error on update query')
        return 0

def view_all_courses(conn):
    try:
        c = conn.cursor()
        c.execute('SELECT id,title FROM courses')
        return c.fetchall()
    except sqlite3.Error:
        print('View courses error')
        return []
    except Exception:
        print('Unexpected view courses error')
        return []

def view_course_by_id(conn,id):
    try:
        c = conn.cursor()
        c.execute('SELECT id FROM courses WHERE id = ?',(id,))
        course = c.fetchone()
        if not course:
            print('Course does not exists')
            return None
        
        return course
    except sqlite3.Error:
        print('Error on id')
        return None
    except Exception:
        print('Unexpected error on id by course')
        return None

def  delete_course(conn,id):
    try:
        c = conn.cursor()
        c.execute('SELECT id FROM courses WHERE id = ?',(id,))
        if not c.fetchone():
            print('Courses does not exists')
            return 0
        c.execute('DELETE FROM courses WHERE id = ? ',(id,))
        conn.commit()
        print('Course deleted successfully')
        return c.rowcount

    except sqlite3.Error:
        print('Error deleting')
        return 0
    except Exception:
        print("Unexpected error deleting")
        return 0

