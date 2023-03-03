# import required libraries and modules

from flask import request
from flask_restx import Resource, Namespace
from dao.model.user import UserSchema
from implemented import user_service
from service.auth import admin_required

# creating namespace
user_ns = Namespace('users')


# creating class based views using namespaces for all required endpoints
@user_ns.route('/')
class UsersView(Resource):
    @admin_required
    def get(self):
        """
        getting all users list using method get_all of UserService class object
        using serialization with Schema class object
        :return: users list
        """
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        """
        getting data from request, transforming data using .json
        creating new element using create(transformed data) method for MovieService class object
        :return: info message,response code
        """
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/movies/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def get(self, uid):
        """
        getting one user dict using method get_one of UserService class object
        using serialization with Schema class object
        :return: user with required id - dict
        """
        r = user_service.get_one(uid)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    def put(self, uid):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update() of MovieService class object
        :param uid: element to update id
        :return: response code
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        """
        delete movie with required id, using method delete() of MovieService class object

        :param uid: id of required movie to be deleted
        :return: response code
        """
        user_service.delete(uid)
        return "", 204
