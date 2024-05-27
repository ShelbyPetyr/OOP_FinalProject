import sqlite3

def create_connection():
    connection = sqlite3.connect("movies.db")
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        director TEXT NOT NULL,
        year INTEGER,
        genre TEXT
    )
    ''')
    connection.commit()
    connection.close()

create_table()

def add_movie(title, director, year, genre):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO movies (title, director, year, genre)
    VALUES (?, ?, ?, ?)
    ''', (title, director, year, genre))
    connection.commit()
    connection.close()

def get_all_movies():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    connection.close()
    return movies

def update_movie(movie_id, title, director, year, genre):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE movies
    SET title = ?, director = ?, year = ?, genre = ?
    WHERE id = ?
    ''', (title, director, year, genre, movie_id))
    connection.commit()
    connection.close()

def delete_movie(movie_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
    connection.commit()
    connection.close()

def main():
    while True:
        print("1. Add movie")
        print("2. View all movies")
        print("3. Update movie")
        print("4. Delete movie")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            director = input("Enter director: ")
            year = int(input("Enter year: "))
            genre = input("Enter genre: ")
            add_movie(title, director, year, genre)
        elif choice == "2":
            movies = get_all_movies()
            for movie in movies:
                print(f"ID: {movie[0]}, Title: {movie[1]}, Director: {movie[2]}, Year: {movie[3]}, Genre: {movie[4]}")
        elif choice == "3":
            movie_id = int(input("Enter movie ID to update: "))
            title = input("Enter new title: ")
            director = input("Enter new director: ")
            year = int(input("Enter new year: "))
            genre = input("Enter new genre: ")
            update_movie(movie_id, title, director, year, genre)
        elif choice == "4":
            movie_id = int(input("Enter movie ID to delete: "))
            delete_movie(movie_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    create_table()
    main()