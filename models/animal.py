from mongoengine import *
from . import ANIMALS

class Animal(Document):
    kind = StringField(choice=ANIMALS)
    id = StringField()
    dad = ReferenceField(Animal)
    mam = ReferenceField(Amimal)