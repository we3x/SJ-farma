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
        print("Pogresni podatci")
        option = input("Zelite li da pokusate ponovo [Y/n]: ")
        if option.upper() == "N":
            return option
        else:
            return "Y"