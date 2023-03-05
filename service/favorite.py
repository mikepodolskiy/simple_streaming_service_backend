# import required modules
from dao.favorite import FavoriteDAO


# creating class to contain logics from DAO class
class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao

    def create(self, favorite_d):
        """
            applying  to dao object create() method
            :param genre_d: genre data
            """
        return self.dao.create(favorite_d)



    def delete(self, filters):
        """
                applying  to dao object delete() method
                :param fid: id of favorite to delete
                """
        favorite_answer = self.dao.get_by_filters(filters)
        favorite = favorite_answer[0]
        fid = favorite.id
        self.dao.delete(fid)
