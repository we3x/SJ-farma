from mongoengine import *
from .animal import Animal

ANIMALS = ('pig', 'cow', 'sheep')

class Stall(EmbeddedDocument):
    kind = StringField(choice=ANIMALS)
    animals = ListField(ReferenceField(Animal))


class Farm(Document):
    name = StringField()
    stalls = ListField(EmbeddedDocumentField(Stall))