# import required libraries and modules
from marshmallow import Schema, fields
from app.setup_db import db


# creating class as inheritance of Model class, cols acc to UML
class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    movie = db.relationship("Movie")


# creating Schema class as inheritance of Schema for serialization
class FavoriteSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    movie_id = fields.Int()
