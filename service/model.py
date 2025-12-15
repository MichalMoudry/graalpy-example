"""
A module with model class for the service layer.
"""
from datetime import datetime


class EventInfo:
    """
    A class that represents an event.
    """
    def __init__(self, id: int, data: str, created: datetime) -> None:
        self._id = id
        self._data = data
        self._created = datetime
