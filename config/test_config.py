from config import config


def test_read_config():
    """
    A simple test that validates if the configuration file is correctly loaded.
    """
    cfg = config.read("./config.toml")
    assert cfg != None
    assert cfg.should_run_db_setup == True
    assert cfg.db_conn_str != None or cfg.db_conn_str != ""
