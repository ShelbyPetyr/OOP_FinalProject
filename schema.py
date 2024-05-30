import sqlite3

conn = sqlite3.connect('/home/petyr/Github/OOP_FinalProject/data/movies.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(movies);")
#cursor.execute("ALTER TABLE movies ADD COLUMN release TEXT;")
columns = cursor.fetchall()

for column in columns:
    print(column)

conn.close()
