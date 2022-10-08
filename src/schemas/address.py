from mongoengine import *

class Address(Document):
    street = StringField(required=True, max_length=100)
    city = StringField(required=True, max_length=50)
    state = StringField(required=True, max_length=50)
    zip = StringField(required=True, max_length=10)
    country = StringField(required=True, max_length=50)
