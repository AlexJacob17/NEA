import sqlite3
from CreateDatabase import load_database

class EditDatabase:
    """
    The first two passed values are the name of the attribute that you want to change and the value you want to
    change it to.
    The last two attribute are to identify the record that these values belong to with the attribute name
    first and the value second.
    """
    def __init__(self):
        load_database()

    def editUsers(self, index, value, changeIndex, newValue):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("UPDATE Users SET %s = '%s' WHERE %s = '%s'" % (changeIndex, newValue, index, value))
            db.commit()

    def editAdvertisements(self, index, value, changeIndex, newValue):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("UPDATE Advertisements SET %s = '%s' WHERE %s = '%s'" % (changeIndex, newValue, index, value))
            db.commit()

    def editLocation(self, index, value, changeIndex, newValue):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("UPDATE Location SET %s = '%s' WHERE %s = '%s'" % (changeIndex, newValue, index, value))
            db.commit()

