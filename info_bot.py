from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from src.db.database import store_user_info

INFO_BOT_TOKEN = os.getenv("INFO_BOT_TOKEN")

updater = Updater(INFO_BOT_TOKEN)

# Function to store user info
def update_user_info(user_id, user_data):
    store_user_info(user_id, {
        "username": user_data.username,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name
    })

# Info bot start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Info bot here! This bot stores your information for anonymous chatting.")

# Command to retrieve user info
def get_user_info(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_info = retrieve_user_info(user_id)
    update.message.reply_text(f"Your info: {user_info}")

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("get_info", get_user_info))

updater.start_polling()
updater.idle()
