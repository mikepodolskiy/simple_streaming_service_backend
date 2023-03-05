# import required libraries and modules
import jwt
from flask import request
from flask_restx import Resource, Namespace, abort
from app.implemented import user_service
from app.constants import auth_secret as secret, algo
from app.service.auth import check_request_integrity, check_user_exist, compare_passwords, generate_access_token, \
    generate_refresh_token

# creating namespace
auth_ns = Namespace('auth')


# creating class based views using namespaces for register endpoints
@auth_ns.route('/register/')
class AuthRegView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email', None)
        password = req_json.get('password', None)
        name = req_json.get('name', None)
        surname = req_json.get('surname', None)
        role = req_json.get("role", "user")
        favorite_genre = req_json.get('favorite_genre', None)
        user_data = {"email": email,
                     "password": password,
                     "name": name,
                     "surname": surname,
                     "role": role,
                     "favorite_genre": favorite_genre
                     }
        user_service.create(user_data)

        return "", 201

# creating class based views using namespaces for login endpoints
@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email', None)
        password = req_json.get('password', None)
        filters = {'email': email,
                   'password': password
                   }
        # check if data is existing, otherwise abort
        if check_request_integrity([email, password]):
            abort(400)

        # get user by email from db, check if user exists, otherwise return error
        user = user_service.get_one_by_key(filters)

        if check_user_exist(user):
            return {"error": "User not exist"}, 401

        # hash user password from request
        password_hash = user_service.get_hash(password)

        # check password correctness, otherwise return error
        if compare_passwords(password_hash, user.password):
            return {"error": "Wrong user data"}, 401

        # generating tokens
        data = {
            'email': user.email,
            'role': user.role,
        }
        access_token = generate_access_token(data)
        refresh_token = generate_refresh_token(data)

        return {'access_token': access_token, 'refresh_token': refresh_token}, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token', None)
        if check_request_integrity([refresh_token]):
            abort(400)
        try:
            data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        except Exception as e:
            abort(400)
        email = data.get('email')
        filters = {'email': email}
        # get user by email from db, check if user exists, otherwise return error
        user = user_service.get_one_by_key(filters)

        # generating tokens
        data = {
            'email': user.email,
            'role': user.role,
        }
        access_token = user_service.generate_access_token(data)
        refresh_token = user_service.generate_refresh_token(data)

        return {'access_token': access_token, 'refresh_token': refresh_token}, 201
