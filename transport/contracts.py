"""
A module with all the contract classes.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EventResponseInfo:
    id: int
    data: str
    created: datetime
    updated: datetime
