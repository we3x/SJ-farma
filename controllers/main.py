from views.basic import BasicView
from .login import LoginController
from .register import RegisterController
from .farm import FarmController
from .vet import VetController

class MainController(object):
    def __init__(self):
        self.controllers = {
            'login': LoginController,
            'register': RegisterController,
            'Farmer': FarmController,
            'Vet': VetController,
            'exit': self.exit,
        }
        self.view  = BasicView()
        option = self.init_message()
        self.auth = self.controllers[option]()
        user = self.auth.get_user()
        if user['user'] == None:
            self.__init__()
        self.controller = self.controllers[user['user_type']](**user)
        self.__init__()

    def exit(self):
        self.view.exit_message()
        exit()

    def init_message(self):
        option = self.view.choice_auth()
        while option not in ['login', 'register', 'exit']:
            option = self.view.choice_auth()
        return option