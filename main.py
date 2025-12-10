import logging

from config import config
from service.db_setup_service import run_db_setup
from falcon.asgi import App
from transport import resources


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    cfg = config.read("config.toml")
    if cfg.should_run_db_setup:
        run_db_setup(cfg)

    app = App()
    app.add_route("/health", resources.HealthResource())
    app.add_route("/", resources.IndexResource())
    app.add_route("/events", resources.EventsResource())
