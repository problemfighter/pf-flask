import os
from flask import render_template
from pf_sqlalchemy.db.orm import database
from pfms.common.pfms_exception import PfMsException
from pfms.flask_pf_marshmallow_swagger import PFMarshmallowSwagger
from pf_flask.pfrf_app_config import PFRFAppConfigInterface
from pf_flask.pfrf_utils import import_from_string, is_url_register

env = os.environ.get('env')


class Bootstrap:

    def _get_app_environment(self):
        if env:
            return env
        return "local"

    def _get_app_config(self) -> PFRFAppConfigInterface:
        app_config = import_from_string("application.app_config.AppConfig", False)
        if app_config:
            if not issubclass(app_config, PFRFAppConfigInterface):
                raise PfMsException("AppConfig Should be Implementation of PFRFAppConfigInterface")
            return app_config()
        return PFRFAppConfigInterface()

    def _register_environment(self, flask_app, app_config: PFRFAppConfigInterface):
        environment = app_config.register_env_config(self._get_app_environment(), flask_app)
        environment_class = "pfrf.pfrf_base_env_config.PFRFBaseEnvConfiguration"
        if environment and isinstance(environment, str):
            environment_class = environment
        flask_app.config.from_object(environment_class)

    def _init_database(self, flask_app):
        database.init_app(flask_app)

    def _app_bismillah(self, flask_app):
        app_config = self._get_app_config()
        self._register_environment(flask_app, app_config)
        self._init_database(flask_app)
        with flask_app.app_context():
            app_config.register_model(flask_app)
        app_config.register_controller(flask_app)

    def _init_pf_marshmallow_swagger(self, flask_app):
        PFMarshmallowSwagger(flask_app)

    def _default_home(self):
        return render_template('bismillah.html')

    def _register_root_url(self, flask_app):
        is_slash_registered = is_url_register(flask_app, "/")
        if not is_slash_registered:
            flask_app.add_url_rule("/", view_func=self._default_home)

    def load_app(self, flask_app):
        self._app_bismillah(flask_app)
        self._init_pf_marshmallow_swagger(flask_app)
        self._register_root_url(flask_app)


