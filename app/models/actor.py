#09163033
#陳明龍

from datetime import date

class Actor:
    def __init__(self, name:str, birthday:date, nationality:str) -> None:
        self.name = name
        self.birthday = birthday
        self.nationality = nationality

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS actors (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        birthday DATE,
                        nationality TEXT
        )
        """
        db.execute(query)