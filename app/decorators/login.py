from functools import wraps
from flask import abort, request, session
import jwt

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
            data = session.get('email')
            print(data)
            # if not 'Authorization' in request.headers:
            #    abort(401)

            user = None
           
            # token = str.replace(str(data), 'Bearer ','')
            # try:
            #     user = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['sub']
            # except:
            #     abort(401)

            return f(user, *args, **kws)            
    return decorated_function