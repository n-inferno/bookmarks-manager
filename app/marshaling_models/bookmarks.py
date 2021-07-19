from flask_restx import fields

from app import api
from app.marshaling_models.helpers import StringUUID


bookmark_model_base = api.model('BookmarkModelBase', {
    'link': fields.String(description='Link you want to save'),
    'comment': fields.String(description='Add a comment if necessary'),
    'link_group': fields.String(description='Add link to group in necessary'),
})

bookmark_model_with_uuid = api.inherit("BookmarkModelWithUUID",
                                       bookmark_model_base, {
    'bookmark_uuid': StringUUID(description='Bookmark uuid'),
})
