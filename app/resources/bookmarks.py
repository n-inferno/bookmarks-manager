from flask_restx import Resource, reqparse, abort

from app import api
from app.db_models.bookmark_model import Bookmark
from app.marshaling_models.bookmarks import bookmark_model


parser = reqparse.RequestParser()
parser.add_argument('link', type=str, required=True, help='Link is not in request')
parser.add_argument('comment', type=str, help='Comment is not in request')
parser.add_argument('group', type=str, help='Group is not in request')

parser_uuid = reqparse.RequestParser()
parser_uuid.add_argument('uuid', required=True, type=str)

bookmarks = []


@api.route('/bookmarks')
class Bookmarks(Resource):
    @api.marshal_with(bookmark_model)
    def get(self):
        """get all bookmarks"""
        return bookmarks

    @api.marshal_with(bookmark_model)
    @api.expect(parser)
    def post(self):
        """create new bookmark"""
        args = parser.parse_args()
        link, comment, group = args.get('comment'), args.get('link'), args.get('group')

        new = Bookmark(user_id=1, link=link, comment=comment, group=group)
        bookmarks.append(new)

        return new


@api.route('/bookmarks/<uuid>')
class BookmarksByUUID(Resource):
    @api.marshal_with(bookmark_model)
    def get(self, uuid):
        """get bookmark by uuid"""
        if uuid:
            search_result = list(filter(lambda x: str(x.bookmark_uuid) == uuid, bookmarks))
            if search_result:
                return search_result[0]
            abort(404, 'Bookmark not found')
        abort(404, 'UUID not in request')
