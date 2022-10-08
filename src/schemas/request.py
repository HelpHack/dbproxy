from mongoengine import *
from data.request import RequestStatus

class Request(Document):
    requester = ReferenceField('User', required=True)
    volunteer = ReferenceField('User', required=False)
    location = ReferenceField('Address', required=False)
    description = StringField(required=True, max_length=1000)
    status = EnumField(RequestStatus, required=True)

    meta = {'indexes': [
        {'fields': ['$description', "$status"],
         'default_language': 'english',
         'weights': {'title': 10, 'content': 2}
        }
    ]}

# class ShoppingListItem(EmbeddedDocument):
#     item = StringField(required=True, max_length=100)
#     ticked = BooleanField(required=True)

# class ShoppingList(Request):
#     items = ListField(EmbeddedDocumentField('ShoppingListItem'), required=True)

