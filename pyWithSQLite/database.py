import sqlite3

def setup():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS recipes(id INTEGER PRIMARY KEY,name TEXT,time INT)")
    conn.commit()
    return conn

def add_recipes(conn, name, time):
    c = conn.cursor()
    c.execute("INSERT INTO recipes (name,time) VALUES (?,?)",(name,time))
    conn.commit()
    return c.lastrowid

def get_recipes(conn):
    c = conn.cursor()
    c.execute('SELECT id, name,time from recipes')
    return c.fetchall()