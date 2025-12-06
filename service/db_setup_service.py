"""
A module for a DbSetupService class.
"""
from config.config import Config
from db.open import open


def run_db_setup(cfg: Config) -> None:
    conn = open(cfg.db_conn_str)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS test_table(id, data, date_created, date_updated)"
    )

    conn.commit()
    conn.close()
