"""
Telegram bot tasks module
"""

import pandas as pd           # Required for tasks representation
from telegram import Message  # Required for message sending

from providers.tasks import get_relevant_tasks  # Required for tasks feature


async def tasks(message: Message, sub_option: str) -> None:
    """
    Send tasks
    """

    if sub_option == 'nearest':
        await message.reply_text(nearest())


def nearest(n: int = 5) -> str:
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
