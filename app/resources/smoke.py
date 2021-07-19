from flask_restx import Resource

from app import api


smoke_namespace = api.namespace('smoke', description='Smoke test')


@smoke_namespace.route('/smoke')
class Smoke(Resource):
    """smoke test for app"""
    def get(self):
        return {'smoke-test': 'ok'}
