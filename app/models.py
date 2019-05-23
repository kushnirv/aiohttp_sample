from bson import ObjectId


class NodeManager(object):

    def __init__(self, db):
        self.collection = db.trees

    async def tree_add_node(self, text, root_id=None):
        """ Дбавление вершины
        """
        print(text, root_id)
        if not root_id:
            new_obj = await self.collection.insert_one({'text': text,
                                                        'ancestors': [],
                                                        'parent': None})
            return str(new_obj.inserted_id)

        obj = await self.collection.find_one({'_id': ObjectId(root_id)})
        ancestors = obj.get('ancestors')
        ancestors.append(root_id)
        new_obj = await self.collection.insert_one({'text': text,
                                                    'ancestors': ancestors,
                                                    'parent': root_id})
        return str(new_obj.inserted_id)

    async def get_tree_child(self, _id):
        """ Получение детей
            Args:
                _id(str): id вершины, чьих детей нужно получить
        """
        cursor = self.collection.find({'parent': _id})
        childs_id = []
        async for document in cursor:
            childs_id.append(str(document.get('_id')))
        return childs_id

    async def get_tree(self, _id):
        """ Получение поддерева
            Args:
                _id(str): id вершины, поддерево для которой нужно получить
        """
        cursor = self.collection.find({'ancestors': {'$elemMatch': {'$eq': _id}}})
        trees_id = []
        async for document in cursor:
            trees_id.append(str(document.get('_id')))
        return trees_id

    async def get_tree_path(self, _id):
        """ Получение пути до вершины
            Args:
                _id(str): id вершины, до которой нужно получить путь
        """
        obj = self.collection.find_one({'_id': ObjectId(_id)})
        ancestors = obj.get('ancestors')
        return ancestors

    async def move_node(self, new_root_id, _id):
        """ Перемещение вершины
            Args:
                _id(str): id переносимой вершины
                new_root_id(str): id нового родителя
        """
        obj = await self.collection.find_one({'_id': ObjectId(new_root_id)})
        ancestors = obj.get('ancestors')
        ancestors.append(new_root_id)

        upd_obj = await self.collection.update_one({'_id': ObjectId(_id)}, {'$set': {
            'parent': new_root_id,
            'ancestors': ancestors}
        })
        return upd_obj.modified_count

    async def remove_node(self, _id):
        """ Удаление вершины
            Args:
                _id(str): id удаляемой вершины
        """
        del_obj_many = await self.collection.delete_many({'ancestors': {'$elemMatch': {'$eq': _id}}})
        del_obj_one = await self.collection.delete_one({'_id': ObjectId(_id)})
        return del_obj_many.deleted_count + del_obj_one.deleted_count
