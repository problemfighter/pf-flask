import os
from pf_flask.bismillah import Bismillah
from pf_flask.pff_app_config import PFFAppConfig


base_path = os.path.abspath(os.path.dirname(__file__))
config = PFFAppConfig()
config.set_base_dir(base_path)
bismillah = Bismillah(__name__, config)


if __name__ == '__main__':
    bismillah.run()
