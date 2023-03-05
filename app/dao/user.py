# import required modules
from app.dao.model.user import User


# creating class for interaction with db
class UserDAO:
    # creating constructor, getting object - session and save it in itself. session could be with different db type (
    # sqlite... etc)
    def __init__(self, session):
        self.session = session

    # creating methods for CRUD
    def get_one(self, uid):
        """
        using session, requesting to db to required class, getting data by id
        :param uid: required id
        :return: data of element with required id
        """
        return self.session.query(User).get(uid)

    def get_all(self):
        """
        using session, requesting to db to required class, getting all data
        :return: all data of required class
        """
        return self.session.query(User).all()

    def get_by_email(self, val):
        """
        using session, requesting to db to required class with requested filter
        :param val: required email
        :return: required user data
        """
        return self.session.query(User).filter(User.email == val).first()

    def create(self, user_d):
        """
        creating User class object using data
        requesting to session to add user
        requesting to session to commit changes to save info
        :param user_d: data from request body
        :return: user that was added (not necessary)
        """
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, user_d):
        """
        requesting to session to add movie and commit
        :param user_d: element to be updated
        :return: updated element (not necessary)
        """

        self.session.add(user_d)
        self.session.commit()

        return user_d

    def delete(self, rid):
        """
        getting user to delete using get_one with id
        :param rid: id of required user
        :return: nothing
        """
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()
