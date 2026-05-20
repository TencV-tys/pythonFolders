import database as db

class School:
    def __init__(self,conn):
        self.conn = conn

try:
    conn = db.setup()
    school = School(conn)

except ValueError:
    print("choices must be integer")
except Exception:
    print('Unexpected error in the main file')
finally:
    try:
     if conn:
        conn.close()
        print("Database connection closed")
    except:
        pass