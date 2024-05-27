#09163033
#陳明龍

from app.database import create_connection
from typing import List, Tuple

class Genre:
    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description

def save(self):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO genres (name, description)
        VALUES (?, ?)
        ''', (self.name, self.description))
        conn.commit()

@staticmethod
def get_all() -> List[Tuple[int,str,str]]:
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM genres')
        return cursor.fetchall()
    
# class Genre:
#     def __init__(self, db, name):
#         self.db = db
#         self.name = name

#     def save(self):
#         self.db.cur.execute('''
#             INSERT INTO genres (name) VALUES (?)
#         ''', (self.name,))
#         self.db.conn.commit()