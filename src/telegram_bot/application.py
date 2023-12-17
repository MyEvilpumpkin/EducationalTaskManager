from telegram import Update, InlineKeyboardMarkup, Message, BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, \
    CallbackQueryHandler, CallbackContext, Application

from src.libs.secrets_manager import get_secret
from src.modules.motivation_generator import generate as generate_motivation

from .keyboard import keyboards, keyboard_options
from .motivation import motivations
from .tasks import tasks
from .pomodoro import pomodoro


def start() -> None:
    token = get_secret('BOT_TOKEN')
    application = ApplicationBuilder().token(token).post_init(post_init).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('options', options_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()


async def post_init(application: Application) -> None:
    await application.bot.set_my_commands([
        BotCommand('start', 'Начало работы'),
        BotCommand('options', 'Опции'),
        BotCommand('help', 'Помощь')
    ])


async def send_keyboard(message: Message, keyboard_name: str) -> None:
    keyboard = keyboards[keyboard_name]
    await message.reply_text('Пожалуйста, выберите:', reply_markup=InlineKeyboardMarkup(keyboard))


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Используйте /options для просмотра доступных опций ')


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f'Выбрано: {keyboard_options[query.data]}')

    option, sub_option = get_option(query.data)

    if option == 'keyboard':
        await query.delete_message()
        if sub_option != 'hide':
            await send_keyboard(query.message, sub_option)
    else:
        if option == 'motivation':
            await query.message.reply_text(
                generate_motivation(motivations.get(sub_option))
            )
        elif option == 'tasks':
            await query.message.reply_text(
                tasks.get(sub_option)()
            )
        elif query.data.startswith('pomodoro'):
            await pomodoro(query.message, context, sub_option)

        await send_keyboard(query.message, option)


async def options_command(update: Update, context: CallbackContext) -> None:
    await send_keyboard(update.message, 'main')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Используйте /start для начала работы с ботом')


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю этой команды')


def get_option(command: str) -> tuple[str, str]:
    return command.split('_')[0], command.split('_')[1]
