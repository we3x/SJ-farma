from mongoengine import *
from .user import User
from .task import Task

class Service(EmbeddedDocument):
    id = StringField(max_length=32)
    name = StringField(max_length=64)
    price = DecimalField()

class Vet(User, Document):
    station_name = StringField(max_length=64)
    services = ListField(EmbeddedDocumentField(Service))

