# import asyncio
# from motor.motor_asyncio import AsyncIOMotorClient
# from models import TreesManager
#
#
# client = AsyncIOMotorClient('localhost', 27017)
# db = client['test_database']
#
# trees_manager = TreesManager(db)
#
#
# # text_db.create_index([('text', TEXT)], default_language='en', background=True)
#
#
# async def do_insert():
#     t0 = await trees_manager.tree_add_node(text='Educetilonal Literature')
#     t1 = await trees_manager.tree_add_node(text='Natural Lenguages', root_id=t0)
#     t3 = await trees_manager.tree_add_node(text='English', root_id=t1)
#     t4 = await trees_manager.tree_add_node(text='German', root_id=t1)
#     t5 = await trees_manager.tree_add_node(text='Franch', root_id=t1)
#
#     t2 = await trees_manager.tree_add_node(text='Programming', root_id=t0)
#     t8 = await trees_manager.tree_add_node(text='Programming Lenguages', root_id=t2)
#     t9 = await trees_manager.tree_add_node(text='Database', root_id=t2)
#
#     t10 = await trees_manager.tree_add_node(text='SQL', root_id=t9)
#     t11 = await trees_manager.tree_add_node(text='NoSQL', root_id=t9)
#
#     t12 = await trees_manager.tree_add_node(text='mongoDB', root_id=t11)
#
#
# async def get_tree_child():
#     result = await trees_manager.get_tree_child(_id='5ce3e8af9c58ac5c0fded367')
#     print(result)
#
#
# async def get_tree():
#     result = await trees_manager.get_tree(_id='5ce3ef88a2a6e3b9f9e44cad')
#     print(result)
#
#
# async def get_tree_path():
#     result = await trees_manager.get_tree_path(_id='5ce3ef88a2a6e3b9f9e44cb4')
#     print(result)
#
#
# async def move_node():
#     result = await trees_manager.move_node(_id='5ce3ef88a2a6e3b9f9e44cae', new_root_id='5ce3ef88a2a6e3b9f9e44cb4')
#     print(result)
#
#
# async def remove_node():
#     result = await trees_manager.remove_node(_id='5ce3f7785a82d107d703f78e')
#     print(result)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(remove_node())
#
#


def f(x, y={}):
    y[x] = x
    print(y)


f(1)
f(2)
f(3)