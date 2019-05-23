from schemer import Schema
from schemer.validators import is_objectid

node_schema = Schema({
    'text': {'type': str, 'required': True},
    '_id': {'type': str, 'validates': is_objectid()}
})

id_schema = Schema({
    '_id': {'type': str, 'required': True, 'validates': is_objectid()}
})

token_schema = Schema({
    'token': {'type': str, 'required': True}
})

move_schema = Schema({
    'new_root_id': {'type': str, 'required': True},
    '_id': {'type': str, 'validates': is_objectid()}
})