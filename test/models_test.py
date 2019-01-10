import unittest
import mongoengine
from models import *

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        mongoengine.connect(db='SJ-farm_test')


class CreateUserTest(ModelTestCase):
    def runTest(self):
        user = User()
        user.email = "veljko.simic98@gmail.com"
        user.password = "test123"
        user.username = "wex"
        user.first_name = "Veljko"
        user.last_name = "Simic"
        user.save()
        assert user.__repr__() == "User: veljko.simic98@gmail.com", \
            'invalid user create'

class CreateFarmTest(ModelTestCase):
    def runTest(self):
        farm = Farm()
        tor1 = Stall(kind="")
        farm.name = "Simic-Farm"
        farm.save()
        assert farm.__repr__() == 'Farm: Simic-Farm' , 'Failed create farm'

class CreateVetTest(ModelTestCase):
    def runTest(self):
        vet = Vet()
        vet.first_name = "Marko"
        vet.last_name = "Markovic"
        vet.email = "markic@gmai.com"
        vet.username = "mmarko"
        vet.password = "test123"
        vet.station_name = "Vet Marko"
        vet.services = [Service(id="h4",name="Pregled 4", price=100.0),\
                        Service(id="h5", name="Vakcinacija", price=12.20)]
        vet.save()
        assert vet.__repr__() == "Vet: mmarko Vet Marko", "Failed create vet"


