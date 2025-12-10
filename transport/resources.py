"""
A module containing resources for handling app's requests.
"""
import content_types

from falcon import Request, Response
from datetime import datetime

from .templates import get_template


class HealthResource:
    async def on_get(self, req: Request, resp: Response) -> None:
        resp.text = "healthy"
        resp.content_type = content_types.TEXT
        resp.status = 200


class IndexResource:
    async def on_get(self, req: Request, resp: Response) -> None:
        resp.status = 200
        resp.content_type = content_types.HTML
        # TODO: switch to async Jinja templating
        resp.text = get_template("index.html").render(current_time=datetime.now())


class EventsResource:
    async def on_get(self, req: Request, resp: Response) -> None:
        resp.status = 200
        resp.media = {}
