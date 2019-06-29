from views.login import LoginView
from models.user import User

class LoginController():
    def __init__(self):
        email, password = LoginView.login_form()
        try:
            self.user = User.auth(email, password)
        except Exception as e:
            option = LoginView.wrong_user()
            if option == 'Y':
                self.__init__()
            else:
                self.user = None
                return

    def get_user(self):
        return dict(user=self.user, user_type=type(self.user).__name__)
        
