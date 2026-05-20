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

def add_student(conn, name):
    try:
       c = conn.cursor()
       c.execute('INSERT INTO students (name) VALUES (?)',(name,))
       conn.commit()
       return c.lastrowid

    except sqlite3.Error:
        print("Adding student error")
        return None
    except Exception:
        print("Unexpected adding in student table")
        return None

def view_all_student(conn):
    try:
        c = conn.cursor()
        c.execute('SELECT id,name FROM students ')
        return c.fetchall()
    
    except sqlite3.Error:
        print("View method error ")
        return []
    except Exception:
        print("Unexpected error in view method in student table")
        return []

def update_student(conn,id,name):
    try:
        c = conn.cursor()
        c.execute('SELECT id,name FROM students WHERE id = ?',(id,))
        if not c.fetchone():
            print('Student does not exists')
            return 0

        c.execute('UPDATE students SET name = ? WHERE id = ?',(name,id))
        conn.commit()
        return c.rowcount

    except sqlite3.Error:
        print("Updating query error")
        return 0
    except Exception:
        print("Unexpected updating error")
        return 0

def delete_student(conn,id):
    try:
        c = conn.cursor()
        c.execute('SELECT id,name FROM students WHERE id = ? ',(id,))
        if not c.fetchone():
            print('Student does not exists')
            return 0
        c.execute('DELETE FROM students WHERE id = ?',(id,))
        conn.commit()
        return c.rowcount
    except sqlite3.Error:
        print('Delete query error')
        return 0
    except Exception:
        print('Unexpected error on delete table')
        return 0

def  view_student_by_id(conn,id):
    try:
        c = conn.cursor()
        c.execute('SELECT id,name FROM students WHERE id = ?', (id,))
        student = c.fetchone()
        if not student:
            print('Student does not exists')
            return None
        
        return student

    except sqlite3.Error:
        print("Error viewing id query")
        return None
    except Exception:
        print("Unexpecetd error in viewing by id")
        return None