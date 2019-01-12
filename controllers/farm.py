import os
from views.farm import FarmView
from models.farm import Stall
from models.animal import Animal

class FarmController(object):
    def __init__(self, **kwargs):
        self.farmer = kwargs['user']
        self.farm = self.farmer.farm
        self.view = FarmView(self.farm, self.farmer)
        self.options = {
            'animal_list': self.animal_list,
            'create_animal': self.create_animal,
            'log_out': '',
            'new_stall': self.new_stall,
            'stall_list': self.stall_list
        }
        self.farm_menu()

    def farm_menu(self):
        option = self.view.show_menu()
        while option not in self.options.keys():
            option = self.view.show_menu()
        if option == "log_out":
            return
        self.options[option]()
        self.farm_menu()

    def animal_list(self):
        stall = self.view.choice_stall()
        self.view.animal_list(stall.animals)
        input()


    def create_animal(self):
        stall = self.view.choice_stall()
        animal_data = self.view.create_animal_form()
        animal = Animal(**animal_data)
        stall.animals.append(animal)
        self.farm.save()


    def new_stall(self):
        data = self.view.create_stall()
        stall = Stall(**data)
        self.farm.stalls.append(stall)
        self.farm.save()
        input()

    def stall_list(self):
        self.view.stall_list()
        input()
        