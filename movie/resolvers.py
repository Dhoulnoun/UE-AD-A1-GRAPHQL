import json


def movie_with_id(_, info, _id):
    with open('{}/data/movies.json'.format("."), 'r') as f:
        movies = json.load(f)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie


def actor_with_id(_, info, _id):
    with open('{}/data/actors.json'.format("."), 'r') as f:
        actors = json.load(f)
        for actor in actors['actors']:
            if actor['id'] == _id:
                return actor


def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors


def resolve_movies_in_actor(actor, info):
    with open('{}/data/movies.json'.format("."), "r") as file:
        data = json.load(file)
        movies = [movie for movie in data['movies'] if actor['id'] in movie['actors']]
        return movies


def update_movie_rate(_, info, _id, _rate):
    new_movie = {}
    new_movies = {}
    with open('{}/data/movies.json'.format("."), 'r') as f:
        movies = json.load(f)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                new_movie = movie
                new_movies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(new_movies, wfile)
    return new_movie
