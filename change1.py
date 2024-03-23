import cgi
import sqlite3

params = cgi.FieldStorage()

id2 = params.getfirst('id2')

name2 = params.getfirst('name2')

price2 = params.getfirst('price2')


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('UPDATE goods SET name = "{}", price = "{}" WHERE id = "{}"'.format(name2,price2,id2))



connection.commit()
connection.close()
#UPDATE your_table
#SET your_column = REPLACE(your_column, 'find_this', 'replace_with_this')
#WHERE your_column LIKE '%find_this%';