"""
Telegram bot launcher
"""

import logging  # Required for bot logging

from telegram_bot import bot  # Required for bot launching


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)

if __name__ == '__main__':
    bot.start()
