import sqlite3
import os

def connect(filename):
    create = not os.path.exists(filename)
    db = sqlite3.connect(filename)
    if create:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE KioskLog ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
            "Location TEXT NOT NULL, "
            "passwd TEXT NOT NULL, "
            "money INTEGER NOT NULL, "
            "PlayerID INTEGER  , "       
            "MobileID TEXT   "
            ")")
        db.commit()
    return db
    
connect('pdb')    