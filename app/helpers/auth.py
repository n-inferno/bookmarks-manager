import os
from datetime import datetime, timedelta

import jwt
from werkzeug.security import check_password_hash

from app import basic_auth
from app.db_models.user_model import UserModel


def generate_token(user_uuid):
    now = datetime.utcnow()
    token_data = {
        'iat': now,
        'exp': now + timedelta(seconds=600),
        'uuid': user_uuid
    }
    token = jwt.encode(token_data, os.environ.get('AUTH_STRING'), algorithm='HS256').decode('utf-8')

    return token


@basic_auth.verify_password
def verify_password(login, password):
    user = UserModel.get_user(login)
    if not user:
        return False
    if not check_password_hash(user.password_hash, password):
        return False
    return True
