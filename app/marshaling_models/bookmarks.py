from flask_restx import fields

from app import api
from app.marshaling_models.helpers import StringUUID


bookmark_model = api.model('Model', {
    'bookmark_uuid': StringUUID,
    'link': fields.String,
    'comment': fields.String,
    'group': fields.String
})
