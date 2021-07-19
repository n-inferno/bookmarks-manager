from datetime import datetime
from uuid import uuid4


class Bookmark:
    def __init__(self, user_id, link, comment=None, group=None):
        self.bookmark_uuid = uuid4()
        self.user_id = user_id
        self.link = link
        self.comment = comment
        self.datetime_added = datetime.utcnow()
        self.group = group