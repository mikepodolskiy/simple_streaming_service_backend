# import required modules
from dao.model.genre import Genre


# creating class for interaction with db
class GenreDAO:
    # creating constructor, getting object - session and save it in itself. session could be with different db type (
    # sqlite... etc)
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        using session, requesting to db to required class, getting data by id
        :param bid: required id
        :return: data of element with required id
        """
        return self.session.query(Genre).get(bid)

    def get_all(self):
        """
        using session, requesting to db to required class, getting all data
        :return: all data of required class
        """
        return self.session.query(Genre).all()

    def create(self, genre_d):
        """
        creating Genre class object using data
        requesting to session to add movie
        requesting to session to commit changes to save info
        :param genre_d: data from request body
        :return: movie that was added (not necessary)
        """
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        getting genre to delete using get_one with id
        :param rid: id of required genre
        :return: nothing
        """
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        """
        requesting to session to add movie and commit
        :param genre_d: element to be updated
        :return: updated element (not necessary)
        """
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
