from views.basic import BasicView
from .login import LoginController
from .register import RegisterController

class MainController(object):

    def __init__(self):
        self.view  = BasicView()
        option = self.init_message()
        if option == 1:
            self.auth = LoginController()
        elif option == 2:
            self.auth = RegisterController()
        elif option == 3:
            self.exit()

    def exit(self):
        self.view.exit_message()
        exit()

    def init_message(self):
        self.view.greeting_message()
        self.view.choice_auth()
        option = eval(input())
        while option not in [1, 2, 3]:
            self.view.choice_auth()
            option = eval(input())
        return option




