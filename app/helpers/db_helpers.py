from bson import ObjectId

def ObjectID_to_str(data):
    data_type = type(data)
    if data_type == list:
        for value in data:
            value["_id"] = str(value["_id"])
    elif data_type == dict:
        data["_id"] = str(data["_id"])
    else:
        data = str(data)
    return data

def str_to_ObjectID(data):
    data_type = type(data)
    if data_type == list:
        for value in data:
            value["_id"] = ObjectId(str(value["_id"]))
    elif data_type == dict:
        data["_id"] = ObjectId(str(data["_id"]))
    else:
        data = ObjectId(str(data))
    return data

