SUCCESS = {"message": "Success", "status": True}
FAILED = {"message": "Value Empty", "status": False}

def check_empty_value(data):
    if type(data) == dict:
        if dict_val_empty(data):
            return SUCCESS
        return FAILED
    elif type(data) == list:
        if array_empty(data):
            return SUCCESS
        return FAILED
    else:
        if str_empty(data):
            return SUCCESS
        return FAILED

def str_empty(data):
    if not data:
        return False
    return True

def array_empty(data):
    if not data:
        return False
    return True

def dict_val_empty(data):
    if not data:
        return False
    else:
        for i in data:
            if not data[i]:
                return False
    return True
