from os import environ

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from lib.custom_updater import CustomUpdater


def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Hi!')


def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Help!')


def create_updater(**kwargs) -> CustomUpdater:
    updater = CustomUpdater(environ.get('BOT_ID'), **kwargs)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    return updater
