import sqlite3

def db_init():
	db_create()
	add_locomotive_types()
	add_locomotives()
	#TODO: functions for filling all tables
	

from os.path import exists
if not exists('railways.db') #TODO: are all tables ok
	db_init()
	
conn = sqlite3.connect('railways.db')
cursor = conn.cursor()
cursor.execute(select * from locomotives;)
res = cursor.fetchall()
for r in res:
	print(r)
conn.close()