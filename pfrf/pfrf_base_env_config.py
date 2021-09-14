import os


class PFRFBaseEnvConfiguration(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SECRET_KEY = 'random_secret_key_base'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ''
