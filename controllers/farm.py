import os
from views.farm import FarmView
from models.farm import Stall
from models.animal import Animal
from .task import TaskController

class FarmController(object):
    def __init__(self, **kwargs):
        self.farmer = kwargs['user']
        self.farm = self.farmer.farm
        self.taskController = TaskController()
        self.options = {
            'animal_list': self.animal_list,
            'create_animal': self.create_animal,
            'log_out': '',
            'new_stall': self.new_stall,
            'stall_list': self.stall_list,
            'choice_animal': self.choice_animal,
            'remove_animal': self.remove_animal,
            'make_app': self.make_app
        }
        self.farm_menu()

    def farm_menu(self):
        option = FarmView.show_menu(self.farm, self.farmer)
        while option not in self.options.keys():
            option = FarmView.show_menu(self.farm, self.farmer)
        if option == "log_out":
            return
        self.options[option]()
        self.farm_menu()

    def animal_list(self):
        stall = FarmView.choice_stall(self.farm.stalls)
        FarmView.animal_list(stall.animals)
        input()

    def make_app(self):
        pass

    def choice_animal(self):
        stall = FarmView.choice_stall(self.farm.stalls)
        animal = FarmView.choice_animal(stall.animals)
        return (animal, stall)

    def create_animal(self):
        stall = FarmView.choice_stall(self.farm.stalls)
        animal_data = FarmView.create_animal_form()
        animal = Animal(**animal_data)
        stall.animals.append(animal)
        self.farm.save()

    def remove_animal(self):
        animal,stall = self.choice_animal()
        stall.animals.remove(animal)
        self.farm.save()


    def new_stall(self):
        data = FarmView.create_stall()
        stall = Stall(**data)
        self.farm.stalls.append(stall)
        self.farm.save()
        input()

    def stall_list(self):
        FarmView.stall_list(self.farm.stalls)
        input()
