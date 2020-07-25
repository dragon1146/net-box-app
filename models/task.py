import sqlite3



class TaskModel:
    def __init__(self, task, command):
      self.task = task
      self.command = command
     
 
    def json(self):
      return {'task':self.task, 'command':self.command}    
      

    def insert(self):
        connection = sqlite3.connect('toolbox.db')
        cursor = connection.cursor()

        query = "INSERT INTO networking_toolbox VALUES (?,?)"
        cursor.execute(query, (self.task, self.command))

        connection.commit()
        connection.close()
    
    @classmethod
    def find_by_name(cls, task):
        connection = sqlite3.connect('toolbox.db')
        cursor = connection.cursor()

        query = "SELECT * FROM networking_toolbox WHERE task=?"
        result = cursor.execute(query, (task,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
    
    
    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     """
    #     - this SQL command will update the items table and set the
    #         price column value to the updated price where the name of
    #         the item in the row is equal to the variable 'name'
    #     """
        
        
    #     cursor.execute(query, (self.price, self.name))
    #     """
    #     - the order in which we sent the values for the name and price
    #     of the item is defferent from anywhere else in the code

    #     - this is because in the variable 'query' the value of price
    #         comes before the value of the name of the item

    #     - so we must follow the order in which SQL command will be executed
    #     """

    #     connection.commit()
    #     connection.close()
