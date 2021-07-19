from flask_restx import Resource

from app import api

auth_namespace = api.add_namespace('authentication')


@auth_namespace.route('/auth/token')
class AuthToken(Resource):
    def get(self):
        ...
