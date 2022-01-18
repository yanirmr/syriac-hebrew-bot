#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Transliteration Telegram bot for Hebrew to Syriac and vice versa.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

"""

import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from transliteration import transliterate


def start(update, context):
    """Send a message when the command /start is issued."""
    update.effective_message.reply_text('שלום, יש להכניס כאן טקסט בעברית או בסורית')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.effective_message.reply_text('Help!')


def transliterate_massage(update, context):
    """Transliterate the the user message from Hebrew to Syriac or vice versa."""
    update.effective_message.reply_text(transliterate(update.effective_message.text))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    # Set these variable to the appropriate values	
    TOKEN = TELEGRAM_TOKEN
    
    # Port is given by Heroku	
    PORT = os.environ.get('PORT')
    
    # Enable logging	
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',	
                        level=logging.INFO)	
    logger = logging.getLogger(__name__)
    
    # Set up the Updater	
    updater = Updater(TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Set up the Updater	    
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - transliterate the message on Telegram
    dp.add_handler(CommandHandler('start', start))	
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, transliterate_massage))

    # log all errors
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=f"https://{NAME}.herokuapp.com/{TOKEN}")
    updater.idle()


if __name__ == '__main__':
    main()



