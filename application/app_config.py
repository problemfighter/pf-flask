from pfrf.pfrf_app_config import PFRFAppConfigInterface


class AppConfig(PFRFAppConfigInterface):

    def register_controller(self, flask_app):
        pass

    def register_model(self, flask_app):
        pass

    def register_env_config(self, env, flask_app) -> str:
        if env and str(env) == 'prod':
            return 'application.config.prod_config.ProdConfiguration'
        else:
            return 'application.config.dev_config.DevConfiguration'
