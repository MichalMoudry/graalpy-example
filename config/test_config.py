from config import config


def test_read_config():
    cfg = config.read("../config.toml")
    assert cfg != None