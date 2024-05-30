
#app/database.py
import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
    
    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
    
    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()

#app/models/movie.py
class Movie:
    def __init__(self, id, title, director_id, genre_id, release_year):
        self.id = id
        self.title = title
        self.director_id = director_id
        self.genre_id = genre_id
        self.release_year = release_year

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            director_id INTEGER,
            genre_id INTEGER,
            release_year INTEGER,
            FOREIGN KEY (director_id) REFERENCES directors(id),
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
        """
        db.execute(query)

    def save(self, db):
        query = """
        INSERT INTO movies (title, director_id, genre_id, release_year)
        VALUES (?, ?, ?, ?)
        """
        db.execute(query, (self.title, self.director_id, self.genre_id, self.release_year))

#app/models/actor.py
class Actor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        db.execute(query)

    def save(self, db):
        query = """
        INSERT INTO actors (name)
        VALUES (?)
        """
        db.execute(query, (self.name,))

#app/models/genre.py
class Genre:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        db.class Movie:
#     def __init__(self, id=None, title=None, director_id=None, genre_id=None, release_year=None):
#         self.id = id
#         self.title = title
#         self.director_id = director_id
#         self.genre_id = genre_id
#         self.release_year = release_year

#     @staticmethod
#     def create_table(db):
#         query = """
#         CREATE TABLE IF NOT EXISTS movies (
#             id INTEGER PRIMARY KEY,
#             title TEXT NOT NULL,
#             director_id INTEGER,
#             genre_id INTEGER,
#             release_year INTEGER,
#             FOREIGN KEY (director_id) REFERENCES directors(id),
#             FOREIGN KEY (genre_id) REFERENCES genres(id)
#         )
#         """
#         db.execute(query)execute(query)

    def save(self, db):
        query = """
        INSERT INTO genres (name)
        VALUES (?)
        """
        db.execute(query, (self.name,))

#app/models/director.py
class Director:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS directors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        db.execute(query)

    def save(self, db):
        query = """
        INSERT INTO directors (name)
        VALUES (?)
        """
        db

#app/database.py
import sqlite3
from contextlib import closing

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def execute(self, query, params=()):
        with sqlite3.connect(self.db_path) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params)
                conn.commit()
    
    def fetchall(self, query, params=()):
        with sqlite3.connect(self.db_path) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
    
    def fetchone(self, query, params=()):
        with sqlite3.connect(self.db_path) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def close(self):
        pass  # Since we're using context managers, there's no need to manually close connections
    
    # CRUD operations for User
    def create_user(self, username, email):
        query = "INSERT INTO users (username, email) VALUES (?, ?)"
        self.execute(query, (username, email))

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE id = ?"
        return self.fetchone(query, (user_id,))

    def update_user(self, user_id, username, email):
        query = "UPDATE users SET username = ?, email = ? WHERE id = ?"
        self.execute(query, (username, email, user_id))

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = ?"
        self.execute(query, (user_id,))
    
    # CRUD operations for Movie
    def create_movie(self, title, director_id, genre_id, release_year):
        query = "INSERT INTO movies (title, director_id, genre_id, release_year) VALUES (?, ?, ?, ?)"
        self.execute(query, (title, director_id, genre_id, release_year))

    def get_movie(self, movie_id):
        query = "SELECT * FROM movies WHERE id = ?"
        return self.fetchone(query, (movie_id,))

    def update_movie(self, movie_id, title, director_id, genre_id, release_year):
        query = "UPDATE movies SET title = ?, director_id = ?, genre_id = ?, release_year = ? WHERE id = ?"
        self.execute(query, (title, director_id, genre_id, release_year, movie_id))

    def delete_movie(self, movie_id):
        query = "DELETE FROM movies WHERE id = ?"
        self.execute(query, (movie_id,))
    
    # CRUD operations for Genre
    def create_genre(self, name):
        query = "INSERT INTO genres (name) VALUES (?)"
        self.execute(query, (name,))

    def get_genre(self, genre_id):
        query = "SELECT * FROM genres WHERE id = ?"
        return self.fetchone(query, (genre_id,))

    def update_genre(self, genre_id, name):
        query = "UPDATE genres SET name = ? WHERE id = ?"
        self.execute(query, (name, genre_id))

    def delete_genre(self, genre_id):
        query = "DELETE FROM genres WHERE id = ?"
        self.execute(query, (genre_id,))
    
    # CRUD operations for Actor
    def create_actor(self, name):
        query = "INSERT INTO actors (name) VALUES (?)"
        self.execute(query, (name,))

    def get_actor(self, actor_id):
        query = "SELECT * FROM actors WHERE id = ?"
        return self.fetchone(query, (actor_id,))

    def update_actor(self, actor_id, name):
        query = "UPDATE actors SET name = ? WHERE id = ?"
        self.execute(query, (name, actor_id))

    def delete_actor(self, actor_id):
        query = "DELETE FROM actors WHERE id = ?"
        self.execute(query, (actor_id,))
    
    # CRUD operations for Director
    def create_director(self, name):
        query = "INSERT INTO directors (name) VALUES (?)"
        self.execute(query, (name,))

    def get_director(self, director_id):
        query = "SELECT * FROM directors WHERE id = ?"
        return self.fetchone(query, (director_id,))

    def update_director(self, director_id, name):
        query = "UPDATE directors SET name = ? WHERE id = ?"
        self.execute(query, (name, director_id))

    def delete_director(self, director_id):
        query = "DELETE FROM directors WHERE id = ?"
        self.execute(query, (director_id,))
