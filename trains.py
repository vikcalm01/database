import sqlite3
from os import remove

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


def fill_clients():
    conn = sqlite3.connect('railways.db')
    conn.execute('''insert into clients(client_id, username, password, email) 
    values("1", "visuly", "route12", "visuly@gmail.com"), 
    ("2", "dotatk", "rdnh1234", "dotatk@mail.ru"),
    ("3", "opa", "yev45", "opa@yandex.ru");''')

    conn.commit()
    conn.close()
    
def fill_genders():
    conn = sqlite3.connect('railways.db')
    conn.execute('''insert into genders(gender_name) 
    values("мужчина"), 
    ("женщина"),
    ("интерсекс");''')

    conn.commit()
    conn.close()
    
    
def fill_locomotive_types():
    conn = sqlite3.connect('railways.db')
    conn.execute('''insert into locomotive_types(type_name) values('�������');''')
    conn.execute('''insert into locomotive_types(type_name) values('����������');''')
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
    fill_locomotive_types()
    fill_clients()
    fill_genders()
    check_tables()
    
    #TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"
remove('railways.db')#TODO5: uncomment

from os.path import exists
if not exists('railways.db'):
    db_init()
#fill_locomotive_types()
conn = sqlite3.connect('railways.db')
cursor = conn.cursor()
cursor.execute('''SELECT * FROM genders;''')
res = cursor.fetchall()
for r in res:
    print(r)

'''TODO3: make a select query that shows run timetables like in http://izformatika.ru/mod/assign/view.php?id=2564

run_timetable_entry run_id rpt_entry arrival
("5", "������-��� ����", "�� ������ - �����-���������: ��������� ������ (������) (������-��� ����) (10:00:00)", "01.01.2022 10:00:00"), 
("6", "������-��� ����", "�� ������ - �����-���������: ���������� (������) (������-��� ����) (11:00:00)", "01.01.2022 11:00:00"), 
("7", "������-��� ����", "�� ������ - �����-���������: ����������� (�����������) (������-��� ����) (12:00:00)", "01.01.2022 12:00:00"), 
("8", "������-��� ����", "�� ������ - �����-���������: �����-����� (�����) (������-��� ����) (13:00:00)", "01.01.2022 13:00:00"), 
("9", "������-��� ����", "�� ������ - �����-���������: ���������� ������ (�����-���������) (������-��� ����) (14:00:00)", "01.01.2022 14:00:00")
'''

'''TODO3: make a select query that shows tickets like in http://izformatika.ru/mod/assign/view.php?id=2564
ticket_id client_document_id rpt_from rpt_to carriage_type_id carriage_no place_no run_id
("1", "ioann (������� ���� ����������, ������� #123)", "���������� (������) �� �������� ���������� - �����������, �������� � 10:00:00 � ������������ � ������-����������� ����", "����������� (�����������) �� �������� ���������� - �����������, �������� � 11:00:00 � ������������ � ������-����������� ����", "������������", "1", "10", "����� 1 �� ������-����������� ����"), 
("2", "ioann (������� ���� ����������, ������� #123)", "���������� (������) �� �������� ������ - �����-���������, �������� � 11:00:00 � ������������ � ������-��� ����", "�����-����� (�����) �� �������� ������ - �����-���������, �������� � 13:00:00 � ������������ � ������-��� ����", "�����-��������", "2", "33", "����� 1 �� ������-����������� ����")
'''

