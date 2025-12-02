from dataclasses import dataclass

@dataclass
class Config:
    should_run_db_setup: bool


def read() -> Config:
    ...
