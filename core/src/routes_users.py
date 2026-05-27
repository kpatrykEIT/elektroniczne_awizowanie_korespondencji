## @package routes_users
#  Punkty końcowe (endpoints) Flask do zarządzania użytkownikami (CRUD).
#  Wymagają weryfikacji uprawnień administratora.

from flask import Blueprint, request, jsonify
from users import load_users, save_users, is_admin

## Blueprint dla tras zarządzania użytkownikami.
users_bp = Blueprint("users", __name__)


## Zwraca listę wszystkich zarejestrowanych użytkowników.
#  @route GET /users
#  @return Lista użytkowników w formacie JSON.
@users_bp.route("/users", methods=["GET"])
def list_users():
    return jsonify(load_users())


## Dodaje nowego użytkownika do bazy danych.
#  Wymaga, aby w polu `admin_email` przesłać e-mail administratora.
#  @route POST /users
#  @request_json name Nazwa użytkownika.
#  @request_json email Adres e-mail użytkownika.
#  @request_json admin_email Adres e-mail osoby zlecającej (wymagany admin).
#  @request_json role Opcjonalna rola (domyślnie "user").
#  @return Status 201 (sukces) lub 403 (brak uprawnień).
@users_bp.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users = load_users()

    if not is_admin(data.get("admin_email")):
        return jsonify({"error": "Unauthorized"}), 403

    new_user = {
        "id": max([user["id"] for user in users], default=0) + 1,
        "name": data["name"],
        "email": data["email"],
        "role": data.get("role", "user")
    }

    users.append(new_user)
    save_users(users)

    return jsonify({"message": "User added successfully"}), 201


## Usuwa użytkownika z bazy danych na podstawie ID.
#  @route DELETE /users/<user_id>
#  @param user_id Identyfikator użytkownika do usunięcia.
#  @request_json admin_email Adres e-mail osoby zlecającej (wymagany admin).
#  @return Status 200 (sukces) lub 403 (brak uprawnień).
@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    data = request.json
    users = load_users()

    if not is_admin(data.get("admin_email")):
        return jsonify({"error": "Unauthorized"}), 403

    users = [user for user in users if user["id"] != user_id]
    save_users(users)

    return jsonify({"message": "User deleted successfully"}), 200


## Aktualizuje dane istniejącego użytkownika.
#  @route PUT /users/<user_id>
#  @param user_id Identyfikator modyfikowanego użytkownika.
#  @request_json admin_email Adres e-mail osoby zlecającej (wymagany admin).
#  @request_json name Nowa nazwa (opcjonalnie).
#  @request_json email Nowy e-mail (opcjonalnie).
#  @request_json role Nowa rola (opcjonalnie).
#  @return Status 200 (sukces) lub 403 (brak uprawnień).
@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    users = load_users()

    if not is_admin(data.get("admin_email")):
        return jsonify({"error": "Unauthorized"}), 403

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["role"] = data.get("role", user["role"])
            break

    save_users(users)

    return jsonify({"message": "User updated successfully"}), 200