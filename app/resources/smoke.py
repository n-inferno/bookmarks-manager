from flask_restx import Resource

from app import api
from app.helpers.auth import token_required

smoke_namespace = api.namespace('smoke', description='Smoke test')


@smoke_namespace.route('')
class Smoke(Resource):
    """smoke test for app"""
    @api.doc(security='apiKey')
    @token_required
    def get(self):
        return {'smoke-test': 'ok'}
