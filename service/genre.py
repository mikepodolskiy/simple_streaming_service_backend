# import required modules
from dao.genre import GenreDAO


# creating class to contain all logics from DAO class
class GenreService:
    def __init__(self, dao: GenreDAO):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao

    def get_one(self, bid):
        """
        applying get_one() method to dao object

        :param bid: id of required movie
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        applying get_all() method to dao object
        """
        return self.dao.get_all()

    def create(self, genre_d):
        """
        applying  to dao object create() method
        :param genre_d: genre data
        """
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """
        applying  to dao object update() method
        :param genre_d: genre data
        """
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """
        applying  to dao object update() method
        :param rid: id of genre to delete
        """
        self.dao.delete(rid)
