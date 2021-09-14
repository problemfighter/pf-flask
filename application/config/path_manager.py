import os

from pf_file_dir.pf_fd_util import join_path
from application.config.config_helper import get_config


def upload_path():
    config_helper = get_config()
    return join_path(config_helper.BASE_STATIC, "uploads")


def upload_path_concat(extension):
    return os.path.join(upload_path(), extension)
