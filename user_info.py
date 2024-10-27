import requests
import os

def update_user_info(info_bot_token, user_id, user_data):
    url = f"https://api.telegram.org/bot{info_bot_token}/sendMessage"
    data = {
        "chat_id": user_id,
        "text": f"Storing info for user: {user_data.first_name} {user_data.last_name} (@{user_data.username})"
    }
    requests.post(url, data=data)
