import os
class RegisterView():

    @classmethod
    def choice_user(cls):
        message = """
        Izaberite tip korisnika:
        Farmer
        Veterinar
        """
        os.system('clear')
        print(message)
        choice = input(":")
        return choice

    @classmethod
    def vet_form(cls):
        os.system('clear')
        print("Kreiranje novog Veterinara")
        data = {}
        data['email'] = input("email: ")
        data['first_name'] = input("ime: ")
        data['last_name'] = input("prezime: ")
        data['password'] = input("password: ")
        data['station_name'] = input("ime stanice: ")
        return data

    @classmethod
    def farmer_form(cls):
        os.system('clear')
        print("Kreiranje novog Farmera")
        data = {}
        data['email'] = input("email: ")
        data['first_name'] = input("ime: ")
        data['last_name'] = input("prezime: ")
        data['password'] = input("password: ")
        data['farm_name'] = input("ime farme: ")
        return data
