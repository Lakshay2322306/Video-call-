from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from src.utils.pairing import find_partner
from src.utils.user_info import update_user_info
import os

MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN")

updater = Updater(MAIN_BOT_TOKEN)

# Command to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Anonymous Chat Bot! Type /connect to start chatting with a random user.")

# Connect command to pair users
def connect(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    partner_id = find_partner(user_id)

    # Send user info to info_bot for storage
    update_user_info(os.getenv("INFO_BOT_TOKEN"), user_id, update.message.from_user)

    if partner_id:
        context.bot.send_message(chat_id=partner_id, text="You have been connected to a random user!")
        update.message.reply_text("You have been connected to a random user!")
    else:
        update.message.reply_text("Waiting for a user to connect...")

# Command to disconnect
def disconnect(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    context.bot.send_message(chat_id=user_id, text="You have disconnected.")

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("connect", connect))
updater.dispatcher.add_handler(CommandHandler("disconnect", disconnect))

updater.start_polling()
updater.idle()
