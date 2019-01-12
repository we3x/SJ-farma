import os
class RegisterView(object):
    def __init__(self):
        os.system("clear")
        print("Register View")

    def choice_user(self):
        message = """
        Izaberite tip korisnika:
        Farmer
        Veterinar
        """
        os.system('clear')
        print(message)
        choice = input(":")
        return choice
    
    def vet_form(self):
        os.system('clear')
        print("Kreiranje novog Veterinara")
        data = {}
        data['email'] = input("email: ")
        data['first_name'] = input("ime: ")
        data['last_name'] = input("prezime: ")
        data['password'] = input("password: ")
        data['station_name'] = input("ime stanice: ")
        return data

    def farmer_form(self):
        os.system('clear')
        print("Kreiranje novog Farmera")
        data = {}
        data['email'] = input("email: ")
        data['first_name'] = input("ime: ")
        data['last_name'] = input("prezime: ")
        data['password'] = input("password: ")
        data['farm_name'] = input("ime farme: ")
        return data