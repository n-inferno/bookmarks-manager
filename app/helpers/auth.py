import os
from datetime import datetime, timedelta
from functools import wraps
from time import time

import jwt
from flask import request
from jwt import ExpiredSignatureError
from werkzeug.exceptions import Unauthorized, Forbidden
from werkzeug.security import check_password_hash

from app.db_models.user_model import UserModel


def generate_token(user_uuid):
    now = datetime.utcnow()
    token_data = {
        'iat': now,
        'exp': now + timedelta(seconds=600),
        'uuid': user_uuid
    }
    token = jwt.encode(token_data, os.environ.get('AUTH_STRING'), algorithm="HS256")

    return {'token': token}


def verify_token(token):
    if not token:
        return Unauthorized()
    try:
        token_data = jwt.decode(token, os.environ.get('AUTH_STRING'), algorithms=["HS256"])
    except ExpiredSignatureError:
        return Forbidden()
    user = UserModel.get_user(token_data.get('uuid'))
    if not user:
        return Unauthorized()

    return True


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("X-API")
        if verify_token(token=token):
            return f(*args, **kwargs)
        return Unauthorized()
    return decorated
