import sqlite3
import json

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


cursor.execute('select min(price) from goods')
x = cursor.fetchall()
x = json.dumps(x[0][0])


print('Content-type: text/html\n')

print(x)

