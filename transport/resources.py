"""
A module containing resources for handling app's requests.
"""
import content_types

from falcon import Request, Response, HTTP_200
from datetime import datetime
from config.config import Config
from service.event_service import EventService

from .templates import get_template
from .responses import EventResponseInfo


class HealthResource:
    async def on_get(self, req: Request, resp: Response) -> None:
        resp.text = "healthy"
        resp.content_type = content_types.TEXT
        resp.status = HTTP_200


class IndexResource:
    async def on_get(self, req: Request, resp: Response) -> None:
        resp.status = HTTP_200
        resp.content_type = content_types.HTML
        # TODO: switch to async Jinja templating
        resp.text = get_template("index.html").render(current_time=datetime.now())


class EventsResource:
    def __init__(self, cfg: Config) -> None:
        self._event_service = EventService(cfg.db_conn_str)

    async def on_get(self, req: Request, resp: Response) -> None:
        response: list[EventResponseInfo] = []
        response.append(EventResponseInfo.from_service_model())

        resp.status = HTTP_200
        resp.media = {}

    async def on_post(self, req: Request, resp: Response):
        obj: any = await req.get_media()
        resp.status = HTTP_200
