from flask import Flask,request,jsonify,g
import sqlite3

app = Flask(__name__)

DATABASE = 'data/movies.db'

# connect to our DB
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#Homepage
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Movie Database Management"

#API 1: Get all movies
@app.route('/get-movies', methods=['GET'])
def get_movies():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    movie_list = []
    for m in movies:
        m_dict = {
            'Title': m[1],
            'Director': m[2],
            'Release date': m[3],
            'Genre': m[4],
            'Rating': m[5]
        }
        movie_list.append(m_dict)
    
    return jsonify(movie_list)

#API 2: Get all directors
@app.route('/get-directors', methods=['GET'])
def get_directors():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM directors")
    directors = cursor.fetchall()

    director_list = []
    for d in directors:
        d_dict = {
            "Name": d[1],
            "Birthday": d[2],
            "Nationality": d[3]
        }
        director_list.append(d_dict)
    return jsonify(director_list)

#API 3: Get all actors
@app.route('/get-actors', methods=['GET'])
def get_actors():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM actors")
    actors = cursor.fetchall()

    actor_list = []
    for a in actors:
        a_dict = {
            "Name": a[1],
            "Birthday": a[2],
            "Nationality": a[3]
        }
        actor_list.append(a_dict)
    return jsonify(actor_list)



if __name__ == '__main__':
     app.run(debug=True)