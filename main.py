"""Main script."""
from os import environ

import argparse
# import asyncio
# import uvloop
from aiohttp import web

# from app.config.settings import basepath
from app.config.application import app_config
# from app.middlewares import MIDDLEWARES


def main():
    """Start app."""
    parser = argparse.ArgumentParser(description='Run application.')

    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='application port.'
    )

    parser.add_argument(
        '--host',
        type=str,
        default='127.0.0.1',
        help='application host.'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
    )

    args = parser.parse_args()

    app = web.Application(
        debug=args.debug,
        # middlewares=MIDDLEWARES
    )
    app_config(app)
    web.run_app(
        app,
        host=args.host,
        port=args.port,
        access_log=None
    )


if __name__ == '__main__':
    main()
