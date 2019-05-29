import telegram.ext as tge
import telegram
import random
import logging


command_handlers = []


def cmd_handler(callback):
    def decorated(update: telegram.Update, context: tge.CallbackContext):
        callback(update, context)
        logging.log(logging.INFO, f"served /{callback.__name__} to chat {update.effective_chat.id}")

    command_handlers.append(tge.CommandHandler(callback.__name__, decorated))
    return callback


@cmd_handler
def start(update: telegram.Update, context: tge.CallbackContext):
    update.message.reply_markdown("_PrippròBot è impripprottito_ 🐤")


chirp_list = ["ciù!", "pripprò!", "cirp!"]

for i in range(1, 4):
    chirp_list.append(
        lambda _i=i: open('db/voice/cirp{}.opus'.format(_i), 'rb'))


@cmd_handler
def cirpa(update: telegram.Update, context: tge.CallbackContext):
    chirp = random.choice(chirp_list)
    if isinstance(chirp, str): update.message.reply_text(chirp)
    else: update.message.reply_voice(chirp())
