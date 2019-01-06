from mongoengine import *

ANIMALS = ('pig', 'cow', 'sheep')

class Animal(Document):
    kind = StringField(choice=ANIMALS)
    id = StringField()
    