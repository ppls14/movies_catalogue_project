from flask import Flask, render_template, request, redirect, url_for
import tmdb_client
from tmdb_client import get_movies

app = Flask(__name__)

movies_types_of_lists = {
        "Popularne": "popular", "Najlepiej oceniane ": "top_rated", "Nadchodzące": "upcoming", "Obecnie w kinach": "now_playing"
    }

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in movies_types_of_lists.values():
        return redirect(url_for('homepage'))
    movies = get_movies(list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, movies_types_of_lists= movies_types_of_lists)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)