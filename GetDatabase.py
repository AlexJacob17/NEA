import sqlite3
from CreateDatabase import load_database

class GetDatabase:
    """
Each method takes two values, index and value.
Value is the value that is being matched to an attribute in the table and index is the name of that attribute.
    """
    def __init__(self):
        load_database()

    def getUsers(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("Select * From Users Where %s = '%s';" % (index, value))
            result = cursor.fetchall()
            results = []
            for each in result:
                results += [each]
            return results

    def getAdvertisements(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("Select * From Advertisements Where %s = '%s';" % (index, value))
            result = cursor.fetchall()
            results = []
            for each in result:
                results += [each]
            return results

    def getLocation(self, index, value):
        with sqlite3.connect("NEA.db") as db:
            cursor = db.cursor()
            cursor.execute("Select * From Location Where %s = '%s';" % (index, value))
            result = cursor.fetchall()
            results = []
            for each in result:
                results += [each]
            return results


