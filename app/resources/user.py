from flask_restx import Resource

from app import api


@api.route('/users/create')
class Smoke(Resource):
    def get(self):
        return {'smoke-test': 'ok'}
