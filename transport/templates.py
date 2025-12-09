"""
A module for code related to app's HTML templates.
"""
from jinja2 import Environment, FileSystemLoader, Template


_JINIJA2_ENV: Environment = Environment(loader=FileSystemLoader("templates"))

def get_template(name: str) -> Template:
    return _JINIJA2_ENV.get_template(name)
