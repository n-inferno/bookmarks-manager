from flask_restx import Resource

from app import api


@api.route('/smoke')
class Smoke(Resource):
    """smoke test for app"""
    def get(self):
        return {'smoke-test': 'ok'}
