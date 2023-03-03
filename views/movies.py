# import required libraries and modules
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from service.auth import auth_required, admin_required

# creating namespaces for movies
movie_ns = Namespace('movies')


# creating class based views using namespaces for all required endpoints
@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """
        getting all movies list or movies with filter using method get_all of MovieService class object
        using serialization with Schema class object
        :return: movies list
        """
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @admin_required
    def post(self):
        """
        getting data from request, transforming data using .json
        creating new element using create(transformed data) method for MovieService class object
        :return: info message,response code
        """
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        """
        getting one movie using method get_one of MovieService class object
        using serialization with Schema class object
        :return: movie with required id - dict
        """
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update() of MovieService class object
        :param bid: element to update id
        :return: response code
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, bid):
        """
        delete movie with required id, using method delete() of MovieService class object

        :param bid: id of required movie to be deleted
        :return: response code
        """
        movie_service.delete(bid)
        return "", 204
