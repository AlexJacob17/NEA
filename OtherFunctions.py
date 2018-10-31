import hashlib
import binascii
from GetDatabase import GetDatabase
from EditDatabase import EditDatabase

# This procedure gets the current value of Account funds using the database function GetDatabase
# The amount to be added is added on to the retrieved value and replaced in the database using the Edit function

def addAccountFunds(userID, addValue):
    g = GetDatabase()
    currentValue = g.getUsers("UserID", userID)[0][3]
    newValue = round(currentValue + addValue, 2)
    e = EditDatabase()
    e.editUsers("userID", userID, "AccountFunds", newValue)

# This function will compare the hash value in the database to the value that was entered by the user
# If these values match, True will be returned and the user will be let into their account

def matchHashValue(userID, enteredPassword):
    g = GetDatabase()
    currentValue = g.getUsers("UserID", userID)[0][2]
    enteredHashValue = hashlib.sha256()
    enteredHashValue.update(enteredPassword.encode('utf-8'))
    enteredValue = enteredHashValue.hexdigest()
    if enteredValue == currentValue:
        return True
    return False


