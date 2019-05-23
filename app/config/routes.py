from app.views import Nodes, Trees, ChildTrees, PathTrees, MoveNode


def map_routes(app):

    app.router.add_route('*', '/nodes', Nodes)
    app.router.add_route('POST', '/nodes/move', MoveNode)
    app.router.add_route('GET', '/trees/{_id}', Trees)
    app.router.add_route('GET', '/trees/{_id}/child', ChildTrees)
    app.router.add_route('GET', '/trees/{_id}/path', PathTrees)