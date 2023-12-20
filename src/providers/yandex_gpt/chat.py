"""
Module that contains code for working with the YandexGPT model
"""

import requests  # Required for model requests

from configuration.secrets import get_secret    # Required to get secrets
from configuration.settings import get_setting  # Required to get settings

from .dto import *               # Required for working with data transfer objects
from .auth import get_auth_data  # Required to get authentication data


model_url = get_setting('GPT_MODEL_URL')
model_name = get_setting('GPT_MODEL_NAME')
catalog = get_secret('GPT_CATALOG')


def send(messages: list[Message], options: Options = None) -> Message | None:
    """
    Send a message to the YandexGPT model and return the response
    :param messages: conversation history
    :param options: model options (optional)
    :return: model response
    """

    gpt_request = Request(
        modelUri=f'gpt://{catalog}/{model_name}',
        completionOptions=options if options else Options.default(),
        messages=messages
    )

    response = requests.post(
        model_url,
        headers={
            'Authorization': get_auth_data()
        },
        json=gpt_request.model_dump()
    )

    gpt_response = Response.model_validate_json(response.text)
    alternatives = gpt_response.result.alternatives

    return alternatives[0] if alternatives else None
