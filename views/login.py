import os
class LoginView(object):
    def __init__(self):
        os.system("clear")
        print("Login View")

    def login_form(self):
        email = input("Unesite email: ")
        password = input("Unesite password: ")
        return (email, password)

    def wrong_user(self):
        pass