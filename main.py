# main_bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Anonymous Chat Bot! Type /connect to start chatting with a random user.")

def connect(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    partner_id = find_partner(user_id)
    update_user_info(os.getenv("INFO_BOT_TOKEN"), user_id, update.message.from_user)

    if partner_id:
        context.bot.send_message(chat_id=partner_id, text="You have been connected to a random user!")
        update.message.reply_text("You have been connected to a random user!")
    else:
        update.message.reply_text("Waiting for a user to connect...")

def run_main_bot():
    updater = Updater(os.getenv("MAIN_BOT_TOKEN"))
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("connect", connect))
    updater.start_polling()
    updater.idle()
