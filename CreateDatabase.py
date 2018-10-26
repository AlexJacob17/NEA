import sqlite3

def load_database():
    with sqlite3.connect("NEA.db") as db:
        cursor = db.cursor()
        
        sql_users = """
    CREATE TABLE IF NOT EXISTS Users(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Email TEXT,
    HashedPassword TEXT,
    AccountFunds NUMERIC
    );
    """
        cursor.execute(sql_users)

        sql_location = """
    CREATE TABLE IF NOT EXISTS Location(
    LocationID INTEGER PRIMARY KEY AUTOINCREMENT,
    LongLatCoordinates TEXT,
    LocationDescription TEXT
    );
    """
        cursor.execute(sql_location)

        sql_advertisements = """
    CREATE TABLE IF NOT EXISTS Advertisements(
    AdvertID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    LocationID INTEGER,
    ImageLink TEXT,
    ViewsRemaining INTEGER,
    TotalViews INTEGER,
    DayDisplayed TEXT,
    OverlayPosition TEXT,
    OverlayColour INTEGER,
    OverlayContWalkingDist INTEGER,
    OverlayContOpenTime TEXT,
    FOREIGN KEY(UserID) REFERENCES Users(UserID),
    FOREIGN KEY(LocationID) REFERENCES Location(LocationID)
    );
    """
        cursor.execute(sql_advertisements)

def validate_values(atuple, length):
    if len(atuple) == length:
        return True
    return False
