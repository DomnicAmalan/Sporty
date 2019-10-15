from app.data.models import users, verication_codes
from app.schemas.login import sign_up, login
from app.urls.registration import sign_up_urls, login_urls
import json
from app.helpers import countries, mail, verification_code, db_helpers, authentication

SUCCESS = {"message":"", "status":True}
FAILED = {"message":"", "status":False}

def sign_up_schema():
    data = {}
    data["schema"] = sign_up
    data["urls"] = sign_up_urls()
    # data["countries"] = countries_list()
    return data

def login_schema():
    data = {}
    data["schema"] = login
    data["urls"] = login_urls()
    return data

def sign_up_check(data):
    data = clean_data(data)
    code = verification_code.id_generator()
    try:
        if not check_user_exists(data):
            users.insert_one(additional_signup_data(data))
            update_verification(data["email"], {"verification_code":code}, False)
            mail.send_confirmation_mail(data['email'], code)
            SUCCESS["message"] = "Email Has been sent to you, kindly confirm"
            return SUCCESS
        else:
            FAILED["message"] = "Email or Mobile number already Exists"
            return FAILED
    except Exception as e:
        FAILED["message"] = "System Error Contact Admin amalandomnic@gmail.com"
        return FAILED

def check_user_exists(data):
    return bool(list(users.find({"$and" : [{'email':  data['email'], "mobile_number": data["mobile_number"]}]})))

def clean_data(data):
    for key in data.keys():
        data[key]= data[key].strip()
    return data

def additional_signup_data(data):
    data["verified"]= False
    return data

def login_check(data):
    try:
        verfied = users.find_one({"email":data["email"]})["verified"]
        if not verfied:
            FAILED["message"] = "Please verify your email address"
            return FAILED
        else:
            SUCCESS["message"] = "Login Succesful"
            return SUCCESS
    except Exception as e:
        FAILED["message"] = "System error contact administrator amalandomnic@gmail.com"
        return FAILED

def update_verification(email, data, delete=False):
    operation = "$set" if not delete else "$unset"
    users.update_one({'email': email}, {operation: data})
    print("tttt")
    pass

def confirm_token(token):
    try:
        data = users.find_one({"verification_code": token})
        if not data:
            FAILED["message"] = "Token Invalid"
            return FAILED
        else:
            update_verification(data['email'], {"verified":True}, False)
            update_verification(data['email'], {"verification_code":token}, True)
            SUCCESS["message"] = "Verified Successfully"
            return SUCCESS
    except Exception as e:
        FAILED["message"] = "System error contact admin amaandomnic@gmail.com"
        return FAILED

def create_password(password):
    password = authentication.encryption(password, True)
    return SUCCESS

