"""
A package for handling database related operations.
"""
from sqlite3 import Connection


def setup_db(conn: Connection):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE ")
    ...
