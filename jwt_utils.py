import jwt
from datetime import datetime, timedelta
from django.conf import settings

def create_jwt_token(user_id):
    payload={
        'user_id':user_id,
        'exp':datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm='HS256')
    return token.decode('utf-8')

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None