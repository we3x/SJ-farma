from mongoengine import *

class User():
    email = StringField()
    password = StringField(max_length=64)
    username = StringField(max_length=32)
    first_name = StringField(max_length=32)
    last_name = StringField(max_length=32)
