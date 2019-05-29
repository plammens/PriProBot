from handlers import *
import logging


with open("db/TOKEN.txt") as token_file:
    TOKEN = token_file.read().strip()

UPDATER = tge.Updater(token=TOKEN, use_context=True)
BOT = UPDATER.bot
DISPATCHER = UPDATER.dispatcher

for handler in command_handlers:
    DISPATCHER.add_handler(handler)


def start_bot():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    UPDATER.start_polling()
    logging.info("bot online")


if __name__ == '__main__':
    start_bot()
