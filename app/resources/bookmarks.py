from flask import request
from flask_restx import Resource, reqparse
from werkzeug.exceptions import NotFound, BadRequest

from app import api, db
from app.db_models.bookmark_model import BookmarkModel
from app.helpers.auth import token_required
from app.marshaling_models.bookmarks import bookmark_model_base, bookmark_model_with_uuid


bookmarks_namespace = api.namespace('bookmarks', description='Operations with bookmarks')

parser_link = reqparse.RequestParser()
parser_link.add_argument('link', type=str, required=True, help='Link you want to save')

bookmarks = []


@bookmarks_namespace.route('')
class Bookmarks(Resource):
    @bookmarks_namespace.marshal_with(bookmark_model_with_uuid)
    @api.doc(security='apiKey')
    @token_required
    def get(self):
        """get all bookmarks"""
        bookmarks = db.session.query(BookmarkModel).all()
        return bookmarks

    @bookmarks_namespace.marshal_with(bookmark_model_with_uuid, code=201, description='Created')
    @bookmarks_namespace.expect(bookmark_model_base)
    @api.doc(security='apiKey')
    @token_required
    def post(self):
        """create new bookmark"""
        _ = parser_link.parse_args().get('link')
        data = request.json

        new = BookmarkModel(user_id=1, **data)
        db.session.add(new)
        db.session.commit()
        return new, 201


@bookmarks_namespace.route('/<uuid>')
class BookmarksByUUID(Resource):
    @bookmarks_namespace.marshal_with(bookmark_model_with_uuid)
    @api.doc(security='apiKey')
    @token_required
    def get(self, uuid):
        """get bookmark by uuid"""
        if uuid:
            search_result = db.session.query(BookmarkModel).filter_by(bookmark_uuid=uuid).first()
            if not search_result:
                raise NotFound('Bookmark not found')
            return search_result
        raise BadRequest('UUID not in request')

    @bookmarks_namespace.marshal_with(bookmark_model_with_uuid)
    @bookmarks_namespace.expect(bookmark_model_base)
    @api.doc(security='apiKey')
    @token_required
    def put(self, uuid):
        """update bookmark by uuid"""
        link = parser_link.parse_args().get('link')
        data = request.json
        bookmark = db.session.query(BookmarkModel).filter_by(bookmark_uuid=uuid).first()
        if not bookmark:
            raise NotFound('Bookmark not found')
        bookmark.update(link=link, comment=data.get('comment'), link_group=data.get('link_group'))
        db.session.commit()
        return bookmark

    @bookmarks_namespace.marshal_with(bookmark_model_with_uuid)
    @bookmarks_namespace.expect(bookmark_model_base)
    @api.doc(security='apiKey')
    @token_required
    def patch(self, uuid):
        """edit bookmark by uuid"""
        data = request.json
        bookmark = db.session.query(BookmarkModel).filter_by(bookmark_uuid=uuid).first()
        if not bookmark:
            raise NotFound('Bookmark not found')
        bookmark.update(**data)
        db.session.commit()
        return bookmark

    @bookmarks_namespace.marshal_with(bookmark_model_with_uuid)
    @api.doc(security='apiKey')
    @token_required
    def delete(self, uuid):
        """delete bookmark by uuid"""
        bookmark = db.session.query(BookmarkModel).filter_by(bookmark_uuid=uuid).first()
        if not bookmark:
            raise NotFound('Bookmark not found')
        db.session.delete(bookmark)
        db.session.commit()
        return bookmark
