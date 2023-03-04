# import required modules
from dao.movie import MovieDAO
from constants import movie_page_limit as page_limit


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

    def show_by_page(self, page, page_lim, list_):
        """
        evaluate consistent of page to show and return it
        :param page: number of page to be shown
        :param page_lim: number of elements on one page
        :param list_: initial list with data
        :return: list of elements with required filter
        """
        if page * page_lim < len(list_):
            list_to_show = [list_[index] for index in range((page - 1) * page_lim, page * page_lim)]

        else:
            list_to_show = [list_[index] for index in range((page - 1) * page_lim, len(list_))]
        return list_to_show

    def get_all(self, filters):
        """
        checking what filter could be applied
        :param filters: possibly applied filters
        :return: movies according to filters
        """
        status = filters.get("status")
        page = filters.get("page")
        if page is not None:
            page = int(page)


            if status == 'new':
                movies = self.dao.get_all_by_year()
                movies_to_show = self.show_by_page(page, page_limit, movies)
            else:
                movies = self.dao.get_all()
                movies_to_show = self.show_by_page(page, page_limit, movies)

        elif status and status == "new":
            movies_to_show = self.dao.get_all_by_year()

        else:
            movies_to_show = self.dao.get_all()
        return movies_to_show

    def get_all_by_year(self):
        return self.dao.get_all_by_year()

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
