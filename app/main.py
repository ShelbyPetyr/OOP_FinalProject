#Name       : 陳明龍   
#Student ID : 09163033

#Import necessary modules
from app.database import create_tables
from app.models.movie import Movie
from app.models.actor import Actor
from app.models.genre import Genre
from app.models.director import Director
from app.models.user import User

def main():
    create_tables()

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
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
            case 10:
            case 11:
            case 12:
            case 13:
            case 14:
            case 15:
            case 16:
            case 17:
            case 18:
            case 19:
            case 20:


if __name__ == "__main__":
    main()






        