user_db = {}

def store_user_info(user_id, info):
    user_db[user_id] = info

def retrieve_user_info(user_id):
    return user_db.get(user_id, "No info available")
