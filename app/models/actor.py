#09163033
#陳明龍

from datetime import date

class Actor:
    def __init__(self,db, name:str, birthday:date, nationality:str):
        self.db = db
        self.name = name
        self.birthday = birthday
        self.nationality = nationality

def save(self):
    self.db.cur.execute('''
        INSERT INTO actors (name, birthday, nationality)
        VALUES (?, ?, ?)
        ''', (self.name, self.birthday, self.nationality))
    self.db.conn.commit()