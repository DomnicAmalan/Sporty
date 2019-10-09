from flask import Blueprint, render_template
from app.data.models import sports_list

admin = Blueprint('admin', __name__, template_folder="templates")


@admin.route('/')
def index():
    return render_template("admin/sports.html")

@admin.route('/login')
def login():
    return render_template("admin/login.html")