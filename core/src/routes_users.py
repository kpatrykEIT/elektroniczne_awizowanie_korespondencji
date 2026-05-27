from flask import Blueprint, request, jsonify
from users import load_users, save_users, is_admin

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def list_users():
    return jsonify(load_users())


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


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    data = request.json
    users = load_users()

    if not is_admin(data.get("admin_email")):
        return jsonify({"error": "Unauthorized"}), 403

    users = [user for user in users if user["id"] != user_id]
    save_users(users)

    return jsonify({"message": "User deleted successfully"}), 200


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