# import required modules
from dao.model.director import Director


# creating class for interaction with db
class DirectorDAO:
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
        return self.session.query(Director).get(bid)

    def get_all(self):
        """
        using session, requesting to db to required class, getting all data
        :return: all data of required class
        """
        return self.session.query(Director).all()

    def create(self, director_d):
        """
        creating Director class object using data
        requesting to session to add movie
        requesting to session to commit changes to save info
        :param director_d: data from request body
        :return: movie that was added (not necessary)
        """
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        getting genre to delete using get_one with id
        :param rid: id of required director
        :return: nothing
        """
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """
        requesting to session to add movie and commit
        :param director_d: element to be updated
        :return: updated element (not necessary)
        """
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
