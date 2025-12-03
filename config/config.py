from dataclasses import dataclass
from tomllib import load


@dataclass
class Config:
    """
    A class containing app's configuration information.
    """
    should_run_db_setup: bool


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
        with_db_setup_val = data.get("with_db_setup")
        if with_db_setup_val and isinstance(with_db_setup_val, bool):
            with_db_setup = with_db_setup_val

    return Config(with_db_setup)
