# import required modules
from dao.favorite import FavoriteDAO

# creating class to contain logics from DAO class
# creating class to contain logics from DAO class
class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao
