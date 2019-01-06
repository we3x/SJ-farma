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



