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
 
    
    conn.execute("""CREATE TABLE client_document_types(
        document_type_id INTEGER PRIMARY KEY,
        type_name TEXT
    )""")
    conn.commit()  
    
    conn.execute("""CREATE TABLE geo_entities(
        geo_entity_id INTEGER PRIMARY KEY,
        geo_entity_name TEXT
    )""")
    conn.commit()
    
    conn.execute("""CREATE TABLE geo_hierarchy(
        geo_hierarchy_entry INTEGER PRIMARY KEY,
        parent INTEGER NOT NULL,
        child INTEGER NOT NULL
    )""")
    conn.commit()
    
    conn.execute("""CREATE TABLE document_issue_places (
        document_issue_place_id INTEGER PRIMARY KEY,
        organization TEXT,
        org_code TEXT,
        geo_entity_id TEXT
    )""")
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
    

def fill_client_document_types():
    conn = sqlite3.connect('railways.db')
    conn.execute("""INSERT INTO client_document_types (type_name) VALUES
    ('Паспорт'),
    ('Загранпаспорт')""")

    conn.commit()
    conn.close()
    
    
def fill_geo_entities():
    conn = sqlite3.connect('railways.db')
    conn.execute("""INSERT INTO geo_entities (geo_entity_name) VALUES
    ('Земля'),
    ('Европа'),
    ('Россия'),
    ('Краснодарский край'),
    ('Анапа'),
    ('Кореновск'),
    ('Белореченск'),
    ('Белоруссия'),
    ('Брестская область'),
    ('Брест'),
    ('Пинск'),
    ('Барановичи'),
    ('Москва'),
    ('Самара'),
    ('Рязань'),
    ('Рузаевка'),
    ('Сызрань')""")
    conn.commit()
    conn.close()
    
def fill_geo_hierarchy():
    conn = sqlite3.connect('railways.db')
    conn.execute("""INSERT INTO geo_hierarchy(parent, child) VALUES
    ('Земля', 'Европа'),
    ('Европа', 'Россия'),
    ('Россия', 'Краснодарский'),
    ('Краснодарский край', 'Анапа'),
    ('Краснодарский край', 'Белореченск'),
    ('Краснодарский край', 'Кореновск'),
    ('Белоруссия', 'тская область'),
    ('Брестская область', 'Брест'),
    ('Брестская область', 'Пинск')
    """)
    conn.commit()
    conn.close()
    
def fill_document_issue_places():
    conn = sqlite3.connect('railways.db')
    conn.execute("""INSERT INTO document_issue_places (organization, org_code, geo_entity_id) VALUES
    ("ОВД Фили Давыдково", "770038", 'Белореченск'),
    ("МВД Белоруссии", "54544", 'Пинск'),
    ("УВД Краснодара", "4235", 'Кореновск')""")
    
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
    fill_client_document_types()
    fill_geo_entities()
    fill_geo_hierarchy()
    fill_document_issue_places()
    check_tables()
    
    #TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"
remove('railways.db')#TODO5: uncomment

from os.path import exists
if not exists('railways.db'):
    db_init()
#fill_locomotive_types()
conn = sqlite3.connect('railways.db')
cursor = conn.cursor()
cursor.execute('''SELECT * FROM document_issue_places;''')
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

