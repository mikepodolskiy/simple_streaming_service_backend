# import required modules
import base64
import hashlib
from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.dao.user import UserDAO


# creating class to contain logics from DAO class
class UserService:
    def __init__(self, dao: UserDAO):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao

    def get_one(self, uid):
        """
        applying get_one() method to dao object
        :param uid: id of required user
        """
        return self.dao.get_one(uid)

    def get_one_by_key(self, filters):
        """
        applying to dao object method to get data from db by columns name (could be expanded for more than just
        email filters)
        :param filters: dict with data
        :return: method applying or None if keyword not in filters
        """
        if filters.get("email") is not None:
            return self.dao.get_by_email(filters.get("email"))
        return None

    def get_all(self):
        """
        checking what filter could be applied
        :return: users according to filters
        """

        return self.dao.get_all()

    def create(self, user_d):
        """
        applying a create() method to dao object, using data form response
        """
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        """
        applying  to dao object update() method
        :param user_d: user data
        """
        user_d['password'] = self.get_hash(user_d['password'])
        self.dao.update(user_d)
        return self.dao

    def update_partial(self, user_d):
        """
        checking what fields to update in data creating fields of movie_to update with info, received from data,
        using get() method by field names
        :param user_d: data from request body
        """

        user_d_to_update = self.get_one_by_key(user_d)
        if 'name' in user_d:
            user_d_to_update.name = user_d.get('name')
        if 'surname' in user_d:
            user_d_to_update.surname = user_d.get('surname')
        if 'favorite_genre' in user_d:
            user_d_to_update.favorite_genre = user_d.get('favorite_genre')

        self.dao.update(user_d_to_update)

    def update_password(self, user_d):
        """
        checking password correctness
        checking what fields to update in data creating fields of movie_to update with info, received from data,
        using get() method by field names
        :param user_d: data from request body
        """

        user_d_to_update = self.get_one_by_key(user_d)
        if None in user_d.values():
            return {"message": "data incomplete"}, 401


        if 'password_2' in user_d:
            user_d_to_update.password = self.get_hash(user_d.get('password_2'))


        self.dao.update(user_d_to_update)

        return "", 204



    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        """
        getting password as string, converted to bytes using pbkdf2_hmac as
        sha256 secure hash algorithm shall be used, salt and number of iterations from constants
        :return: password hash as string
        """
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)
