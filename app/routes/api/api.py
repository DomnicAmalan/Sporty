
from flask import Blueprint, render_template, flash, request, abort, redirect
from app.helpers.frontend_helpers import to_response, covert_to_string
from app.api_helpers import sports_api, login_api
from app.routes.client.controllers import create_password_page, login

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

@api.route('/verify/user/<token>', methods=["POST", "GET"])
def verification_user(token):
    if login_api.confirm_token(token)['status']:
        return create_password_page(login_api.confirm_token(token)['email'])
    else:
        return login_api.confirm_token(token)['message']

@api.route('/password/create', methods=["POST"])
def create_password():
    return login_api.create_password(request.json)

@api.route('/logout', methods=['GET'])
def sign_out():
    login_api.clear_session()
    return login()