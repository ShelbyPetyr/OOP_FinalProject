#09163033
#陳明龍

class Genre:
    def __init__(self,db, name:str, description:str) -> None:
        self.db = db
        self.name = name
        self.description = description

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS genres (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            description TEXT
        )
        """
        db.execute(query)