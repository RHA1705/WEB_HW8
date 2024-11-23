from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, IntField, DictField


class Cats(Document):
    name = StringField()
    age = IntField()
    features = ListField()
    owners = DictField()