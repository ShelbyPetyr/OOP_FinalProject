#09163033
#陳明龍

class User:
    def __init__(self, username:str, email:str, subscription:str) -> None:
        self.username = username
        self.email = email
        self.subscription = subscription

    @staticmethod
    def create_table(db):
        query = """
        CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        subscription TEXT
        )
        """
        db.execute(query)

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
