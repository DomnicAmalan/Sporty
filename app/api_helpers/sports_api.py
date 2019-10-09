from app.data.models import sports_list
from app.helpers.db_helpers import ObjectID_to_str, str_to_ObjectID

def sports_all():
    list_sports = list(sports_list.find())
    data = ObjectID_to_str(list_sports)
    return data