"""
Settings provider
"""

import json  # Required for parsing the settings file


settings_file_path = 'settings.json'
settings_file_cache = None


def get_setting(name: str) -> str:
    """
    Getting a setting by name
    :param name: setting name
    :return: setting
    """

    global settings_file_cache

    if settings_file_cache is None:
        # Caching settings
        with open(settings_file_path, 'r') as file:
            settings_file_cache = json.load(file)

    return settings_file_cache.get(name)
