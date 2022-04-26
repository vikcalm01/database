import sqlite3

def create_tables():
    conn = sqlite3.connect('railways.db')
    conn.execute('''CREATE TABLE locomotive_types
            (
            locomotive_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );''')
    #TODO1: add all tables
    conn.commit()
    conn.close()  
    
def check_tables():
    conn = sqlite3.connect('railways.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table';''')
    res = cursor.fetchall()
    for r in res:
        print(r)
    
def db_init():    
    create_tables()
    check_tables()

from os.path import exists
if not exists('railways.db'):
    db_init()
