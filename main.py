from datetime import datetime
from flask import Flask, render_template
from config import config


cfg = config.read()
app = Flask(__name__)

@app.route("/")
def index() -> str:
    return render_template(
        "index.html",
        current_time=datetime.now().isoformat()
    )


@app.route("/health")
def health() -> str:
    return "healthy"
