from telegram import Message
from telegram.ext import ContextTypes

from src.modules.motivation_generator import generate as generate_motivation


motivations = {
    'quote': 'Скажи небольшую мотивационную цитату про учебу',
    'advice': 'Подскажи один короткий совет по учебе',
    'exams': 'Как лучше подготовиться перед экзаменом?',
    'time-management': 'Как лучше организовать своё учебное время?'
}


async def motivation(message: Message, context: ContextTypes.DEFAULT_TYPE, sub_option: str) -> None:
    await message.reply_text(
        generate_motivation(motivations.get(sub_option))
    )
