# import required libraries and modules

from flask import request
from flask_restx import Resource, Namespace, abort
from app.dao.model.user import UserSchema
from app.implemented import user_service
from app.service.auth import auth_required, admin_required, get_email_from_token, check_request_integrity, compare_passwords

# creating namespace
user_ns = Namespace('users')


# creating class based views using namespaces for all required endpoints
@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        """
        getting all users list using method get_all of UserService class object
        using serialization with Schema class object
        :return: users list
        """
        email = get_email_from_token()
        filters = {'email': email}
        r = user_service.get_one_by_key(filters)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    def patch(self):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update_partial() of MovieService class object

        :return: response code
        """
        request_data = request.json
        request_data["email"] = get_email_from_token()
        user_service.update_partial(request_data)

        return '', 204


@user_ns.route('/password')
class UserPass(Resource):
    @auth_required
    def put(self):
        """
        changing password - from password_1 to password_2, collected from request body as dict {"password_1":
        password_1, "password_2": password_2} only if password_1 is correct
        """
        request_data = request.json
        password_1 = request_data.get('password_1', None)
        password_2 = request_data.get('password_2', None)
        # check if data is existing, otherwise abort
        if check_request_integrity([password_1, password_2]):
            abort(400)

        email = get_email_from_token()
        filters = {'email': email,
                   'password': password_1
                   }
        # get user by email from db
        user = user_service.get_one_by_key(filters)

        # hash user password from request
        password_hash = user_service.get_hash(password_1)

        # check password correctness, otherwise return error
        if compare_passwords(password_hash, user.password):
            return {"error": "Wrong user data"}, 401

        request_data["email"] = get_email_from_token()

        user_service.update_password(request_data)
        return '', 204



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

    def delete(self, uid):
        """
        delete user with required id, using method delete() of MovieService class object

        :param uid: id of required user to be deleted
        :return: response code
        """
        user_service.delete(uid)
        return "", 204
