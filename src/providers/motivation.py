"""
Motivation provider
"""

from .yandex_gpt.dto import Message  # Required for message creation
from .yandex_gpt.chat import send    # Required for message sending


system_message = Message.system_message(
    '''
    Ты - помощник студента, который должен поддерживать мотивацию. 
    Отвечай кратко, в пределах 10-15 слов, вдохновляющим и позитивным тоном. 
    Включай в свои ответы слова поддержки и утверждения.
    '''
)


def get_motivation(user_message_text: str) -> str:
    """
    Get motivation response from YandexGPT
    :param user_message_text: message from user
    :return: model response
    """

    if not user_message_text:
        return ''

    response = send([system_message, Message.user_message(user_message_text)])

    return response.message.text if response else ''
