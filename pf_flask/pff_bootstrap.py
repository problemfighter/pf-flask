from typing import Optional
from flask import render_template
from pf_flask.pff_app_config import PFFAppConfig
from pf_flask.pff_interfaces import PFFRegisterModule
from pf_flask.pff_utils import is_url_register, import_from_string
from pfms.common.pfms_exception import PfMsException
from pfms.flask_pf_marshmallow_swagger import PFMarshmallowSwagger
from pf_sqlalchemy.db.orm import database


class PFFBootstrap:
    _flask_app = None
    _config: PFFAppConfig = None

    def initialize_app(self, flask_app, config: PFFAppConfig):
        self._config = config
        self._flask_app = flask_app
        self._init_pf_marshmallow_swagger(flask_app)
        self._init_database(flask_app)
        self._register_default_url(flask_app)
        self._register_modules()

    def _init_pf_marshmallow_swagger(self, flask_app):
        PFMarshmallowSwagger(flask_app)

    def _init_database(self, flask_app):
        database.init_app(flask_app)

    def _default_home(self):
        return render_template(self._config.DEFAULT_HTML)

    def _register_default_url(self, flask_app):
        is_slash_registered = is_url_register(flask_app, self._config.DEFAULT_URL)
        if not is_slash_registered:
            flask_app.add_url_rule(self._config.DEFAULT_URL, view_func=self._default_home)

    def _get_modules(self, module_registry_package) -> Optional[PFFRegisterModule]:
        app_config = import_from_string(module_registry_package, self._config.STRING_IMPORT_SILENT)
        if app_config:
            if not issubclass(app_config, PFFRegisterModule):
                raise PfMsException("Register Should be Implementation of PFFRegisterModule")
            return app_config()
        return None

    def _register_modules(self):
        module_registry_packages = self._config.MODULE_REGISTRY_PACKAGE
        if module_registry_packages and isinstance(module_registry_packages, list):
            for module_registry_package in module_registry_packages:
                modules = self._get_modules(module_registry_package)
                if modules:
                    with self._flask_app.app_context():
                        modules.register_model_controller(self._flask_app)
                    modules.run_on_start(self._flask_app)
