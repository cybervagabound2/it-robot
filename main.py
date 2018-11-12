import logging
from telegram.ext improt (Updater, CommandHandler, Filters, CallbackQueryHandler)
from handlers.start import start


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater('631771539:AAEYWzzk3HYbWXP9OAM3bklD56Z40H1K9dA')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_error_handler(error)
    