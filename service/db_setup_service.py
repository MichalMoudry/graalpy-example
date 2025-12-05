"""
A module for a DbSetupService class.
"""
from config.config import Config
from db.open import open


def run_db_setup(cfg: Config) -> None:
    with open(cfg.db_conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE test_table(id, data, date_created, date_updated)")
        conn.commit()
