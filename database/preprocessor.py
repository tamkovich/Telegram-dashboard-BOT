from private.parse import parse_yaml, parse_json

import sqlalchemy as sa


CONFIG = {
    'dir': 'database',
    'filename': 'config.yaml',
    'type': 'yaml'
}


def load_engine(echo: bool=False):
    """
    create database engine from config-file params
    :param echo: bool flag. param for sqlalchemy.create_engine func.
    :return: [sqlalchemy] engine
    """
    config = dict()
    if CONFIG['type'] == 'json':
        config = parse_json(CONFIG['dir'], CONFIG['filename'])
    elif CONFIG['type'] == 'yaml':
        config = parse_yaml(CONFIG['dir'], CONFIG['filename'])
    else:
        pass
    database = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(
        config['user'], config['password'], config['host'], config['database']
    )
    return sa.create_engine(database, echo=echo)
