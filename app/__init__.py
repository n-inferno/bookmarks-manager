import os

from flask import Flask
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI'))

auth = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API'
    },
}

api = Api(app, authorizations=auth)

db = SQLAlchemy(app)

basic_auth = HTTPBasicAuth(os.environ.get('AUTH_STRING'))
token_auth = HTTPTokenAuth(scheme='Bearer')

from app.resources.auth import AuthToken
from app.resources.smoke import Smoke
from app.resources.bookmarks import Bookmarks
from app.resources.bookmarks import BookmarksByUUID
