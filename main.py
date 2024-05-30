#Name       : 陳明龍   
#Student ID : 09163033

#Import necessary modules
from database import MovieDatabase
import os
from app.models.movie import Movie
from app.models.actor import Actor
from app.models.genre import Genre
from app.models.director import Director
from app.models.user import User

def initialize_database(db):
    User.create_table(db)
    Movie.create_table(db)
    Actor.create_table(db)
    Genre.create_table(db)
    Director.create_table(db)

def main():
    db_path = 'movies.db'
    db = MovieDatabase(db_path)

    # Initialize the database with tables
    initialize_database(db)

    while True:
        print("1. Insert Movie")
        print("2. Update Movie")
        print("3. Delete Movie")
        print("4. Get Movies")

        print("5. Insert Director")
        print("6. Update Director")
        print("7. Delete Director")
        print("8. Get Directors")

        print("9. Insert Actor")
        print("10. Update Actor")
        print("11. Delete Actor")
        print("12. Get Actors")

        print("13. Insert Genre")
        print("14. Update Genre")
        print("15. Delete Genre")
        print("16. Get Genres")

        print("17. Insert User")
        print("18. Update User")
        print("19. Delete User")
        print("20. Get Users")

        print("0. Exit")

        choice = int(input("Enter a choice: "))

        match choice:
            case 0:
                break
            case 1:
                title = input("Enter movie title: ")
                director = input("Enter director name: ")
                release = input("Enter relase date in the YYYY/MM/DD format: ")
                genre = input("Enter the genre: ")
                rating = float(input("Enter the rating: "))

                db.create_movie(title, director, release, genre, rating)
                print(f"Movie '{title}' added successfully!")
            case 2:
                id = int(input("Enter the movie ID to update: "))

                title = input("Enter new title (leave blank to keep the same): ")
                director = input("Enter new director (leave blank to keep the same): ")
                release = input("Enter new release date (leave blank to keep the same): ")
                genre = input("Enter new genre (leave blank to keep the same): ")
                rating_input = input("Enter new rating (leave blank to keep the same): ")

                title = title if title else None
                director = director if director else None
                release = release if release else None
                genre = genre if genre else None
                rating = float(rating_input) if rating_input else None

                db.update_movie(id,title,director,release,genre,rating)
            # case 3:
            case 4:
                results = db.fetchall("movies")
                for r in results:
                    print(f"ID: {r[0]}, Title: {r[1]}, Director: {r[2]}, Release Date: {r[3]}, Genre: {r[4]}, Rating: {r[5]}")
                temp = input("Press Enter to continue.")
            case 5:
                name = input("Enter name of director: ")
                birthday = input("Enter their birthday in YYYY/MM/DD format: ")
                nationality = input("Enther nationality of director: ")

                db.create_director(name, birthday, nationality)
                print(f"Director '{name}' added successfully!")
            # case 6:
            # case 7:
            case 8:
                results = db.fetchall("directors")
                for r in results:
                    print(f"ID: {r[0]}, Director name: {r[1]}, Birthday: {r[2]}, Nationality: {r[3]}")
                temp = input("Press Enter to continue.")
            case 9:
                name = input("Enter name of actor: ")
                birthday = input("Enter their birthday in YYYY/MM/DD format: ")
                nationality = input("Enther nationality of actor: ")

                db.create_actor(name, birthday, nationality)
                print(f"Actor '{name}' added successfully!")
            # case 10:
            # case 11:
            case 12:
                results = db.fetchall("actors")
                for r in results:
                    print(f"ID: {r[0]}, Actor name: {r[1]}, Birthday: {r[2]}, Nationality: {r[3]}")
                temp = input("Press Enter to continue")
            case 13:
                name = input("Enter the genre type: ")
                description = input("Type a sentence of description: ")

                db.create_genre(name, description)
                print(f"Genre '{name}' added successfully!")
            # case 14:
            # case 15:
            case 16:
                results = db.fetchall("genres")
                for r in results:
                    print(f"ID: {r[0]}, Genre: {r[1]}, Description: {r[2]}")
                temp = input("Press Enter to continue")
            case 17:
                username = input("Enter name of user: ")
                email = input("Enter user email: ")
                subscription = input("Enter user subscription status (Y/N): ")

                db.create_user(username,email,subscription)
                print(f"User '{username}' added successfully!")
            # case 18:
            # case 19:
            case 20:
                results = db.fetchall("users")
                for r in results:
                    print(f"ID: {r[0]}, Name: {r[1]}, Email: {r[2]}, Subscription: {r[3]}")
                temp = input("Press Enter to continue")


# if __name__ == "__main__":
#     main()



# from app.database import Database
# from app.models.user import User
# from app.models.movie import Movie
# from app.models.actor import Actor
# from app.models.genre import Genre
# from app.models.director import Director

# def initialize_database(db):
#     User.create_table(db)
#     Movie.create_table(db)
#     Actor.create_table(db)
#     Genre.create_table(db)
#     Director.create_table(db)

# def main():
#     db_path = 'data/movies.db'
#     db = Database(db_path)

#     # Initialize the database with tables
#     initialize_database(db)

#     # Example operations
#     db.create_user(username="john_doe", email="john@example.com")
#     user = db.get_user(1)
#     print(f"User: {user}")

#     db.create_director(name="Christopher Nolan")
#     director = db.get_director(1)
#     print(f"Director: {director}")

#     db.create_genre(name="Sci-Fi")
#     genre = db.get_genre(1)
#     print(f"Genre: {genre}")

#     db.create_movie(title="Inception", director_id=1, genre_id=1, release_year=2010)
#     movie = db.get_movie(1)
#     print(f"Movie: {movie}")

#     db.create_actor(name="Leonardo DiCaprio")
#     actor = db.get_actor(1)
#     print(f"Actor: {actor}")

if __name__ == "__main__":
    main()



        