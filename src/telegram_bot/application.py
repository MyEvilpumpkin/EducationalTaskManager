from telegram import Update, InlineKeyboardMarkup, Message, BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, \
    CallbackQueryHandler, CallbackContext, Application

from src.libs.secrets_manager import get_secret
from src.modules.motivation_generator import generate as generate_motivation
from src.modules.tasks_handler import get_actual_tasks

from .keyboard import keyboards, keyboard_options
from .motivation import motivations


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

    if query.data.startswith('keyboard_'):
        await query.delete_message()
        keyboards_option = query.data.split('_')[1]
        if keyboards_option != 'hide':
            await send_keyboard(query.message, keyboards_option)
    elif query.data.startswith('motivation_'):
        motivation_option = query.data.split('_')[1]
        await query.message.reply_text(
            generate_motivation(motivations.get(motivation_option))
        )
        await send_keyboard(query.message, 'motivation')
    elif query.data == 'tasks_nearest':
        tasks = get_actual_tasks()
        tasks_info = ''
        n = 5
        i = 0
        for index, task in tasks.iterrows():
            tasks_info += f'{i + 1}. {task["name"]} - {task["begin"].strftime("%d.%m.%Y %H:%M")}\n'
            i += 1
            if i >= n:
                break
        await query.message.reply_text(
            tasks_info
        )
        await send_keyboard(query.message, 'main')


async def options_command(update: Update, context: CallbackContext) -> None:
    await send_keyboard(update.message, 'main')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Используйте /start для начала работы с ботом')


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю этой команды')
