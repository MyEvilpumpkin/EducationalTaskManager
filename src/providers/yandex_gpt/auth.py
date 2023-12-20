"""
Module that contains code for YandexGPT authentication
"""

import requests                # Required for authentication requests
from datetime import datetime  # Required to track IAM-token expiration time
from enum import StrEnum       # Required to define options for authentication method

from configuration.secrets import get_secret    # Required to get secrets
from configuration.settings import get_setting  # Required to get settings

from .dto import OAuthToken, IAMToken  # Required for working with data transfer objects


class AuthMethod(StrEnum):
    """
    Authentication methods
    """

    BEARER = 'BEARER'    # Authentication with OAuth-token (user and service account)
    API_KEY = 'API_KEY'  # Authentication with API-key (only service account)


class Bearer:
    """
    Bearer authentication data
    """

    token: str            # IAM-token
    expires_at: datetime  # IAM-token expiration time

    def __init__(self, iam_token_: IAMToken):
        self.token = iam_token_.iamToken
        self.expires_at = datetime.strptime(iam_token_.expiresAt[:19], '%Y-%m-%dT%H:%M:%S')


auth_url = get_setting('GPT_AUTH_URL')
auth_method = get_setting('GPT_AUTH_METHOD')
oauth_token = get_secret('GPT_OAUTH_TOKEN')
api_key = get_secret('GPT_API_KEY')

bearer_auth_data = None


def get_auth_data() -> str:
    """
    Get authentication data
    :return: authentication data
    """

    if auth_method == AuthMethod.BEARER:
        return _get_bearer()
    if auth_method == AuthMethod.API_KEY:
        return _get_api_key()


def _get_bearer() -> str:
    """
    Get authentication data for bearer method
    :return: authentication data
    """

    global bearer_auth_data

    if bearer_auth_data is None or bearer_auth_data.expires_at < datetime.now():
        # Updating bearer method authentication data
        bearer_auth_data = _get_new_bearer()

    return f'Bearer {bearer_auth_data.token}'


def _get_new_bearer() -> Bearer:
    """
    Exchange OAuth-token to IAM-token
    :return: bearer method authentication data
    """

    request = OAuthToken.token(oauth_token)

    response = requests.post(
        auth_url,
        json=request.model_dump()
    )

    iam_token = IAMToken.model_validate_json(response.text)

    return Bearer(iam_token)


def _get_api_key() -> str:
    """
    Get authentication data for API-key method
    :return: authentication data
    """

    return f'Api-Key {api_key}'
