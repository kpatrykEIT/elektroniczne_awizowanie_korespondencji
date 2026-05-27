## @package config
#  Moduł odpowiedzialny za konfigurację aplikacji oraz zarządzanie plikami JSON.

import os
import json

## Ścieżka do katalogu, w którym zapisywane są przesyłane zdjęcia.
UPLOAD_FOLDER = "uploads"
## Nazwa pliku JSON przechowującego dane użytkowników.
USER_FILE = "users.json"
## Nazwa pliku JSON z danymi konfiguracyjnymi (np. SMTP).
CONFIG_FILE = "config.json"


## Ładuje konfigurację aplikacji z pliku JSON.
#  Jeśli plik konfiguracyjny nie istnieje, tworzy go z domyślnymi wartościami.
#  @return Słownik (dict) zawierający ustawienia administratora i serwera SMTP.
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


## Globalny obiekt konfiguracji załadowany przy starcie modułu.
config = load_config()