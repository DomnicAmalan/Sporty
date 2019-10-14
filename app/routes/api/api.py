
from flask import Blueprint, render_template, flash, request
from app.helpers.frontend_helpers import to_response, covert_to_string
from app.api_helpers import sports_api, login_api

api = Blueprint('api', __name__)

@api.route('/list/sports/all', methods=["GET"])
def sports_data():
    return to_response(sports_api.sports_all())

@api.route('/signup/user/schema', methods=["GET"])
def signup_schema():
    return login_api.sign_up_schema()

@api.route('/signup/user/submit', methods=["POST"])
def signup_user():
    return login_api.sign_up_check(request.json)

@api.route('/login/user/schema')
def login_schema():
    return login_api.login_schema()

@api.route('/login/user/submit', methods=["POST"])
def login_user():
    return login_api.login_check(request.json)
