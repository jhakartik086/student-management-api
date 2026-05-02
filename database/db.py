import sqlite3
from config import DB_NAME

def get_conn():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def db_init():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            s_class TEXT
        )
    ''')

    conn.commit()
    conn.close()