from flask import Flask
import os

from config import UPLOAD_FOLDER
from routes_users import users_bp
from routes_upload import upload_bp
from routes_admin import admin_bp

app = Flask(__name__)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.register_blueprint(users_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)