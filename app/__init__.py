from flask import Flask
from flask_restx import Api


app = Flask(__name__)
api = Api(app)


from app.resources.smoke import Smoke
from app.resources.bookmarks import Bookmarks
from app.resources.bookmarks import BookmarksByUUID