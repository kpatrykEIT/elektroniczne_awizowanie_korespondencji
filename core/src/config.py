import os
import json

UPLOAD_FOLDER = "uploads"
USER_FILE = "users.json"
CONFIG_FILE = "config.json"


def load_config():
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "admin_email": "twoj_email@gmail.com",
            "email_password": "twoje_haslo_app",
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


config = load_config()