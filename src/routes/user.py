from schemas.user import User

def get_users():
    return User.objects().to_json()

def add_user(obj):
    user = User(**obj)
    user.save()
    return user.to_json()

def get_user_by_id(id):
    return User.objects.aggregate([
        {
            '$match': {
                '_id': id
            }
        },
        {
            "$lookup": {
                "from": "address",
                "localField": "locations",
                "foreignField": "_id",
                "as": "locations"
            }
        }
    ]).to_json()