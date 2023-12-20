"""
Telegram bot motivation module
"""

from telegram import Message  # Required for message sending

from providers.motivation import get_motivation  # Required for motivation feature


motivations = {
    'quote': 'Скажи небольшую мотивационную цитату про учебу',
    'advice': 'Подскажи один короткий совет по учебе',
    'exams': 'Как лучше подготовиться перед экзаменом?',
    'time-management': 'Как лучше организовать своё учебное время?'
}


async def motivation(message: Message, sub_option: str) -> None:
    """
    Send motivation
    """

    await message.reply_text(
        get_motivation(motivations.get(sub_option))
    )
