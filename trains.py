import sqlite3

def create_tables():
    conn = sqlite3.connect('railways.db')
    conn.execute('''CREATE TABLE locomotive_types
            (
            locomotive_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );''')
    #TODO1: add all tables, one commit per adding one table
    #TODO4: (optional for this task) add foreign keys
    conn.commit()
    
    conn.execute('''CREATE TABLE clients
            (
            client_id INTEGER PRIMARY KEY NOT NULL,
            username TEXT NOT NULL,
            password INTEGER NOT NULL,
            email INTEGER NOT NULL
            );''')
    #TODO1: add all tables, one commit per adding one table
    #TODO4: (optional for this task) add foreign keys
    conn.commit() 
    
    conn.execute('''CREATE TABLE genders
            (
            gender_id INTEGER PRIMARY KEY NOT NULL,
            gender_name TEXT NOT NULL
            );''')
    #TODO1: add all tables, one commit per adding one table
    #TODO4: (optional for this task) add foreign keys
    conn.commit()    
    conn.close() 
    
    

def fill_client():
    conn = sqlite3.connect('railways.db')
    conn.execute('''insert into client(username) values('visuly');''')
    conn.execute('''insert into client(username) values('dotatk');''')
    conn.execute('''insert into client(username) values('opa');''')
    
    conn.execute('''insert into client(password) values('route12');''')
    conn.execute('''insert into client(password) values('rdnh1234');''')
    conn.execute('''insert into client(password) values('yev45');''')
    
    conn.execute('''insert into client(email) values('visuly@gmail.com');''')
    conn.execute('''insert into client(email) values('dotatk@mail.ru');''')
    conn.execute('''insert into client(email) values('opa@yandex.ru');''')
    
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
    #TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"

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

'''TODO3: make a select query that shows run timetables like in http://izformatika.ru/mod/assign/view.php?id=2564

run_timetable_entry run_id rpt_entry arrival
("5", "Москва-Спб утро", "На Москва - Санкт-Петербург: Казанский вокзал (Москва) (Москва-Спб утро) (10:00:00)", "01.01.2022 10:00:00"), 
("6", "Москва-Спб утро", "На Москва - Санкт-Петербург: Павелецкая (Москва) (Москва-Спб утро) (11:00:00)", "01.01.2022 11:00:00"), 
("7", "Москва-Спб утро", "На Москва - Санкт-Петербург: Владивосток (Владивосток) (Москва-Спб утро) (12:00:00)", "01.01.2022 12:00:00"), 
("8", "Москва-Спб утро", "На Москва - Санкт-Петербург: Минск-Южный (Минск) (Москва-Спб утро) (13:00:00)", "01.01.2022 13:00:00"), 
("9", "Москва-Спб утро", "На Москва - Санкт-Петербург: Балтийский вокзал (Санкт-Петербург) (Москва-Спб утро) (14:00:00)", "01.01.2022 14:00:00")
'''

'''TODO3: make a select query that shows tickets like in http://izformatika.ru/mod/assign/view.php?id=2564
ticket_id client_document_id rpt_from rpt_to carriage_type_id carriage_no place_no run_id
("1", "ioann (Никулин Иван Васильевич, паспорт #123)", "Павелецкая (Москва) на маршруте Павелецкая - Владивосток, прибытие в 10:00:00 в соответствии с Москва-Владивосток утро", "Владивосток (Владивосток) на маршруте Павелецкая - Владивосток, прибытие в 11:00:00 в соответствии с Москва-Владивосток утро", "пассажирский", "1", "10", "Поезд 1 на Москва-Владивосток утро"), 
("2", "ioann (Никулин Иван Васильевич, паспорт #123)", "Павелецкая (Москва) на маршруте Москва - Санкт-Петербург, прибытие в 11:00:00 в соответствии с Москва-Спб утро", "Минск-Южный (Минск) на маршруте Москва - Санкт-Петербург, прибытие в 13:00:00 в соответствии с Москва-Спб утро", "вагон-ресторан", "2", "33", "Поезд 1 на Москва-Владивосток утро")
'''

