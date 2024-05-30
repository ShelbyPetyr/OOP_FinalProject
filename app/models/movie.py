#09163033
#陳明龍

from datetime import date

class Movie:
    def __init__(self, title:str, director:str, release:date, genre:str, rating:float)-> None:
        self.title = title
        self.director = director
        self.release = release
        self.genre = genre
        self.rating = rating
        
    @staticmethod
    def create_table(db):
            query=""" 
            CREATE TABLE IF NOT EXISTS movies (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        director TEXT,
                        release TEXT,
                        genre TEXT,
                        rating REAL,
                        FOREIGN KEY (genre) REFERENCES genres(name),
                        FOREIGN KEY (director) REFERENCES deirectors(name)
            )
            """
            db.execute(query)

