
import secrets
import random

def id_generator():
    hash = secrets.token_urlsafe(random.randrange(20, 50))
    return hash