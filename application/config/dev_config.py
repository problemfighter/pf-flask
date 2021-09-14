from application.config.base_config import BaseConfiguration


class DevConfiguration(BaseConfiguration):
    SQLALCHEMY_ECHO = False

