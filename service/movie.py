# import required modules
from dao.movie import MovieDAO


# creating class to contain logics from DAO class
class MovieService:
    def __init__(self, dao: MovieDAO):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao

    def get_one(self, bid):
        """
        applying get_one() method to dao object
        :param bid: id of required movie
        :return:
        """
        return self.dao.get_one(bid)

    def get_all(self, filters):
        """
        checking what filter could be applied
        :param filters: possibly applied filters
        :return: movies according to filters
        """
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        """
        applying a create() method to dao object, using data form response
        """
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """
        getting id from data using get method (as data type is dict)
        getting movie to update using get_one with id, that was gotten
        creating fields of movie_to update with info, received from data, using get() method by field names
        :param movie_d: data from request body
        """
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
