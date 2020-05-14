import aiohttp_jinja2
import jinja2
from aiohttp import web

import settings
from storage import MockStorage

routes = web.RouteTableDef()
storage = MockStorage()


@routes.get("/users/{user_name:[a-zA-Z0-9-_.]+}/comments")
@aiohttp_jinja2.template('index.html')
async def comments(request):
    user_name = request.match_info["user_name"]
    offset = int(request.rel_url.query.get("offset", 0))
    limit = int(request.rel_url.query.get("limit", settings.maximum_number_of_items_per_page))

    return {
        "comments": await storage.get_comments_for_user_by_name(user_name, offset, limit),
    }


def main():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader("templates"),
    )

    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
