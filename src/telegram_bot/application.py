from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, \
    CallbackQueryHandler, CallbackContext, Application

from src.libs.secrets_manager import get_secret

from .keyboard import keyboard, keyboard_options
from .motivation import motivation
from .tasks import tasks
from .pomodoro import pomodoro


def start() -> None:
    token = get_secret('BOT_TOKEN')
    application = ApplicationBuilder().token(token).post_init(post_init).build()

    application.add_handler(CommandHandler('start', start_command_handler))
    application.add_handler(CommandHandler('options', options_command_handler))
    application.add_handler(CommandHandler('help', help_command_handler))
    application.add_handler(CallbackQueryHandler(keyboard_button_handler))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command_handler))

    application.run_polling()


async def post_init(application: Application) -> None:
    await application.bot.set_my_commands([
        BotCommand('start', 'Начало работы'),
        BotCommand('options', 'Опции'),
        BotCommand('help', 'Помощь')
    ])


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Используйте /options для просмотра доступных опций')


async def options_command_handler(update: Update, context: CallbackContext) -> None:
    await keyboard(update.message, 'main')


async def help_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Используйте /start для начала работы с ботом')


async def unknown_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю этой команды')


async def keyboard_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
            await motivation(query.message, context, sub_option)
            await keyboard(query.message, option)
        elif option == 'tasks':
            await tasks(query.message, context, sub_option)
            await keyboard(query.message, 'main')
        elif option == 'pomodoro':
            await pomodoro(query.message, context, sub_option)
            await keyboard(query.message, option)

        # await keyboard(query.message, option)
