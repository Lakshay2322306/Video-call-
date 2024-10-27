# src/server.py
from flask import Flask
import os
import threading
from main_bot import run_main_bot
from info_bot import run_info_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bots are running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))  # Render expects PORT variable
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()

    # Start the bots
    run_main_bot()  # Ensure you create run_main_bot function in main_bot.py
    run_info_bot()  # Ensure you create run_info_bot function in info_bot.py
