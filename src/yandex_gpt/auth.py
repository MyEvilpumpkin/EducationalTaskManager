import requests
from enum import StrEnum
from datetime import datetime

from .dto import OAuthToken, IAMToken
from src.libs.secrets_manager import get_secret
from src.libs.settings_manager import get_setting


class AuthMethod(StrEnum):
    BEARER = 'BEARER'
    API_KEY = 'API_KEY'


class Bearer:
    token: str
    expires_at: datetime

    def __init__(self, iam_token_: IAMToken):
        self.token = iam_token_.iamToken
        self.expires_at = datetime.strptime(iam_token_.expiresAt[:19], '%Y-%m-%dT%H:%M:%S')


auth_method = get_setting('GPT_AUTH_METHOD')
oauth_token = get_secret('GPT_OAUTH_TOKEN')
api_key = get_secret('GPT_API_KEY')
url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'

bearer: Bearer | None = None


def get_auth_data():
    if auth_method == AuthMethod.BEARER:
        return get_bearer()
    if auth_method == AuthMethod.API_KEY:
        return get_api_key()


def get_bearer() -> str:
    global bearer
    if bearer is None or bearer.expires_at < datetime.now():
        bearer = get_new_bearer()

    return f'Bearer {bearer.token}'


def get_new_bearer() -> Bearer:
    request = OAuthToken(
        yandexPassportOauthToken=oauth_token
    )

    response = requests.post(
        url,
        json=request.model_dump()
    )

    iam_token = IAMToken.model_validate_json(response.text)

    return Bearer(iam_token)


def get_api_key():
    return f'Api-Key {api_key}'
