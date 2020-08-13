import sqlite3

connection = sqlite3.connect('/home/glitch/Documents/pythonRelated/simple-SQLAlchemy-database-interface/database/database.db')
cursor = connection.cursor()


# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)

create_table = "CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, contact INTEGER)"
cursor.execute(create_table)

tool = (1, 'cisco', '123456')
insert_query = "INSERT INTO test_table VALUES (?, ?, ?)"
cursor.execute(insert_query, tool)

select_query = "SELECT * FROM test_table"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()






