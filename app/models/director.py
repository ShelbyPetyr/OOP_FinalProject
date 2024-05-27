#09163033
#陳明龍

from app.database import create_connection
from typing import List, Tuple
from datetime import date

class Director:
    def __init__(self, name:str, birthday:date, nationality:str):
        self.name = name
        self.birthday = birthday
        self.nationality = nationality

def save(self):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO directors (name, birthday, nationality)
        VALUES (?, ?, ?)
        ''', (self.name, self.birthday, self.nationality))
        conn.commit()


# class Director:
#     def __init__(self, db, name):
#         self.db = db
#         self.name = name

#     def save(self):
#         self.db.cur.execute('''
#             INSERT INTO directors (name) VALUES (?)
#         ''', (self.name,))
#         self.db.conn.commit()
