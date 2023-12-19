import requests

from .dto import *
from .auth import get_auth_data
from libs.secrets_manager import get_secret


default_completion_options = CompletionOptions(
    stream=False,
    temperature=1,
    maxTokens=1000
)

model_name = 'yandexgpt-lite'
url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

catalog = get_secret('GPT_CATALOG')


def send(messages: list[Message] = None, completion_options: CompletionOptions = None) -> Message | None:
    gpt_request = Request(
        modelUri=f'gpt://{catalog}/{model_name}',
        completionOptions=completion_options if completion_options else default_completion_options,
        messages=messages
    )

    response = requests.post(
        url,
        headers={
            'Authorization': get_auth_data()
        },
        json=gpt_request.model_dump()
    )

    gpt_response = Response.model_validate_json(response.text)
    alternatives = gpt_response.result.alternatives

    return alternatives[0] if alternatives else None
