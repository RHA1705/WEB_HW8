from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True, unique=True)
    is_sent = BooleanField(default=False)
