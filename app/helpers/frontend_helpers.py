import json

def to_response(data):
    data = json.dumps(data)
    return data
