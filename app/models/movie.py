#09163033
#陳明龍

from app.database import create_connection
from typing import List, Tuple
from datetime import date

class Movie:
    def __init__(self, title:str, director:str, release:date, genre:str, rating:float)-> None:
        self.title = title
        self.director = director
        self.release = release
        self.genre = genre
        self.rating = rating

def save(self):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO movies (title, director, date, genre, rating)
        VALUES (?, ?, ?, ?)
        ''', (self.title, self.director, self.release, self.genre, self.rating))
        conn.commit()
        
@staticmethod
def get_all() -> List[Tuple[int, str, str, date, str, float]]:
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        return cursor.fetchall()
    
# class Movie:
#     def __init__(self, db, title, director_id, year, genre_id):
#         self.db = db
#         self.title = title
#         self.director_id = director_id
#         self.year = year
#         self.genre_id = genre_id

#     def save(self):
#         self.db.cur.execute('''
#             INSERT INTO movies (title, director_id, year, genre_id) VALUES (?, ?, ?, ?)
#         ''', (self.title, self.director_id, self.year, self.genre_id))
#         self.db.conn.commit()

#     def add_actor(self, actor_id):
#         self.db.cur.execute('''
#             INSERT INTO movie_actors (movie_id, actor_id) VALUES (?, ?)
#         ''', (self.db.cur.lastrowid, actor_id))
#         self.db.conn.commit()
