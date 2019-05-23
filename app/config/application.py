from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import SETTINGS
from app.config.routes import map_routes
from aiohttp_swagger import setup_swagger


async def startup(app):
    """Startup app."""
    # MONGO
    app.mongo_client = AsyncIOMotorClient(
        SETTINGS['mongo']['uri'],
        io_loop=app.loop,
        serverSelectionTimeoutMS=3000
    )
    app['database'] = app.mongo_client[SETTINGS['mongo']['db']]


async def cleanup(app):
    """Cleanup app."""
    # MONGO
    app.mongo_client.close()


def app_config(app):
    """Add app configs."""
    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)
    map_routes(app)
    setup_swagger(app, swagger_from_file="app/config/swagger.yaml")
    return app