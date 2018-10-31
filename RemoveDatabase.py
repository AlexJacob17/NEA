import sqlite3
from CreateDatabase import load_database

class RemoveDatabase:
    """
This will remove the entire record not just the attribute listed
The edit function can be used to change a single attribute
    """
    def __init__(self):
        load_database()

    def removeUsers(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM Users WHERE %s = '%s';" % (index, value))
            db.commit()

    def removeAdvertisements(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM Advertisements WHERE %s = '%s';" % (index, value))
            db.commit()

    def removeLocation(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM Location WHERE %s = '%s';" % (index, value))
            db.commit()


