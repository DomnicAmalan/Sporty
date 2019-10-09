from app.data.models import users
from app.schemas.login import user
from app.urls.registration import sign_up_urls

def sign_up_schema():
    data = {}
    data["schema"] = user
    data["urls"] = sign_up_urls()
    return data
