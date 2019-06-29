import os
from constants import ANIMALS
from terminaltables import AsciiTable

class FarmView(object):

    @classmethod
    def show_menu(cls, farm, farmer):
        cls.init_message(farm.name, farmer.email)
        cls.show_options()
        option = input(":")
        return option


    @classmethod
    def init_message(cls, farm_name, farmer_email):
        message = """
        Farma: {}
        Korisnik: {}
        """.format(farm_name, farmer_email)
        os.system('clear')
        print(message)

    @classmethod
    def show_options(cls):
        message = """
        1. (new_stall) Kreiranje nove stale
        2. (stall_list) Prikaz svih stala
        3. (create_animal) Dodavanje nove zivotinje
        4. (animal_list) Prikazivanje zivotinja
        5. (log_out) Odjavljivanje
        """
        print(message)

    @classmethod
    def create_stall(cls):
        os.system('clear')
        data = {}
        data['name'] = input("Unesite naziv stale: ")
        print("Izaberite tip zivotinje")
        data['kind'] = cls.choice_type_animal()
        return data

    @classmethod
    def choice_stall(cls, stalls):
        cls.stall_list(stalls)
        stall_name = input(":")
        stall = [stall for stall in stalls if stall["name"] == stall_name]
        while stall == []:
            stall_list()
            stall_name = input(":")
            stall = [stall for stall in stalls if stall["name"] == stall_name]
        return stall[0]

    @classmethod
    def choice_animal(cls, animals):
        cls.animal_list(animals)
        animal_id = input("Unesite oznaku zivotinje:")
        animal = [animal for animal in animals if animal['id'] == animal_id]
        while animal == []:
            animal = choice_animal(animals)
        return animal[0]

    @classmethod
    def create_animal_form(cls):
        data = {}
        data['name'] = input("Unesite ime zivotinje: ")
        data['id'] = input("Unesite identifikacionu oznaku zivotinje: ")
        return data


    @classmethod
    def choice_type_animal(cls):
        message = """
        1. (pig) Svinja
        2. (sheep) Ovca
        3. (cow) Krava
        """
        print(message)
        animal_type = input(":")
        while animal_type not in ANIMALS:
            animal_type = cls.choice_type_animal()
        return animal_type


    @classmethod
    def stall_list(cls, stalls):
        os.system('clear')
        table_data = [["Naziv", "Tip zivotinje"]]
        for item in stalls:
            table_data.append([item.name, item.kind])
        table_view = AsciiTable(table_data)
        print(table_view.table)

    @classmethod
    def animal_list(cls, animals):
        os.system('clear')
        table_data = [["Naziv", "Identifikaciona oznaka"]]
        for animal in animals:
            table_data.append([animal.name, animal.id])
        table_view = AsciiTable(table_data)
        print(table_view.table)
