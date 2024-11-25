from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, ReferenceField, EmbeddedDocumentField, ListField, StringField, IntField, DictField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField()
