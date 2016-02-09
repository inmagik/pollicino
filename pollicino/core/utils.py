import jwt

SECRET_KEY = "123123123a2d3a12-3131313ddddd"

def generate_jwt(payload):
    return jwt.encode(payload, 
        SECRET_KEY, 
        algorithm='HS256'
    )


def decode_jwt(encoded):
    return jwt.decode(encoded, SECRET_KEY, algorithms=['HS256'])