from pf_flask.pfrf_app_config import PFRFAppConfigInterface


class AppConfig(PFRFAppConfigInterface):

    def register_controller(self, flask_app):
        pass

    def register_model(self, flask_app):
        pass

    def register_env_config(self, env, flask_app) -> str:
        if env and str(env) == 'prod':
            return 'application.config.prod_config.ProdConfiguration'
        elif env and str(env) == 'stage':
            return 'application.config.stage_config.StageConfiguration'
        elif env and str(env) == 'dev':
            return 'application.config.dev_config.DevConfiguration'
        else:
            return 'application.config.local_config.LocalConfiguration'
