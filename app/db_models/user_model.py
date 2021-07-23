from app import db


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    user_uuid = db.Column(db.String, nullable=False)

    @classmethod
    def get_user(cls, uuid):
        return cls.query.filter_by(user_uuid=uuid).first()
