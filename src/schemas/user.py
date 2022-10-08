from mongoengine import *

class User(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    phone = StringField(required=True, max_length=20)
    location = GeoPointField(required=True)
