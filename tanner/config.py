import logging
import os
import sys

import yaml

LOGGER = logging.getLogger(__name__)


class TannerConfig:
    config = None

    @staticmethod
    def _environment_value(section, value):
        environment_names = (
            "TANNER__{}__{}".format(section, value),
            "TANNER_{}_{}".format(section, value),
        )
        environment = {name.upper(): data for name, data in os.environ.items()}
        for name in environment_names:
            if name.upper() in environment:
                return True, yaml.safe_load(environment[name.upper()])
        return False, None

    @staticmethod
    def _apply_environment(config_values):
        for section, values in config_values.items():
            if not isinstance(values, dict):
                continue
            for value in values:
                is_set, environment_value = TannerConfig._environment_value(section, value)
                if is_set:
                    values[value] = environment_value
        return config_values

    @staticmethod
    def read_config(path):
        config_values = {}
        try:
            with open(path, "r") as f:
                config_values = yaml.load(f, Loader=yaml.FullLoader)
        except yaml.parser.ParserError as e:
            print("Couldn't properly parse the config file. Please use properly formatted YAML config.")
            sys.exit(1)
        return TannerConfig._apply_environment(config_values)

    @staticmethod
    def set_config(config_path):
        if not os.path.exists(config_path):
            print("Config file {} doesn't exist. Check the config path or use default".format(config_path))
            sys.exit(1)

        TannerConfig.config = TannerConfig.read_config(config_path)

    @staticmethod
    def get(section, value):
        try:
            res = TannerConfig.config[section][value]
        except (KeyError, TypeError):
            res = DEFAULT_CONFIG[section][value]

        return res


DEFAULT_CONFIG = TannerConfig.read_config("/opt/tanner/data/config.yaml")
