#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    content = "Привіт!\n\
Цей чат-бот допоможе тобі познайомитися з кафедрою ближче. \
Ти дізнаєшся про викладачів, спеціальності, додаткові можливості для студентів та умови вступу.\n\
Натискай   /start"
    update.message.reply_text(content)

    content2 = "Обери, будь-ласка, теми, які тобі цікаві"
    #update.message.reply_text("Кафедра КМАД \n /about_of_CMAD_departament")
    kb_start = [[InlineKeyboardButton('Кафедра КМАД', \
                                     callback_data = 'about_of_CMAD_departament')],\
                [InlineKeyboardButton("Можливості для студентів",\
                                     callback_data = "opportunities_for_the_students")],\
                [InlineKeyboardButton("Умови вступу",\
                                     callback_data = "conditions_of_entry")]\
                ]
    reply = InlineKeyboardMarkup(kb_start)
    update.message.reply_text(content2,reply_markup = reply)
 
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def about_of_CMAD_departament(update, context):
    #update.message.reply_text("It's place for about_of_CMAD_departament")
    update.callback_query.message.reply_text("It's place for about_of_CMAD_departament")

def opportunities_for_the_students(update, context):
    pass
    #update.message.reply_text()

def conditions_of_entry(update, context):
    pass

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("Token", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    #dp.add_handler(CommandHandler("about_of_CMAD_departament",about_of_CMAD_departament))
    dp.add_handler(CallbackQueryHandler(about_of_CMAD_departament,\
                                       pattern = "about_of_CMAD_departament"))
    dp.add_handler(CallbackQueryHandler(opportunities_for_the_students,\
                                       pattern = "opportunities_for_the_students"))
    dp.add_handler(CallbackQueryHandler(conditions_of_entry,\
                                       pattern = "conditions_of_entry"))
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
