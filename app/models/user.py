#09163033
#陳明龍

from app.database import create_connection
from typing import List, Tuple

class User:
    def __init__(self, username:str, email:str, subscription:str):
        self.username = username
        self.email = email
        self.subscription = subscription

def save(self):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO movies (name, email, subscription)
        VALUES (?, ?, ?)
        ''', (self.username, self.email, self.subscription))
        conn.commit()

@staticmethod
def get_all() -> List[Tuple[int,str,str,str]]:
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

# class User:
#     def __init__(self, db, name, email):
#         self.db = db
#         self.name = name
#         self.email = email

#     def save(self):
#         self.db.cur.execute('''
#             INSERT INTO users (name, email) VALUES (?, ?)
#         ''', (self.name, self.email))
#         self.db.conn.commit()
