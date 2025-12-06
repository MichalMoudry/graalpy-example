from datetime import datetime
from flask import Flask, render_template
from config import config
from service.db_setup_service import run_db_setup


cfg = config.read("config.toml")
if cfg.should_run_db_setup:
    run_db_setup(cfg)

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return render_template(
        "index.html",
        current_time=datetime.now()
    )


@app.route("/health")
def health() -> str:
    return "healthy"
