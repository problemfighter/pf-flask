from application.config.base_config import BaseConfiguration


class LocalConfiguration(BaseConfiguration):
    SQLALCHEMY_ECHO = False

