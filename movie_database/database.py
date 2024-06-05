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

    def update_user(self,id=None, username=None,email=None, subscription=None):
        query = "UPDATE users SET "
        params = []
        if username is not None:
            query += "username = ?, "
            params.append(username)
        if email is not None:
            query += "email = ?, "
            params.append(email)
        if subscription is not None:
            query += "subscription = ?, "
            params.append(subscription)
        query = query.rstrip(', ')
         # Add the WHERE clause
        query += " WHERE id = ?"
        params.append(id)

        # Execute the query with the parameters
        self.execute(query, params)

    def delete_user(self, id):
        query = "DELETE FROM users WHERE id = ?"
        self.execute(query, (id,))
    
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

    def delete_movie(self, id):
        query = "DELETE FROM movies WHERE id = ?"
        self.execute(query, (id,))
    
    # CRUD operations for Genre
    def create_genre(self, name, description):
        query = "INSERT INTO genres (name, description) VALUES (?, ?)"
        self.execute(query, (name, description))

    def get_genre(self, genre_id):
        query = "SELECT * FROM genres WHERE id = ?"
        return self.fetchone(query, (genre_id,))

    def update_genre(self,id=None, name=None, description=None):
        query = "UPDATE genres SET "
        params = []
        if name is not None:
            query += "name = ?, "
            params.append(name)
        if description is not None:
            query += "description = ?, "
            params.append(description)
        query = query.rstrip(', ')
         # Add the WHERE clause
        query += " WHERE id = ?"
        params.append(id)

        # Execute the query with the parameters
        self.execute(query, params)

    def delete_genre(self, id):
        query = "DELETE FROM genres WHERE id = ?"
        self.execute(query, (id,))
    
    # CRUD operations for Actor
    def create_actor(self, name, birthday, nationality):
        query = "INSERT INTO actors (name, birthday, nationality) VALUES (?,?,?)"
        self.execute(query, (name,birthday, nationality))

    def get_actor(self, actor_id):
        query = "SELECT * FROM actors WHERE id = ?"
        return self.fetchone(query, (actor_id,))

    def update_actor(self, id=None, name=None, birthday=None, nationality=None):
        query = "UPDATE actors SET "
        params = []
        # Add fields to update if they are provided
        if name is not None:
            query += "name = ?, "
            params.append(name)
        if birthday is not None:
            query += "birthday = ?, "
            params.append(birthday)
        if nationality is not None:
            query += "nationality = ?, "
            params.append(nationality)
        # Remove the trailing comma and space
        query = query.rstrip(', ')

         # Add the WHERE clause
        query += " WHERE id = ?"
        params.append(id)

        # Execute the query with the parameters
        self.execute(query, params)

    def delete_actor(self, id):
        query = "DELETE FROM actors WHERE id = ?"
        self.execute(query, (id,))
    
    # CRUD operations for Director
    def create_director(self, name, birthday, nationality):
        query = "INSERT INTO directors (name,birthday,nationality) VALUES (?,?,?)"
        self.execute(query, (name,birthday,nationality))

    def get_director(self, director_id):
        query = "SELECT * FROM directors WHERE id = ?"
        return self.fetchone(query, (director_id,))

    def update_director(self, id=None, name=None, birthday=None, nationality=None):
        query = "UPDATE directors SET "
        params = []
        # Add fields to update if they are provided
        if name is not None:
            query += "name = ?, "
            params.append(name)
        if birthday is not None:
            query += "birthday = ?, "
            params.append(birthday)
        if nationality is not None:
            query += "nationality = ?, "
            params.append(nationality)
        # Remove the trailing comma and space
        query = query.rstrip(', ')

        # Add the WHERE clause
        query += " WHERE id = ?"
        params.append(id)

        # Execute the query with the parameters
        self.execute(query, params)

    def delete_director(self, id):
        query = "DELETE FROM directors WHERE id = ?"
        self.execute(query, (id,))
