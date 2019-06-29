import os
class LoginView():

    @classmethod
    def login_form(cls):
        os.system("clear")
        email = input("Unesite email: ")
        password = input("Unesite password: ")
        return (email, password)

    @classmethod
    def wrong_user(cls):
        print("Pogresni podatci")
        option = input("Zelite li da pokusate ponovo [Y/n]: ")
        if option.upper() == "N":
            return option
        else:
            return "Y"
