from flask import Flask
from flask_cors import CORS

from pf_flask.global_registry import init_global_config
from pf_flask.pff_app_config import PFFAppConfig
from pf_flask.pff_bootstrap import PFFBootstrap
from pf_flask.pff_config_manager import PFFConfigManager


class Bismillah(object):
    _flask_app = None
    _config: PFFAppConfig = None
    _config_manager = PFFConfigManager()
    _bootstrap = PFFBootstrap()

    def __init__(self, name, config=PFFAppConfig()):
        self._flask_app = Flask(name)
        self._config = self._config_manager.merge_config(config)
        init_global_config(self._config)
        self._register_app_config()
        self._bootstrap.initialize_app(self._flask_app, self._config)
        self._init_cors()

    def run(self):
        self._flask_app.run(host=self._config.HOST, port=self._config.PORT)

    def add_before_request_fun(self, function):
        self._flask_app.before_request_funcs.setdefault(None, []).append(function)

    def get_flask_app(self):
        return self._flask_app

    def _register_app_config(self):
        self._flask_app.config.from_object(self._config)

    def _init_cors(self):
        CORS(self._flask_app, resources={
            r"/api/*": {"origins": self._config.ALLOW_CORS_ORIGINS, "Access-Control-Allow-Origin": self._config.ALLOW_ACCESS_CONTROL_ORIGIN},
            r"/static/*": {"origins": self._config.ALLOW_CORS_ORIGINS, "Access-Control-Allow-Origin": self._config.ALLOW_ACCESS_CONTROL_ORIGIN}
        })

