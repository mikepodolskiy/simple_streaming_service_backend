# import required modules
import hashlib
import hmac
import datetime
import calendar
import jwt
from flask import request
from flask_restx import abort
from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, auth_secret as secret, algo


def check_request_integrity(param_list):
    """
    func for using to check if data contains all required fields
    :param param_list: list type object, containing required data
    :return: if None in data
    """
    return None in param_list


def check_user_exist(user):
    """
    func to check if user from db request is not None
    :param user: user to be requested from db
    """
    return user is None


def compare_passwords(hash_password, base_password):
    """
    func to compare two passwords
    :param hash_password: hashed password (from POST request)
    :param base_password: user's password in db
    :return: True if compare successful
    """
    return hmac.compare_digest(
        hash_password,
        hashlib.pbkdf2_hmac(
            'sha256',
            base_password,
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
    )


def generate_access_token(data):
    """
    func to generate access token for 30 minutes expire
    :param data: user data
    :return: access token
    """
    token_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data['exp'] = calendar.timegm((token_time.timetuple()))
    return jwt.encode(data, secret, algorithm=algo)


def generate_refresh_token(data):
    """
        func to generate refresh token for 130 days expire
        :param data: user data
        :return: refresh token
        """
    token_time = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data['exp'] = calendar.timegm((token_time.timetuple()))
    return jwt.encode(data, secret, algorithm=algo)


def auth_required(func):
    """
    check authorization decorator
    :param func: func to be decorated
    """

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
    check role decorator
    :param func: func to be decorated
    """

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None

        try:
            user = jwt.decode(token, secret, algorithms=[algo])
            role = user.get('role', 'user')

        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

        if role != 'admin':
            abort(403)

        return func(*args, **kwargs)

    return wrapper



def get_email_from_token():

    if 'Authorization' not in request.headers:
        abort(401)

    data = request.headers['Authorization']
    token = data.split('Bearer ')[-1]

    try:
        jwt.decode(token, secret, algorithms=[algo])

    except Exception as e:
        print('JWT Decode Exception', e)
        abort(401)

    user = jwt.decode(token, secret, algorithms=[algo])
    email = user.get('email')

    if not email:
        return {'message': 'Token not match'}, 401

    return email


def get_name_from_token():

    if 'Authorization' not in request.headers:
        abort(401)

    data = request.headers['Authorization']
    token = data.split('Bearer ')[-1]

    try:
        jwt.decode(token, secret, algorithms=[algo])

    except Exception as e:
        print('JWT Decode Exception', e)
        abort(401)

    user = jwt.decode(token, secret, algorithms=[algo])
    name = user.get('name')
    print(name)

    if not name:
        return {'message': 'Token not match'}, 401

    return name