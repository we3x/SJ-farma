from mongoengine import *
from .animal import Animal
from constants import ANIMALS

class Stall(EmbeddedDocument):
    name = StringField(max_length=32)
    kind = StringField(choice=ANIMALS)
    animals = ListField(EmbeddedDocumentField(Animal))


class Farm(Document):
    name = StringField()
    stalls = ListField(EmbeddedDocumentField(Stall))

    def __repr__(self):
        return 'Farm: %s' % self.name