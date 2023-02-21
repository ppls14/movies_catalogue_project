import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNTliNjliMjQ5NzcwZWViMmY2YjEzZmI0Y2Y4ZjRlYiIsInN1YiI6IjYzZjFmYzQ0YTY3MjU0MDA3ZGU4ZjZhYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4c_fYVmO7MczCLVv6qJ_pQ2dLTYMRRDsZW7019u04wU"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"