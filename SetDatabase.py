import sqlite3
from CreateDatabase import load_database, validate_values

class SetDatabase:
    """
Each method will be passed the list values which will contain all the values for that record of the database.
The index of the attributes are commented in each method.
The number of indexes will be 1 less than the number of attributs in the table as the primary key for every table
is incremented automatically.
I have opened and closed the database in every method because it means I do not need to close the database
externally meaning I am less likely to make an error that will corrupt the data.
It is import that the data type of values is tuple.
    """
    def __init__(self):
        load_database()
    
    def setUsers(self, values):
        # 0 = Email, 1 = HashedPassword, 2 = AccountFunds
        if validate_values(values, 3):
            with sqlite3.connect("NEA.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO Users (Email, HashedPassword, AccountFunds) VALUES (?, ?, ?);"""
                cursor.execute(sql, values)
                db.commit()

    def setLocation(self, values):
        # 0 = LongLatCoordinates, 1 = LocationDescription
        if validate_values(values, 2):
            with sqlite3.connect("NEA.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO Location (LongLatCoordinates, LocationDescription) VALUES (?, ?);"""
                cursor.execute(sql, values)
                db.commit()

    def setAdvertisements(self, values):
        # 0 = UserID, 1 = LocationID, 2 = ImageLink, 3 = ViewsRemaining, 4 = TotalViews, 5 = DayDisplayed
        # 6 = OverlayPosition, 7 = OverlayColour, 8 = OverlayContWalkinDist, 9 = OverlayContOpenTime
        if validate_values(values, 10):
            with sqlite3.connect("NEA.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO Advertisements
                    (UserID, LocationID, ImageLink, ViewsRemaining, TotalViews, DayDisplayed, OverlayPosition,
                    OverlayColour, OverlayContWalkingDist, OverlayContOpenTime)
                    VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                cursor.execute(sql, values)
                db.commit()


def test():
    setter = SetDatabase()
    setter.setAdvertisements((2, 3, "a", 54, 105, "b", "a,b", 255, 6, "a"))
    with sqlite3.connect("NEA.db")as db:
            cursor = db.cursor()
            sql = """Select * From Advertisements;"""
            cursor.execute(sql)
            result = cursor.fetchall()
            for each in result:
                print(each)

test()

                
