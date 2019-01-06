from mongoengine import *
from .vet import Service, Vet
from .animal import Animal
from .farm import Farm

class Task(EmbeddedDocument):
    service = ReferenceField(Service)
    animal = ReferenceField(Animal)
    date = DateField()
    solved = BooleanField(default=False)

class Tasks(Document):
    farm = ReferenceField(Farm)
    vet = ReferenceField(Vet)
    tasks = ListField(EmbeddedDocumentField(Task))