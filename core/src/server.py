## @package server
#  Główny punkt wejścia aplikacji Flask. Inicjalizuje serwer i rejestruje moduły routingu.

from flask import Flask
import os

from config import UPLOAD_FOLDER
from routes_users import users_bp
from routes_upload import upload_bp
from routes_admin import admin_bp

## Instancja aplikacji Flask.
app = Flask(__name__)

# Upewnia się, że folder na przesyłane pliki istnieje.
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Rejestracja poszczególnych komponentów (Blueprints) aplikacji.
app.register_blueprint(users_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    ## Uruchomienie serwera na porcie 5000, dostępnego w sieci lokalnej (0.0.0.0).
    app.run(host="0.0.0.0", port=5000)