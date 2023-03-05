# import required libraries and modules

from flask import request
from flask_restx import Resource, Namespace
from dao.model.favorite import FavoriteSchema
from implemented import favorite_service, user_service
from service.auth import auth_required, get_email_from_token, get_name_from_token

# creating namespace
favorite_ns = Namespace('favorites')


# creating class based views using namespaces for all required endpoints
@favorite_ns.route('/movies/<int:mid>')
class UsersView(Resource):
    @auth_required
    def post(self, mid):
        favorite_d = {"movie_id": mid}
        email = get_email_from_token()
        filters = {"email": email}
        user = user_service.get_one_by_key(filters)
        favorite_d["user_id"] = user.id
        favorite_service.create(favorite_d)

        return "", 204


    def delete(self, mid):
        favorite_d = {"movie_id": mid}
        email = get_email_from_token()
        filters = {"email": email}
        user = user_service.get_one_by_key(filters)
        favorite_d["user_id"] = user.id
        favorite_service.delete(favorite_d)

        return "", 204
