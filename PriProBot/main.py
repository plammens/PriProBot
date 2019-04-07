import telegram.ext as tge


with open("db/TOKEN.txt") as token_file:
    TOKEN = token_file.read().strip()

UPDATER = tge.Updater(token=TOKEN)
BOT = UPDATER.bot
DISPATCHER = UPDATER.dispatcher


def main():
    pass


if __name__ == '__main__':
    main()
