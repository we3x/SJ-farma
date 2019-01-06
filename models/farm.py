from mongoengine import *
from . import ANIMALS

class Stall(EmbededDocument):
    kind = StringField(choice=ANIMALS)
    animals = ListField(ReferenceField(Animal))


class Farm(Document):
    name = StringField()
    stalls = ListField(EmbeddedDocument(Stall))