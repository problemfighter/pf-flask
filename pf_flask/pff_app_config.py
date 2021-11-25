import os


class PFFAppConfig(object):
    BASE_DIR: str = None
    APP_CONFIG_PATH: str = None
    DEBUG: bool = True
    STRING_IMPORT_SILENT: bool = True
    SECRET_KEY: str = 'random_secret_key_base'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: str = None
    SWAGGER_ENABLE: bool = True
    DEFAULT_URL: str = '/'
    DEFAULT_HTML: str = 'bismillah.html'
    ALLOW_CORS_ORIGINS: list = ["*"]
    ALLOW_ACCESS_CONTROL_ORIGIN: str = "*"
    PORT: int = 1200
    HOST: str = "127.0.0.1"
    MODULE_REGISTRY_PACKAGE: list = ["application.registry.Register"]

    def set_base_dir(self, path):
        if not self.BASE_DIR:
            self.BASE_DIR = path
            self.APP_CONFIG_PATH = path
            if not self.SQLALCHEMY_DATABASE_URI:
                self.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(self.BASE_DIR, 'pf-flask.sqlite3')
        return self
