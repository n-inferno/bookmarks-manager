from flask_restx import Resource, reqparse

from app import api
from app.helpers.auth import generate_token

auth_namespace = api.namespace('auth', description='Authorisation')

user_parser = reqparse.RequestParser()
user_parser.add_argument('login', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)


@auth_namespace.route('')
class AuthToken(Resource):
    @api.expect(user_parser)
    def get(self):
        return generate_token("bd6fc9b4-2a86-4ff0-a93d-d0b011fa41bc")
