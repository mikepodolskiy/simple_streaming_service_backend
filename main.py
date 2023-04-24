# import required libraries and modules
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Swagger

from app.config import Config
from app.setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns
from app.views.auth import auth_ns
from app.views.favorites import favorite_ns


# creating and configuring app in function
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# adding sqlalchemy and rest-x, adding namespaces in function
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorite_ns)


# creating app using function
app = create_app(Config())
app.debug = True
migrate = Migrate(app, db, render_as_batch=True)
# run app with import check
if __name__ == '__main__':
    app.run(host="localhost", port=25000, debug=True)
    Swagger(app)

