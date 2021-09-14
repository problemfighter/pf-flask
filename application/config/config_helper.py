import os

from application.config.dev_config import DevConfiguration
from application.config.prod_config import ProdConfiguration

env = os.environ.get('env')


def get_config():
    if env and str(env) == 'prod':
        return ProdConfiguration()
    else:
        return DevConfiguration()
