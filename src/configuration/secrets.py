"""
Secrets provider
"""

import json               # Required for parsing the secrets file
import os                 # Required to obtain secrets from environment variables
from enum import StrEnum  # Required to define options for secret storage locations

from .settings import get_setting  # Required to obtain from the settings where secrets are stored


class SecretsLocation(StrEnum):
    """
    Secrets location variants
    """

    ENV = 'ENV'    # Environment variables
    FILE = 'FILE'  # Secrets file


secrets_location = get_setting('SECRETS_LOCATION')
secrets_file_path = get_setting('SECRETS_FILE_PATH')
secrets_file_cache = None


def get_secret(name: str) -> str:
    """
    Getting a secret by name
    :param name: secret name
    :return: secret
    """

    if secrets_location == SecretsLocation.ENV:
        return _get_secret_from_env(name)
    if secrets_location == SecretsLocation.FILE:
        return _get_secret_from_file(name)


def _get_secret_from_env(name: str) -> str:
    """
    Getting a secret by name from environment variables
    :param name: secret name
    :return: secret
    """

    return os.environ.get(name)


def _get_secret_from_file(name: str) -> str:
    """
    Getting a secret by name from secrets file
    :param name: secret name
    :return: secret
    """

    global secrets_file_cache

    if secrets_file_cache is None:
        # Caching secrets
        with open(secrets_file_path, 'r') as file:
            secrets_file_cache = json.load(file)

    return secrets_file_cache.get(name)
