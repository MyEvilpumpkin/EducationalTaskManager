from yandex_gpt.dto import Message
from yandex_gpt.chat import send

start_message = Message.system_message(
    'Ты - помощник студента, который должен поддерживать мотивацию. Отвечай кратко.'
)


def generate(query: str) -> str:
    if not query:
        return ''

    response = send([start_message, Message.user_message(query)])

    return response.message.text if response else ''
