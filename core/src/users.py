import os
import json
from config import USER_FILE


def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump([], f)

    with open(USER_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


def is_admin(email):
    users = load_users()

    return any(
        user["email"] == email and user["role"] == "admin"
        for user in users
    )


def find_user_by_id(user_id):
    users = load_users()
    return next((user for user in users if user["id"] == user_id), None)