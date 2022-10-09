from mongoengine import *

class User(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    phone = StringField(required=True, max_length=20)
    location = ListField(ReferenceField('Address', required=True))
    is_volunteer = BooleanField(required=True)

    meta = {'indexes': [
        {'fields': ['$first_name', "$last_name"],
         'default_language': 'english',
         'weights': {'title': 10, 'content': 2}
        }
    ]}