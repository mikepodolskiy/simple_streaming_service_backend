# import required modules
from dao.director import DirectorDAO
from constants import director_page_limit as page_limit



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
        applying get_all() method to dao object if no page in request otherwise apply show_by_page method
        """
        page = filters.get("page")
        if page is not None:
            page=int(page)
            directors = self.dao.get_all()
            directors_to_show = self.show_by_page(page, page_limit, directors)
        else:
            directors_to_show = self.dao.get_all()
        return directors_to_show

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
