import json
from aiohttp import web
from schemer.exceptions import ValidationException

from app.models import NodeManager
from app.utils import node_schema, id_schema, move_schema


class BaseView(web.View):
    @property
    def app(self):
        return self.request.app

    @property
    def database(self):
        return self.app["database"]

    @property
    async def headers(self):
        return self.request.headers

    @property
    def node_manager(self):
        node_manager = NodeManager(self.database)
        return node_manager

    @staticmethod
    def json_response(*args, **kwargs):
        return web.json_response(*args, **kwargs)

    async def get_data_body(self, schema, status_code):
        try:
            data = await self.request.json()
            schema.validate(data)
        except ValidationException as e:
            return 400, e.errors
        return status_code, data

    async def get_data_path(self, schema, status_code):
        try:
            _id = self.request.match_info.get('_id', None)
            schema.validate({'_id': _id})
        except ValidationException as e:
            return 400, e.errors
        return status_code, _id


class Nodes(BaseView):

    async def post(self):
        status = 'failed'
        status_code, result = await self.get_data_body(node_schema, 201)
        if status_code is 201:
            result = await self.node_manager.tree_add_node(root_id=result.get('_id', None),
                                                           text=result.get('text'))
            status = 'success'

        return self.json_response({
            'status': status,
            'message': result
        },
            status=status_code)

    async def delete(self):
        status = 'failed'
        status_code, result = await self.get_data_body(id_schema, 200)
        if status_code is 200:
            result = await self.node_manager.remove_node(_id=result.get('_id'))
            status = 'success'

        return self.json_response({
            'status': status,
            'message': result
        },
            status=status_code)


class MoveNode(BaseView):

    async def post(self):
        status = 'failed'
        status_code, result = await self.get_data_body(move_schema, 200)
        if status_code is 200:
            result = await self.node_manager.move_node(_id=result.get('_id'),
                                                       new_root_id=result.get('new_root_id'))
            status = 'success'

        return self.json_response({
            'status': status,
            'message': result
        },
            status=status_code)


class PathTrees(BaseView):

    async def post(self):
        status = 'failed'
        status_code, result = await self.get_data_path(id_schema, 200)
        if status_code is 200:
            result = await self.node_manager.get_tree_path(_id=result)
            status = 'success'

        return self.json_response({
            'status': status,
            'message': result
        },
            status=status_code)


class ChildTrees(BaseView):

    async def post(self):
        status = 'failed'
        status_code, result = await self.get_data_path(id_schema, 200)
        if status_code is 200:
            result = await self.node_manager.get_tree_child(_id=result)
            status = 'success'

        return self.json_response({
            'status': status,
            'message': result
        },
            status=status_code)


class Trees(BaseView):

    async def get(self):
        status = 'failed'
        status_code, result = await self.get_data_path(id_schema, 200)
        if status_code is 200:
            result = await self.node_manager.get_tree(_id=result)
            status = 'success'

        return self.json_response({
            'status': status,
            'message': result
        },
            status=status_code)