"""
A module for a DbSetupService class.
"""
from config.config import Config
from db.open import open


def run_db_setup(cfg: Config) -> None:
    conn = open(cfg.db_conn_str)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS events(id, data, date_created)"
    )

    conn.commit()
    conn.close()
