"""
A module for handling opening DB connection, or initialization of a DB.
"""
from sqlite3 import connect, Connection


def open(connection_str: str) -> Connection:
    return connect(connection_str)
