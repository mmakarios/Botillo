import os
import time
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credentials import TOKEN
from restricted_wrap import restricted

# Python logging configurations
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
    # Connect to Telegram API
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    # Add message handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('r', restart))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('caps', caps, pass_args=True))

    # Log errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    logger.info("Starting...")

    # Block until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
