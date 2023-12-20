"""
Telegram bot tasks module
"""
from datetime import timedelta         # Required for daily messages
import pandas as pd                    # Required for tasks representation
from telegram import Message           # Required for message sending
from telegram.ext import ContextTypes  # Required for message sending

from providers.tasks import get_relevant_tasks  # Required for tasks feature


daily_subscribers = set()


async def tasks(message: Message, sub_option: str) -> None:
    """
    Send tasks
    """

    if sub_option == 'nearest':
        await message.reply_text(_nearest())
    elif sub_option == 'daily-update':
        await daily_update(message)


async def daily(context: ContextTypes.DEFAULT_TYPE) -> None:
    upcoming_tasks = get_relevant_tasks(relevance_delta=timedelta(days=2))

    tasks_info = 'Задачи на ближайшее время:\n' + _get_tasks_info(upcoming_tasks) \
        if not upcoming_tasks.empty else 'В ближайшее время задач нет'
    for daily_subscriber in daily_subscribers:
        await context.bot.send_message(chat_id=daily_subscriber, text=tasks_info)


async def daily_update(message: Message) -> None:
    chat_id = message.chat_id
    if chat_id not in daily_subscribers:
        daily_subscribers.add(chat_id)
        await message.reply_text('Вы подписались на ежедневные уведомления о задачах')
    else:
        daily_subscribers.remove(chat_id)
        await message.reply_text('Вы отписались от ежедневных уведомлений о задачах')


def _nearest(n: int = 5) -> str:
    """
    Get nearest tasks
    :param n: max number of tasks
    :return: formatted tasks info
    """

    actual_tasks = get_relevant_tasks()
    return _get_tasks_info(actual_tasks, n)


def _get_tasks_info(tasks_: pd.DataFrame, n: int = 0) -> str:
    """
    Get formatted tasks info
    :param tasks_: tasks
    :param n: max number of tasks
    :return: formatted tasks info
    """

    tasks_info = ''

    i = 0
    for index, task in tasks_.iterrows():
        tasks_info += f'{i + 1}. {task["name"]} - {task["begin"].strftime("%d.%m.%Y %H:%M")}\n'
        i += 1

        if 0 < n <= i:
            break

    return tasks_info
