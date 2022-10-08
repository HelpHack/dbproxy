from schemas.user import User

def get_users():
    return User.objects().to_json()

def add_user(obj):
    user = User(**obj)
    user.save()
    return user.to_json()

def get_user_by_id(id):
    return User.objects(id=id).to_json()