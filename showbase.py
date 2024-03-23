import json
import  sqlite3
#подключение к базе данных, если таковой нет автоматическое создание
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

sql = '''
create table if not exists goods (
id integer primary key autoincrement,
name txt,
price integer,
comment txt
)
'''
cursor.execute(sql)

cursor.execute('select * from goods')
text  = cursor.fetchall()


table_html = '<table border="1px" width="400px">'

for row in text:
    table_html+='<tr>'
    for col in row:
        table_html += '<td>' + str(col) + '</td>'
    table_html +='<td> <input type="checkbox" id="{}" onchange="checkbox_click(this)"> <td>'.format(row[0])
    table_html+='</tr>'    
    
    
    
    
    

table_html+='</table>'

table_html = json.dumps(table_html)

print('Content-type: text/html\n')

print(table_html)




connection.commit()
connection.close()
