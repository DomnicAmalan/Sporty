
from flask import Blueprint, render_template, flash
from app.data.models import sports_list
from app.helpers.db_helpers import ObjectID_to_str, str_to_ObjectID
from app.helpers.frontend_helpers import to_response

api = Blueprint('api', __name__)

@api.route('/list/sports/all')
def sports_data():
    list_sports = list(sports_list.find())
    data = ObjectID_to_str(list_sports)
    return to_response(data)