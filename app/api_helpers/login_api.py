from app.data.models import users
from app.schemas.login import sign_up
from app.urls.registration import sign_up_urls

def sign_up_schema():
    data = {}
    data["schema"] = sign_up
    data["urls"] = sign_up_urls()
    return data
