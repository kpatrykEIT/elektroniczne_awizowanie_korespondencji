## @package routes_admin
#  Punkty końcowe (endpoints) Flask dla panelu administracyjnego.

from flask import Blueprint, render_template

## Blueprint dla tras administracyjnych.
admin_bp = Blueprint("admin", __name__)


## Wyświetla główną stronę panelu administratora.
#  @route GET /admin
#  @return Wyrenderowany szablon HTML "admin.html".
@admin_bp.route("/admin")
def admin_panel():
    return render_template("admin.html")