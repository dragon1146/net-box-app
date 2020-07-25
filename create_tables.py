import sqlite3

connection = sqlite3.connect('toolbox.db')
cursor = connection.cursor()


# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS networking_toolbox (task text, command text)"
cursor.execute(create_table)

entry = ('glitch', 'cisco')
insert_query = "INSERT INTO networking_toolbox VALUES (?, ?)"
cursor.execute(insert_query, entry)

select_query = "SELECT * FROM networking_toolbox"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()






