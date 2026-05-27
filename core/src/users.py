## @package users
#  Moduł zarządzający bazą danych użytkowników zapisaną w pliku JSON.

import os
import json
from config import USER_FILE


## Ładuje listę użytkowników z pliku JSON.
#  Jeśli plik nie istnieje, inicjalizuje go pustą listą.
#  @return Lista (list) słowników z danymi użytkowników.
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump([], f)

    with open(USER_FILE, "r") as f:
        return json.load(f)


## Zapisuje aktualną listę użytkowników do pliku JSON.
#  @param users Lista słowników reprezentujących użytkowników do zapisu.
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


## Sprawdza, czy użytkownik o podanym adresie e-mail posiada uprawnienia administratora.
#  @param email Adres e-mail sprawdzanego użytkownika.
#  @return True, jeśli użytkownik jest administratorem, w przeciwnym wypadku False.
def is_admin(email):
    users = load_users()

    return any(
        user["email"] == email and user["role"] == "admin"
        for user in users
    )


## Wyszukuje użytkownika w bazie na podstawie jego unikalnego identyfikatora ID.
#  @param user_id Identyfikator (int) szukanego użytkownika.
#  @return Słownik z danymi użytkownika lub None, jeśli nie znaleziono.
def find_user_by_id(user_id):
    users = load_users()
    return next((user for user in users if user["id"] == user_id), None)