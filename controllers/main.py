from views.basic import BasicView
from .login import LoginController
from .register import RegisterController
from .farmer import FarmerController
from .vet import VetController

class MainController(object):
    def __init__(self):
        self.controllers = {
            'login': LoginController,
            'register': RegisterController,
            'farmer': FarmerController,
            'vet': VetController,
            'exit': self.exit,
        }
        self.view  = BasicView()
        option = self.init_message()
        self.auth = self.controllers[option]()
        user = self.auth.get_user()
        if user == None:
            self.__init__()
        self.controller = self.controllers[user.type]()

    def exit(self):
        self.view.exit_message()
        exit()

    def init_message(self):
        self.view.greeting_message()
        self.view.choice_auth()
        option = input()
        while option not in ['login', 'register', 'exit']:
            self.view.choice_auth()
            option = input()
        return option