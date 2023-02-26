import requests, json, random
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNTliNjliMjQ5NzcwZWViMmY2YjEzZmI0Y2Y4ZjRlYiIsInN1YiI6IjYzZjFmYzQ0YTY3MjU0MDA3ZGU4ZjZhYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4c_fYVmO7MczCLVv6qJ_pQ2dLTYMRRDsZW7019u04wU"

def get_movies_list(list_type = "popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movies(list_type, how_many=8):
    movies = []
    list_of_movie = get_movies_list(list_type)['results']
    for _ in range(int(how_many)):
        movies.append(list_of_movie[_])
    return movies
