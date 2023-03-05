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


    def get_one(self, fid):
        """
        using session, requesting to db to required class, getting data by id
        :param fid: required id
        :return: data of element with required id
        """
        return self.session.query(Favorite).get(fid)


    def get_by_filters(self, filters):
        request = self.session.query(Favorite)
        if "movie_id" in filters:
            request = request.filter(Favorite.movie_id == filters.get("movie_id"))
        if "user_id" in filters:
            request = request.filter(Favorite.user_id == filters.get("user_id"))
        return request.all()


    def delete(self, fid):
        """
        getting favorite to delete using get_one with id
        :param fid: id of required favorite
        :return: nothing
        """
        favorite = self.get_one(fid)
        self.session.delete(favorite)
        self.session.commit()

