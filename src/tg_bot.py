import logging

from telegram_bot import application


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)

if __name__ == '__main__':
    application.start()
