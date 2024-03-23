import sqlite3
import json
import cgi

params = cgi.FieldStorage()

x = str(params.getfirst('name',0))
y = float(params.getfirst('price',0))

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('insert into goods(name,price) values("{}","{}")'.format(x,y))



connection.commit()
connection.close()