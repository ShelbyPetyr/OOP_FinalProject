#09163033
#陳明龍

import sqlite3

class MovieDatabase:
    def __init__(self, db_name='data/movies.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute(''' 
        CREATE TABLE IF NOT EXISTS movies (
                       id INTEGER PRIMARY KEY,
                       title TEXT NOT NULL,
                       director TEXT,
                       director_id INTEGER,
                       date TEXT,
                       genre TEXT,
                       rating REAL,
                       FOREIGN KEY (director_id) REFERENCES directors(id),
                       FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS actors (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       birthday DATE,
                       nationality TEXT
        )
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS directors (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       birthday DATE,
                       nationality TEXT
        )
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY,
                       username TEXT NOT NULL,
                       email TEXT NOT NULL,
                       subscription TEXT
        )
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS genres (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT
        )
        ''')
        
        self.cur.exeute('''
        CREATE TABLE IF NOT EXISTS movie_actors (
                      movie_id INTEGER,
                      actor_id INTEGER,
                      FOREIGN KEY (movie_id) REFERENCES movies(id),
                      FOREIGN KEY (actor_id) REFERENCES actors(id),
                      PRIMARY KEYU (movie_id, actor_id)
        )
''')
        self.conn.commit()

    def close(self):
        self.conn.close()