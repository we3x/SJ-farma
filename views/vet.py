import os
from constants import ANIMALS
from terminaltables import AsciiTable

class VetView(object):

    @classmethod
    def show_menu(cls, vet):
        cls.init_message(vet.first_name, vet.station_name)
        cls.show_options()
        option = input(":")
        return option


    @classmethod
    def init_message(cls,first_name, station_name):
        message = """
        Veterinar: {}
        Korisnik: {}
        """.format(first_name, station_name)
        os.system('clear')
        print(message)

    @classmethod
    def show_options(cls):
        message = """
        1. (new_service) Kreiranje nove usluge
        2. (service_list) Prikaz svih stala
        5. (log_out) Odjavljivanje
        """
        print(message)

    @classmethod
    def create_service_form(cls):
        data = {}
        data['id'] = input("Unesite jedinstvenu oznaku usluge: ")
        data['name'] = input("Unesite naziv usluge: ")
        data['price'] = input("Unesite cenu usluge: ")
        return data

    @classmethod
    def service_list(cls, services):
        os.system('clear')
        table_data =  [["Oznaka", "Naziv", "Cena"]]
        for service in services:
            table_data.append([service.id, service.name, service.price])
        table_view = AsciiTable(table_data)
        print(table_view.table)
        input()
