import os
from constants import ANIMALS
     
class FarmView(object):
    def __init__(self, farm, farmer):
        self.farmer = farmer
        self.farm = farm

    def show_menu(self):
        self.init_message()
        self.show_options()
        option = input(":")
        return option


    def init_message(self):
        message = """
        Farma: {}
        Korisnik: {}
        """.format(self.farm.name, self.farmer.email)
        os.system('clear')
        print(message)

    def show_options(self):
        message = """
        1. (new_stall) Kreiranje nove stale
        2. (stall_list) Prikaz svih stala
        3. (log_out) Odjavljivanje
        """
        print(message)

    def create_stall(self):
        os.system('clear')
        data = {}
        data['name'] = input("Unesite naziv stale: ")
        print("Izaberite tip zivotinje")
        data['kind'] = self.choice_type_animal()
        return data

    def choice_type_animal(self):
        message = """
        1. (pig) Svinja
        2. (sheep) Ovca
        3. (cow) Krava
        """
        print(message)
        animal_type = input(":")
        while animal_type not in ANIMALS:
            animal_type = self.choice_type_animal()
        return animal_type

    def stall_list(self):
        os.system('clear')
        for item in self.farmer.farm.stalls:
            print("{} - {}".format(item.name, item.kind))

    

    