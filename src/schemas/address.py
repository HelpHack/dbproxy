from mongoengine import *

class Address(Document):
    user = ReferenceField('User', required=True)
    city = StringField(required=True, max_length=50)
    country = StringField(required=True, max_length=50)
    address = StringField(required=True, max_length=100)
    postcode = StringField(required=True, max_length=10)
    location = GeoPointField()

    meta = {'indexes': [
        {'fields': ['$city', "$country", "$address", "$postcode"],
         'default_language': 'english',
         'weights': {'title': 10, 'content': 2}
        }
    ]}
