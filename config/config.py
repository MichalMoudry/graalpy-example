from dataclasses import dataclass
from tomllib import load


@dataclass(frozen = True)
class Config:
    """
    A class containing app's configuration information.
    """
    should_run_db_setup: bool
    db_conn_str: str


def read(file_path: str) -> Config:
    """
    Tries to read a configuration file in a specified location.
    
    :param file_path: The location where the configuration file is located.
    :type file_path: str
    :return: An instance of a Config class.
    :rtype: Config
    """
    with_db_setup = False
    with open(file_path, mode='rb') as file:
        data = load(file)
        db_config: dict[str, str | bool] | None = data.get("database")
        db_conn_str = ""
        if db_config != None:
            with_db_setup_val = db_config.get("with_db_setup")
            if with_db_setup_val != None and isinstance(with_db_setup_val, bool):
                with_db_setup = with_db_setup_val

            db_conn_str = db_config.get("db_conn_str")
            if not isinstance(db_conn_str, str):
                raise ValueError("DB connection string isn't a string")

    return Config(with_db_setup, db_conn_str)
