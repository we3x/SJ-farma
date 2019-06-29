from views.basic import BasicView
from .login import LoginController
from .register import RegisterController
from .farm import FarmController
from .vet import VetController
from models.user import User

class MainController(object):
    def __init__(self):
        self.controllers = {
            'login': LoginController,
            'register': RegisterController,
            'Farmer': FarmController,
            'Vet': VetController,
            'exit': self.exit,
        }
        option = self.init_message()
        self.auth = self.controllers[option]()
        user = self.auth.get_user()

        # user = dict(user=User.auth("vet1@test.com", "vet1"), user_type="Vet")
        if user['user'] == None:
            self.__init__()
        self.controller = self.controllers[user['user_type']](**user)
        self.__init__()

    def exit(self):
        BasicView.exit_message()
        exit()

    def init_message(self):
        option = BasicView.choice_auth()
        while option not in ['login', 'register', 'exit']:
            option = BasicView.choice_auth()
        return option
