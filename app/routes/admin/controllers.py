from flask import Blueprint


admin = Blueprint('admin', __name__, template_folder="templates/client")


@admin.route('/google')
def index():
    return "Admin"