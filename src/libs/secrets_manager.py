import json
import os
from enum import StrEnum

from .settings_manager import get_setting


class SecretsLocation(StrEnum):
    ENV = 'ENV'
    FILE = 'FILE'


secrets_location = get_setting('SECRETS_LOCATION')
secrets_file_path = get_setting('SECRETS_FILE_PATH')
secrets = None


def get_secret(name: str) -> str:
    if secrets_location == SecretsLocation.ENV:
        return get_secret_from_env(name)
    if secrets_location == SecretsLocation.FILE:
        return get_secret_from_file(name)


def get_secret_from_env(name: str) -> str:
    return os.environ.get(name)


def get_secret_from_file(name: str) -> str:
    global secrets
    if secrets is None:
        with open(secrets_file_path, 'r') as file:
            secrets = json.load(file)

    return secrets.get(name)
