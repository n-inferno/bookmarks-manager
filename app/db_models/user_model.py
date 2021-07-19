from app import db


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    @classmethod
    def get_user(cls, login):
        return cls.query.filter_by(login=login).first()
