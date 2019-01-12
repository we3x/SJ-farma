from mongoengine import *
from constants import ANIMALS

class Animal(Document):
    kind = StringField(choice=ANIMALS)
    id = StringField()
    