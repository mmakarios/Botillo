import os
import time
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from botillo_token import TOKEN
from restricted_wrap import restricted

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('eae')


@restricted
def restart(bot, update):
    update.message.reply_text("Restarting...")
    time.sleep(0.2)
    os.execl(sys.executable, sys.executable, *sys.argv)


def echo(bot, update):
    update.message.chat.send_action('typing')
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    update.message.reply_text(text_caps)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(CommandHandler('r', restart))

    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))

    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
