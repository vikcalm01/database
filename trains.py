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

def fill_locomotive_types():
    conn = sqlite3.connect('railways.db')
    conn.execute('''insert into locomotive_types(type_name) values('паровоз');''')
    conn.execute('''insert into locomotive_types(type_name) values('электровоз');''')
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
    fill_locomotive_types()

from os.path import exists
if not exists('railways.db'):
    db_init()
#fill_locomotive_types()
conn = sqlite3.connect('railways.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM locomotive_types;''')
res = cursor.fetchall()
for r in res:
    print(r)