from datetime import datetime
from uuid import uuid4

from app import db


class BookmarkModel(db.Model):
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String, nullable=False)
    comment = db.Column(db.String)
    datetime_added = db.Column(db.String, default=datetime.utcnow().isoformat())
    link_group = db.Column(db.String)
    bookmark_uuid = db.Column(db.String, unique=True, nullable=False, default=uuid4())

    def __init__(self, **kwargs):
        super(BookmarkModel, self).__init__(**kwargs)
        self.bookmark_uuid = kwargs.get('bookmark_uuid') or str(uuid4())

    def update(self, **data):
        for key in data:
            self.__setattr__(key, data[key])
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return

        return self
