from mongoengine import *
from .user import User

class Service(EmbeddedDocument):
    id = StringField(max_length=32)
    name = StringField(max_length=64)
    price = DecimalField()

class Vet(User):
    station_name = StringField(max_length=64)
    services = ListField(EmbeddedDocumentField(Service))

