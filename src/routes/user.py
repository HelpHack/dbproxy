from schemas.user import User

def get_users():
    return User.objects().to_json()
