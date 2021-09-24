import os

from application.config.dev_config import DevConfiguration
from application.config.local_config import LocalConfiguration
from application.config.prod_config import ProdConfiguration
from application.config.stage_config import StageConfiguration

env = os.environ.get('env')


def get_config():
    if env and str(env) == 'prod':
        return ProdConfiguration()
    elif env and str(env) == 'stage':
        return StageConfiguration()
    elif env and str(env) == 'dev':
        return DevConfiguration()
    else:
        return LocalConfiguration()
