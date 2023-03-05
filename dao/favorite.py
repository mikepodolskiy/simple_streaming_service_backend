# import required modules
from sqlalchemy import desc

from dao.model.favorite import Favorite

class FavoriteDAO:
    # creating constructor, getting object - session and save it in itself. session could be with different db type (
    # sqlite... etc)
    def __init__(self, session):
        self.session = session
    def create(self, favorite_d):
        """
        creating Favorite class object using data
        requesting to session to add favorite
        requesting to session to commit changes to save info
        :param favorite_d: data from request body
        :return: favorite that was added (not necessary)
        """
        ent = Favorite(**favorite_d)
        self.session.add(ent)
        self.session.commit()
        return ent


    def get_one(self, mid):
        """
        using session, requesting to db to required class, getting data by id
        :param mid: required id
        :return: data of element with required id
        """
        return self.session.query(Favorite).get(mid)

    def delete(self, mid):
        """
        getting favorite to delete using get_one with id
        :param mid: id of required favorite
        :return: nothing
        """
        favorite = self.get_one(mid)
        self.session.delete(favorite)
        self.session.commit()

