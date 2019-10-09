
from flask import Blueprint, render_template, flash
from app.helpers.frontend_helpers import to_response, covert_to_string
from app.api_helpers import login_api, sports_api

api = Blueprint('api', __name__)

@api.route('/list/sports/all')
def sports_data():
    return to_response(sports_api.sports_all())

@api.route('/schema/user/signup')
def sign_up():
    return to_response(login_api.sign_up_schema())