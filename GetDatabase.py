import sqlite3
from CreateDatabase import load_database

class GetDatabase:
    """
Each method takes two values, primaryIndex and value.
Value is the value that is being matched to an attribute in the table which is d
    """
    def __init__(self):
        load_database()

    def getUsers(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("Select * From Users Where ? = ?;", (index, value))
            result = cursor.fetchall()
            for each in result:
                print(each)

p = GetDatabase()
p.getUsers("UserID", 1)


