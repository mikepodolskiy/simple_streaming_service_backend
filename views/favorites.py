# import required libraries and modules

from flask import request
from flask_restx import Resource, Namespace
from dao.model.favorite import FavoriteSchema
from implemented import user_service
from service.auth import auth_required

# creating namespace
favorite_ns = Namespace('favorites')


# creating class based views using namespaces for all required endpoints
@favorite_ns.route('/movies/<int:mid>')
class UsersView(Resource):
    @auth_required
    def post(self, mid):
        pass


    def delete(self, mid):
        pass