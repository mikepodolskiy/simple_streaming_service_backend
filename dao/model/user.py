# import required libraries and modules
from marshmallow import Schema, fields
from setup_db import db


# creating class as inheritance of Model class, cols acc to UML
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  # unique parameter provision, user with same name
    # will not be created
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    role = db.Column(db.String(50))
    favorite_genre = db.Column(db.String(100), db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre")



# creating Schema class as inheritance of Schema for serialization
class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    role = fields.Str()
    favorite_genre = fields.Int()
