"""
Telegram bot pomodoro tool module
"""

from datetime import timedelta         # Required for pomodoro timers

from telegram import Message           # Required for message sending
from telegram.ext import ContextTypes  # Required for message sending


async def pomodoro(message: Message, context: ContextTypes.DEFAULT_TYPE, sub_option: str) -> None:
    """
    Set or unset pomodoro timer
    """

    if sub_option == 'work':
        await _set_work_timer(message, context)
    elif sub_option == 'rest':
        await _set_rest_timer(message, context)
    elif sub_option == 'stop':
        await _unset_timer(message, context)


async def _set_work_timer(message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Set work pomodoro timer
    """

    await _set_timer(message, context, timedelta(minutes=25), 'Работа (25 мин.)')


async def _set_rest_timer(message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Set rest pomodoro timer
    """

    await _set_timer(message, context, timedelta(minutes=5), 'Отдых (5 мин.)')


async def _set_timer(message: Message, context: ContextTypes.DEFAULT_TYPE, delta: timedelta, timer_name: str) -> None:
    """
    Set pomodoro timer
    """

    chat_id = message.chat_id
    await _remove_timer_if_exists(str(chat_id), context)
    context.job_queue.run_once(_alarm, delta, chat_id=chat_id, name=str(chat_id), data=timer_name)

    await message.reply_text(f'Таймер {timer_name} установлен')


async def _unset_timer(message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Unset pomodoro timer
    """

    chat_id = message.chat_id
    job_removed = await _remove_timer_if_exists(str(chat_id), context)
    if not job_removed:
        await message.reply_text('Нет активного таймера')


async def _alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Notify user about timer
    """

    job = context.job
    await context.bot.send_message(job.chat_id, text=f'Таймер {job.data} завершен')


async def _remove_timer_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Remove timer if timer exists
    :return: True if timer exists, False otherwise
    """

    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
        await context.bot.send_message(job.chat_id, text=f'Таймер {job.data} удален')
    return True


def _is_timer_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Check timer exists
    :return: True if timer exists, False otherwise
    """

    current_jobs = context.job_queue.get_jobs_by_name(name)
    return False if not current_jobs else True
