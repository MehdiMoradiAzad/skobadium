from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from authz.config import Config

db = SQLAlchemy()
ma = Marshmallow()
mg = Migrate()

api = Api()

from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configs from ENV variables
    db.init_app(app)
    ma.init_app(app)
    mg.init_app(app, db)
    api.init_app(app)
    return app
