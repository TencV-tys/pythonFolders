import sqlite3
from datetime import datetime

def setup():
    try:
       conn = sqlite3.connect('library.db')
       c = conn.cursor()
       c.execute("""
         CREATE TABLE IF NOT EXISTS books (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL,
         author TEXT NOT NULL
         )
       """)
       c.execute("""
        CREATE TABLE IF NOT EXISTS borrowed (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        books_id INTEGER,
        member_name TEXT NOT NULL,
        borrowed_date TEXT NOT NULL,
        FOREIGN KEY (books_id) REFERENCES books(id) ON DELETE CASCADE
         )
       """)

       conn.commit()
       return conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error in database file :{e}")
        raise
def add_book(conn, title, author):
    try:
        c = conn.cursor()
        c.execute('SELECT title FROM books WHERE title = ?',(title,))
        if c.fetchone():
            print('Book exists')
            return None
        c.execute('INSERT INTO books (title, author) VALUES(?,?)', (title,author))
        conn.commit()
        return c.lastrowid
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in database file: {e}")
        return None

def get_all_books(conn):
    try:
       c = conn.cursor()
       c.execute("SELECT id,title, author FROM books")
       return c.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f'Unexpected error: {e}')
        return []

def update_book(conn,id,title,author):
    try:
        c = conn.cursor()
        c.execute('SELECT id FROM books WHERE id = ?', (id,))
        if not c.fetchone():
            print(f'Book does not exists')
            return 0
        
        c.execute('UPDATE books SET title = ?,author = ? WHERE id = ? ',(title,author,id))
        conn.commit()
        return c.rowcount
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return 0
    except Exception as e:
        print(f'Unexpected error: {e}')
        return 0

def delete_book(conn,id):
    try:
        c = conn.cursor()
        c.execute('SELECT id FROM books WHERE id = ? ',(id,))
        if not c.fetchone():
            print(f"Book does not exists")
            return 0
        c.execute("DELETE FROM books WHERE id = ? ",(id,))
        conn.commit()
        return c.rowcount
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return 0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0

def  borrow_book(conn, book_id, member_name):
    try:
        c = conn.cursor()
        c.execute('SELECT id FROM books WHERE id = ?', (book_id,))
        if not c.fetchone():
            print(f'Book does not exists')
            return False
        
        c.execute('SELECT id FROM borrowed WHERE book_id = ?', (book_id,))
        if c.fetchone():
            print(f'Book is already borrowed')
            return False
        
        today = datetime.now().strftime('%Y-%m-%d')
        c.execute("""
        INSERT INTO borrowed (book_id,member_name, borrowed_date) VALUES(?,?,?)
        """,(book_id,member_name,today))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def return_book(conn,book_id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM borrowed WHERE book_id = ?",(book_id,))
        conn.commit()

        if c.rowcount > 0:
            print(f"✅ Book ID {book_id} returned")
            return True
        else:
            print(f"❌ Book ID {book_id} was not borrowed")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f'Unexpected error: {e}')
        return False

def get_borrowed_books(conn):
    try:
        c = conn.cursor()
        c.execute("""
        SELECT b.id, books.title, books.author, b.member_name, b.borrowed_date 
        FROM borrowed as b
        JOIN books ON b.book_id = books.id
        """)
        return c.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def is_book_available(conn,book_id):
    try:
        c = conn.cursor()
        c.execute("SELECT id FROM borrowed WHERE book_id = ?",(book_id,))
        return c.fetchone() is None
    except sqlite3.Error as  e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False