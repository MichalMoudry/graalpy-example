import logging

from config import config
from service.db_setup_service import run_db_setup
from falcon.asgi import App, Request, Response
from transport.templates import get_template
from transport import content_types
from datetime import datetime


logging.basicConfig(level=logging.INFO)

cfg = config.read("config.toml")
if cfg.should_run_db_setup:
    run_db_setup(cfg)


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


app = App()
app.add_route("/health", HealthResource())
app.add_route("/", IndexResource())
