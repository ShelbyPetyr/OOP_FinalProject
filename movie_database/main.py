#Name       : 陳明龍   
#Student ID : 09163033

#Import necessary modules
from database import MovieDatabase
import os
from models.movie import Movie
from models.actor import Actor
from models.genre import Genre
from models.director import Director
from models.user import User

def initialize_database(db):
    User.create_table(db)
    Movie.create_table(db)
    Actor.create_table(db)
    Genre.create_table(db)
    Director.create_table(db)

def main():
    db_path = 'data/movies.db'
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
            case 1: #Insert movie
                title = input("Enter movie title: ")
                director = input("Enter director name: ")
                release = input("Enter relase date in the YYYY/MM/DD format: ")
                genre = input("Enter the genre: ")
                rating = float(input("Enter the rating: "))

                db.create_movie(title, director, release, genre, rating)
                print(f"Movie '{title}' added successfully!")
            case 2: #Update movie
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
            case 3: #Delete movie
                id = int(input("Enter movie id to delete: "))
                db.delete_movie(id)
            case 4: #Get movies
                results = db.fetchall("movies")
                for r in results:
                    print(f"ID: {r[0]}, Title: {r[1]}, Director: {r[2]}, Release Date: {r[3]}, Genre: {r[4]}, Rating: {r[5]}")
                temp = input("Press Enter to continue.")

            case 5: #Insert Director
                name = input("Enter name of director: ")
                birthday = input("Enter their birthday in YYYY/MM/DD format: ")
                nationality = input("Enther nationality of director: ")

                db.create_director(name, birthday, nationality)
                print(f"Director '{name}' added successfully!")
            case 6: #Update director
                id = int(input("Enter the director ID to update: "))

                name = input("Enter new director name (leave blank to keep the same): ")
                birthday = input("Enther new birthday (leave blank to keep the same): ")
                nationality = input("Enter new nationality (leave blank to keep the same): ")

                name = name if name else None
                birthday = birthday if birthday else None
                nationality = nationality if nationality else None

                db.update_director(id,name,birthday,nationality)
            case 7: #Delete director
                id = int(input("Enter director ID to delete: "))
                db.delete_director(id)
            case 8: #Get directors
                results = db.fetchall("directors")
                for r in results:
                    print(f"ID: {r[0]}, Director name: {r[1]}, Birthday: {r[2]}, Nationality: {r[3]}")
                temp = input("Press Enter to continue.")

            case 9: #Insert actor
                name = input("Enter name of actor: ")
                birthday = input("Enter their birthday in YYYY/MM/DD format: ")
                nationality = input("Enther nationality of actor: ")

                db.create_actor(name, birthday, nationality)
                print(f"Actor '{name}' added successfully!")
            case 10: #Update actor
                id = int(input("Enter the actor ID to update: "))

                name = input("Enter new actor name (leave blank to keep the same): ")
                birthday = input("Enther new birthday (leave blank to keep the same): ")
                nationality = input("Enter new nationality (leave blank to keep the same): ")

                name = name if name else None
                birthday = birthday if birthday else None
                nationality = nationality if nationality else None

                db.update_actor(id,name,birthday,nationality)
            case 11: #Delete actor
                id = int(input("Enter actor ID to delete: "))
                db.delete_actor(id)
            case 12: #Get actors
                results = db.fetchall("actors")
                for r in results:
                    print(f"ID: {r[0]}, Actor name: {r[1]}, Birthday: {r[2]}, Nationality: {r[3]}")
                temp = input("Press Enter to continue")

            case 13: #Insert genre
                name = input("Enter the genre type: ")
                description = input("Type a sentence of description: ")

                db.create_genre(name, description)
                print(f"Genre '{name}' added successfully!")
            case 14: #Update genre
                id = int(input("Enter genre ID to update: "))
                name = input("Enter new name (leave blank to keep the same): ")
                description = input("Enter new description (leave black to keep the same): ")

                name = name if name else None
                description = description if description else None

                db.update_genre(id,name,description)
            case 15: #Delete genre
                id = int(input("Enter genre ID to delete: "))
                db.delete_genre(id)
            case 16: #Get genres
                results = db.fetchall("genres")
                for r in results:
                    print(f"ID: {r[0]}, Genre: {r[1]}, Description: {r[2]}")
                temp = input("Press Enter to continue")

            case 17: #Insert user
                username = input("Enter name of user: ")
                email = input("Enter user email: ")
                subscription = input("Enter user subscription status (Y/N): ")

                db.create_user(username,email,subscription)
                print(f"User '{username}' added successfully!")
            case 18: #Update user
                id = int(input("Enter user ID to update: "))
                username = input("Enter new username (leave blank to keep the same): ")
                email = input("Enter new email (leave blank to keep the same): ")
                subscription = input("Enter subscription status (Y/N) (leave blank to keep the same): ")

                username=username if username else None
                email=email if email else None
                subscription=subscription if subscription else None

                db.update_user(id,username,email,subscription)
            case 19: #Delete user
                id = int(input("Enter user ID to delete: "))
                db.delete_user(id)
            case 20: #Get users
                results = db.fetchall("users")
                for r in results:
                    print(f"ID: {r[0]}, Name: {r[1]}, Email: {r[2]}, Subscription: {r[3]}")
                temp = input("Press Enter to continue")

if __name__ == "__main__":
    main()



        