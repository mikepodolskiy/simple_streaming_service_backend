# import required modules
from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
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

    def create(self, director_d):
        """
        applying  to dao object create() method
        :param director_d: genre data
        """
        return self.dao.create(director_d)

    def update(self, director_d):
        """
        applying  to dao object update() method
        :param director_d: director data
        """
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """
        applying  to dao object update() method
        :param rid: id of director to delete
        """
        self.dao.delete(rid)
