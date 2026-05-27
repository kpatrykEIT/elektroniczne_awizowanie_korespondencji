## @package routes_upload
#  Punkty końcowe (endpoints) Flask obsługujące przesyłanie plików ze zdjęciami (PC oraz ESP).

from flask import Blueprint, request, jsonify
import os
import json
import datetime

from config import UPLOAD_FOLDER
from users import find_user_by_id
from email_service import send_email

## Blueprint dla tras przesyłania plików.
upload_bp = Blueprint("upload", __name__)


## Obsługuje przesyłanie zdjęcia paczki bezpośrednio z komputera (laptopa).
#  Zapisuje plik i wysyła powiadomienie e-mail do adresata.
#  @route POST /upload
#  @request_form file Plik graficzny (.jpg).
#  @request_form user_id Identyfikator użytkownika docelowego.
#  @return Odpowiedź JSON ze statusem 200 (sukces) lub 400/404 (błąd).
@upload_bp.route("/upload", methods=["POST"])
def upload_photo_from_laptop():
    if "file" not in request.files or "user_id" not in request.form:
        return jsonify({"error": "Missing file or user_id"}), 400

    file = request.files["file"]
    user_id = int(request.form["user_id"])

    user = find_user_by_id(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    filename = f"user_{user_id}.jpg"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(file_path)

    send_email(
        user["email"],
        "Nowa przesyłka!",
        f"Hej {user['name']}, masz nową przesyłkę.",
        file_path
    )

    return jsonify({"message": "Photo uploaded and email sent"}), 200


## Odbiera proste wiadomości tekstowe/statusowe w formacie JSON z modułu ESP.
#  @route POST /esp
#  @request_json Dane wysłane przez ESP.
#  @return Odpowiedź JSON potwierdzająca odebranie wiadomości.
@upload_bp.route("/esp", methods=["POST"])
def esp_message():
    data = request.json

    print(f"[ESP] Otrzymano dane: {data}")

    return jsonify({"message": "ESP message received"}), 200


## Obsługuje zaawansowane przesyłanie zdjęć i metadanych bezpośrednio z urządzenia ESP.
#  Generuje unikalną nazwę pliku na podstawie znacznika czasu i powiadamia mailowo użytkownika.
#  @route POST /esp-upload
#  @request_form file Plik graficzny z kamery ESP.
#  @request_form json Ciąg tekstowy JSON zawierający: device_id, user_id, message.
#  @return Odpowiedź JSON ze statusem 200, 400, 404 lub 500 (błąd serwera).
@upload_bp.route("/esp-upload", methods=["POST"])
def esp_upload():
    try:
        if "file" not in request.files or "json" not in request.form:
            return jsonify({"error": "Missing file or json"}), 400

        file = request.files["file"]
        metadata = json.loads(request.form["json"])

        device_id = metadata.get("device_id")
        message = metadata.get("message")
        user_id = metadata.get("user_id")

        print(f"[ESP-UPLOAD] device_id={device_id}, user_id={user_id}, message={message}")

        filename = f"{device_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(file_path)

        user = find_user_by_id(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        send_email(
            user["email"],
            "Nowa przesyłka z ESP!",
            f"Hej {user['name']}, przesyłka została wykryta.\n\nKomunikat ESP: {message}",
            file_path
        )

        return jsonify({"message": "ESP photo saved and email sent"}), 200

    except Exception as e:
        print(f"ESP upload error: {e}")
        return jsonify({"error": "ESP upload failed"}), 500