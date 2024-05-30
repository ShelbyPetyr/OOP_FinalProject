#09163033
#陳明龍

import sqlite3
import os
from contextlib import closing
from typing import List, Tuple, Any

class MovieDatabase:
    def __init__(self, db_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(script_dir,db_path)
    
    def execute(self, query, params=()):
        with sqlite3.connect(self.db_path) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params)
                conn.commit()
    
    def fetchall(self, table_name:str) -> List[Tuple[Any,...]]:
        query = f"SELECT * FROM {table_name}"
        with sqlite3.connect(self.db_path) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    
    def fetchone(self, query, params=()):
        with sqlite3.connect(self.db_path) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def close(self):
        pass 
    
    # CRUD operations for User
    def create_user(self, username, email, subscription):
        query = "INSERT INTO users (username, email, subscription) VALUES (?, ?, ?)"
        self.execute(query, (username, email, subscription))

    def update_user(self, user_id, username, email,subscription):
        query = "UPDATE users SET username = ?, email = ?, subscription = ? WHERE id = ?"
        self.execute(query, (username, email, user_id, subscription))

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = ?"
        self.execute(query, (user_id,))
    
    # CRUD operations for Movie
    def create_movie(self, title, director, release, genre, rating):
        query = "INSERT INTO movies (title, director, release, genre, rating) VALUES (?, ?, ?, ?, ?)"
        self.execute(query, (title, director, release, genre, rating))

    def update_movie(self, id=None, title=None, director=None, release=None, genre=None, rating=None):
        query = "UPDATE movies SET "
        params = []
        # Add fields to update if they are provided
        if title is not None:
            query += "title = ?, "
            params.append(title)
        if director is not None:
            query += "director = ?, "
            params.append(director)
        if release is not None:
            query += "release = ?, "
            params.append(release)
        if genre is not None:
            query += "genre = ?, "
            params.append(genre)
        if rating is not None:
            query += "rating = ?, "
            params.append(rating)
        # Remove the trailing comma and space
        query = query.rstrip(', ')

        # Add the WHERE clause
        query += " WHERE id = ?"
        params.append(id)

        # Execute the query with the parameters
        self.execute(query, params)
        #self.execute(query, (id,title, director, release, genre, rating))

    def delete_movie(self, movie_id):
        query = "DELETE FROM movies WHERE id = ?"
        self.execute(query, (movie_id,))
    
    # CRUD operations for Genre
    def create_genre(self, name, description):
        query = "INSERT INTO genres (name, description) VALUES (?, ?)"
        self.execute(query, (name, description))

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
    def create_actor(self, name, birthday, nationality):
        query = "INSERT INTO actors (name, birthday, nationality) VALUES (?,?,?)"
        self.execute(query, (name,birthday, nationality))

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
    def create_director(self, name, birthday, nationality):
        query = "INSERT INTO directors (name,birthday,nationality) VALUES (?,?,?)"
        self.execute(query, (name,birthday,nationality))

    def get_director(self, director_id):
        query = "SELECT * FROM directors WHERE id = ?"
        return self.fetchone(query, (director_id,))

    def update_director(self, director_id, name):
        query = "UPDATE directors SET name = ? WHERE id = ?"
        self.execute(query, (name, director_id))

    def delete_director(self, director_id):
        query = "DELETE FROM directors WHERE id = ?"
        self.execute(query, (director_id,))
