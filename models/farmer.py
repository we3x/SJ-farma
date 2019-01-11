from mongoengine import *
from .user import User

class Farmer(User):
    farm = ReferenceField('Farm')

    def __repr__(self):
        return "Farmer: %s" % self.email