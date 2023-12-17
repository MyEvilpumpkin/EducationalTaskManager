from telegram import Update, InlineKeyboardMarkup, Message
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from src.libs.secrets_manager import get_secret
from src.modules.motivation_generator import generate as generate_motivation

from .keyboards import keyboards, keyboard_options


def start():
    token = get_secret('BOT_TOKEN')
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()


async def send_keyboard(message: Message, keyboard_name: str):
    keyboard = keyboards[keyboard_name]
    await message.reply_text('Пожалуйста, выберите:', reply_markup=InlineKeyboardMarkup(keyboard))


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_keyboard(update.message, 'main')


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f'Выбрано: {keyboard_options[query.data]}')

    if query.data == 'motivation':
        await query.message.reply_text(
            generate_motivation('У меня трудности с учебой, скажи, что-нибудь мотивирующее')
        )
    elif query.data == 'motivation_phrase':
        await query.message.reply_text(
            generate_motivation('Скажи небольшую мотивационную фразу про учебу')
        )

    await send_keyboard(query.message, 'main')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Используйте /start для начала работы с ботом')


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю этой команды')
