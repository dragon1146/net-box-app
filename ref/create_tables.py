import sqlite3

connection = sqlite3.connect('net_box.db')
cursor = connection.cursor()


# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)

create_table = "CREATE TABLE net_box (id INTERGER PRIMARY KEY, manufacture string, device string, task text, command text, notes text)"
cursor.execute(create_table)

tool = (1, 'cisco', 'router', 'interfaces', 'show ip int br', 'show ip int br')
insert_query = "INSERT INTO net_box VALUES (?, ?, ?, ?, ?, ?)"
cursor.execute(insert_query, tool)
connection.commit()
# 


select_query = "SELECT * FROM net_box"
for row in cursor.execute(select_query):
    print(row)

connection.close()






