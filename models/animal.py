from mongoengine import *

class Animal(EmbeddedDocument):
    name = StringField(max_length=32)
    id = StringField()
    