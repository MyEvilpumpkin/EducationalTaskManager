from datetime import timedelta

from telegram import Message
from telegram.ext import ContextTypes


async def pomodoro(message: Message, context: ContextTypes.DEFAULT_TYPE, sub_option: str) -> None:
    if sub_option == 'work':
        await set_work_timer(message, context)
    elif sub_option == 'rest':
        await set_rest_timer(message, context)
    elif sub_option == 'stop':
        await unset(message, context)


async def set_work_timer(message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
    await set_timer(message, context, timedelta(minutes=25), 'Работа (25 мин.)')


async def set_rest_timer(message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
    await set_timer(message, context, timedelta(minutes=5), 'Отдых (5 мин.)')


async def set_timer(message: Message, context: ContextTypes.DEFAULT_TYPE, delta: timedelta, timer_name: str) -> None:
    chat_id = message.chat_id
    await remove_timer_if_exists(str(chat_id), context)
    context.job_queue.run_once(alarm, delta, chat_id=chat_id, name=str(chat_id), data=timer_name)

    await message.reply_text(f'Таймер {timer_name} установлен')


async def unset(message: Message, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = message.chat_id
    job_removed = await remove_timer_if_exists(str(chat_id), context)
    if not job_removed:
        await message.reply_text('Нет активного таймера')


async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    await context.bot.send_message(job.chat_id, text=f'Таймер {job.data} завершен')


async def remove_timer_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
        await context.bot.send_message(job.chat_id, text=f'Таймер {job.data} удален')
    return True


def is_timer_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    return False if not current_jobs else True
