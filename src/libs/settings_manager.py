import json


settings_file_path = 'settings.json'
settings = None


def get_setting(name: str) -> str:
    global settings
    if settings is None:
        with open(settings_file_path, 'r') as file:
            settings = json.load(file)

    return settings.get(name)
