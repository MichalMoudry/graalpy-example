"""
A module with model class for the service layer.
"""
from datetime import datetime


class EventInfo:
    def __init__(self, id: int, data: str, created: datetime) -> None:
        ...
