# info_bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Info bot here! This bot stores your information for anonymous chatting.")

def get_user_info(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_info = retrieve_user_info(user_id)
    update.message.reply_text(f"Your info: {user_info}")

def run_info_bot():
    updater = Updater(os.getenv("INFO_BOT_TOKEN"))
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("get_info", get_user_info))
    updater.start_polling()
    updater.idle()
