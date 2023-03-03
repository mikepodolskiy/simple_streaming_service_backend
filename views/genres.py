# import required libraries and modules
from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service
from service.auth import auth_required, admin_required

# creating namespace
genre_ns = Namespace('genres')


# creating class based views using namespaces for all required endpoints
@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """
        getting all genres list using method get_all of GenreService class object
        using serialization with Schema class object
        :return: genres list
        """
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """
        getting data from request, transforming data using .json
        creating new element using create(transformed data) method for MovieService class object
        :return: info message,response code
        """
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/movies/{genre.id}"}


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        """
        getting one genre dict using method get_one of GenreService class object
        using serialization with Schema class object
        :return: genre with required id - dict
        """
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, gid):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update() of MovieService class object
        :param gid: element to update id
        :return: response code
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, gid):
        """
        delete movie with required id, using method delete() of MovieService class object

        :param gid: id of required movie to be deleted
        :return: response code
        """
        genre_service.delete(gid)
        return "", 204
