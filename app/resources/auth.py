from base64 import b64decode

from flask import request
from flask_restx import Resource
from werkzeug.exceptions import Unauthorized

from app import api
from app.helpers.auth import generate_token, check_user

auth_namespace = api.namespace('auth', description='Authorization')


@auth_namespace.route('')
class AuthToken(Resource):
    @api.doc(security='basic')
    def get(self):
        """Provide login and password using basicAuth to get token"""
        credentials = request.headers.get('Authorization')
        if not credentials:
            raise Unauthorized('Login required')
        auth_type, data = credentials.split(' ')
        if auth_type != 'Basic':
            raise Unauthorized()
        username, password = b64decode(data).decode().split(':', 1)
        user_uuid = check_user(username, password)
        if not user_uuid:
            raise Unauthorized('Invalid login or password')

        return generate_token(user_uuid)
