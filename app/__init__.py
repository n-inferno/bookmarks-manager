import os

from flask import Flask
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI'))

api = Api(app)

db = SQLAlchemy(app)


basic_auth = HTTPBasicAuth(os.environ.get('AUTH_STRING'))
token_auth = HTTPTokenAuth(scheme='Bearer')


from app.resources.smoke import Smoke
from app.resources.bookmarks import Bookmarks
from app.resources.bookmarks import BookmarksByUUID
