# import required libraries and modules
from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service
from service.auth import auth_required, admin_required

# creating namespace
director_ns = Namespace('directors')


# creating class based views using namespaces for all required endpoints
@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """
        getting all directors list using method get_all of DirectorService class object
        using serialization with Schema class object
        :return: directors list
        """
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """
        getting data from request, transforming data using .json
        creating new element using create(transformed data) method for MovieService class object
        :return: info message,response code
        """
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/movies/{director.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        """
        getting one director dict using method get_one of DirectorService class object
        using serialization with Schema class object
        :return: director with required id - dict
        """
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, did):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update() of MovieService class object
        :param did: element to update id
        :return: response code
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, did):
        """
        delete movie with required id, using method delete() of MovieService class object

        :param did: id of required movie to be deleted
        :return: response code
        """
        director_service.delete(did)
        return "", 204
