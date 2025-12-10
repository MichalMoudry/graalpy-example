"""
A module for an EventService class.
"""
from db.open import open

from .model import EventInfo


class EventService:
    """
    A service class responsible for handling logic related to events.
    """
    def __init__(self, db_conn_str: str) -> None:
        self._conn_str = db_conn_str

    def retrieve_events(self, limit: int = 100) -> list[EventInfo]:
        """
        A method for retrieval of currently available events.
        """
        result: list[EventInfo] = []

        with open(self._conn_str) as conn:
            cursor = conn.cursor()
            res = cursor.execute("")
            events = res.fetchall()
            if events:
                for ev in events:
                    result.append(EventInfo(ev[0], ev[1], ev[2]))

        return result

    def add_event(self, data: str):
        """
        A method for adding a new event.
        """
        with open(self._conn_str) as conn:
            conn.commit()
