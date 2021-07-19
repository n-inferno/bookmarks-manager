from flask_restx.fields import String


class StringUUID(String):
    __schema_type__ = 'string'
    __schema_format__ = 'string_uuid'
    __schema_example__ = 'uuid4'
