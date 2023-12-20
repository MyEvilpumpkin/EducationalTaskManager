"""
Telegram bot application module
"""
from datetime import time   # Required for daily messages
from telegram import *      # Required for telegram bot management
from telegram.ext import *  # Required for telegram bot management

from configuration.secrets import get_secret  # Required for obtaining bot token from secrets

from .keyboard import keyboard, keyboard_options  # Required for keyboards feature
from .motivation import motivation                # Required for motivation feature
from .tasks import tasks, daily, daily_update     # Required for tasks feature
from .pomodoro import pomodoro                    # Required for pomodoro feature


def start() -> None:
    """
    Bot launching
    :return:
    """

    # Application creating
    token = get_secret('BOT_TOKEN')
    application = ApplicationBuilder().token(token).post_init(_post_init).build()

    # Handlers adding
    application.add_handler(CommandHandler('start', _start_command_handler))
    application.add_handler(CommandHandler('options', _options_command_handler))
    application.add_handler(CommandHandler('daily', _daily_command_handler))
    application.add_handler(CommandHandler('help', _help_command_handler))
    application.add_handler(CallbackQueryHandler(_keyboard_button_handler))
    application.add_handler(MessageHandler(filters.COMMAND, _unknown_command_handler))

    application.job_queue.run_daily(daily, time=time(hour=10))

    # Application launching
    application.run_polling()


async def _post_init(application: Application) -> None:
    """
    Post initialization function
    """

    # Set menu commands
    await application.bot.set_my_commands([
        BotCommand('start', 'Начало работы'),
        BotCommand('options', 'Опции'),
        BotCommand('daily', 'Ежедневные сообщения о задачах\n(подписаться/отписаться)'),
        BotCommand('help', 'Помощь')
    ])


async def _start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start command handler
    """

    await update.message.reply_text('Используйте /options для просмотра доступных опций')


async def _options_command_handler(update: Update, context: CallbackContext) -> None:
    """
    /options command handler
    """

    await keyboard(update.message, 'main')


async def _daily_command_handler(update: Update, context: CallbackContext) -> None:
    """
    /daily command handler
    """

    await daily_update(update.message)


async def _help_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /help command handler
    """

    await update.message.reply_text('Используйте /start для начала работы с ботом')


async def _unknown_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Unknown command handler
    """

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю этой команды')


async def _keyboard_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Keyboard button handler
    """

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f'Выбрано: {keyboard_options[query.data]}')

    option, sub_option = query.data.split('_')[0], query.data.split('_')[1]

    if option == 'keyboard':
        await query.delete_message()
        if sub_option != 'hide':
            await keyboard(query.message, sub_option)
    else:
        if option == 'motivation':
            await motivation(query.message, sub_option)
            await keyboard(query.message, option)  # Temp
        elif option == 'tasks':
            await tasks(query.message, sub_option)
            await keyboard(query.message, 'main')  # Temp
        elif option == 'pomodoro':
            await pomodoro(query.message, context, sub_option)
            await keyboard(query.message, option)  # Temp

        # await keyboard(query.message, option)
