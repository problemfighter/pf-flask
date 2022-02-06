import os
from typing import get_type_hints, Union

from dotenv import dotenv_values
from pf_flask.pff_app_config import PFFAppConfig
from pf_flask.pff_utils import concat_path, is_exists_path


class PFFConfigManager:

    def merge_config(self, config: PFFAppConfig):
        env_config = self._get_env_values(config)
        if env_config:
            config = self._convert_and_merge(env_config, config)
        return config

    def _get_env_values(self, config: PFFAppConfig):
        env_file_name = self._get_app_environment()
        env_file = concat_path(config.APP_CONFIG_PATH, env_file_name)
        env_config = None
        if is_exists_path(env_file):
            env_config = dotenv_values(env_file)
        return env_config

    def _get_app_environment(self):
        env = os.environ.get('env')
        if env:
            return ".env-" + env
        return ".env"

    def convert_config_to_map(self, config: PFFAppConfig):
        config_map = {}
        for key in dir(config):
            if key.isupper():
                config_map[key] = getattr(config, key)
        return config_map

    def merge_config_by_config(self, source: PFFAppConfig, destination: PFFAppConfig):
        config_map = self.convert_config_to_map(source)
        return self._convert_and_merge(config_map, destination)

    def _convert_and_merge(self, env_config, config: PFFAppConfig):
        config_map = dir(config)
        for key in config_map:
            if key.isupper():
                if key in env_config:
                    try:
                        var_type = get_type_hints(type(config))[key]
                        override_data = env_config.get(key)
                        if var_type == bool:
                            env_config_value = self._parse_bool(override_data)
                        elif var_type == list:
                            if isinstance(override_data, list):
                                env_config_value = override_data
                            else:
                                env_config_value = self._parse_list(override_data)
                        else:
                            env_config_value = var_type(override_data)
                        if env_config_value or (var_type == bool and not env_config_value):
                            setattr(config, key, env_config_value)
                    except:
                        pass
        return config

    def _parse_bool(sele, override_data: str) -> bool:
        return override_data if type(override_data) == bool else override_data.lower() in ['true', 'yes', '1']

    def _parse_list(self, override_data: str):
        if override_data and isinstance(override_data, str):
            return override_data.split(",")
        return None
