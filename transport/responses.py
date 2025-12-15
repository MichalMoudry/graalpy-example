"""
A module with all the contract classes.
"""
from dataclasses import dataclass
from datetime import datetime

from service.model import EventInfo


@dataclass(frozen = True)
class EventResponseInfo:
    """
    A class representing a part of a response with information about a single
    event.
    """
    id: int
    data: str
    created: datetime
    updated: datetime

    @classmethod
    def from_service_model(cls: callable, model: EventInfo) -> EventResponseInfo:
        """
        A method for initialization from 
        """
        return cls()
