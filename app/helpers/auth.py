import os
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, g
from jwt import ExpiredSignatureError
from werkzeug.exceptions import Unauthorized, Forbidden
from werkzeug.security import check_password_hash

from app.db_models.user_model import UserModel


def check_user(username, password):
    user = UserModel.get_user(login=username)
    if not user or not check_password_hash(user.password_hash, password):
        return False
    return user.user_uuid


def generate_token(user_uuid):
    now = datetime.utcnow()
    token_data = {
        'iat': now,
        'exp': now + timedelta(seconds=600),
        'uuid': user_uuid
    }
    token = jwt.encode(token_data, os.environ.get('AUTH_STRING'), algorithm="HS256")

    return {'token': token, 'duration': 600}


def verify_token(token):
    if not token:
        raise Unauthorized()
    try:
        token_data = jwt.decode(token, os.environ.get('AUTH_STRING'), algorithms=["HS256"])
    except ExpiredSignatureError:
        raise Forbidden()
    user = UserModel.get_user(user_uuid=token_data.get('uuid'))
    if not user:
        raise Unauthorized()

    g.user_uuid = user.user_uuid
    g.user_login = user.login
    g.user_id = user.user_id

    return True


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("X-API")
        if not token:
            raise Unauthorized('Token required')
        if verify_token(token=token):
            return f(*args, **kwargs)
        raise Unauthorized()
    return decorated
