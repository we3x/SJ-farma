from views.register import RegisterView

class RegisterController(object):
    def __init__(self):
        self.view = RegisterView()

    def get_user(self):
        pass