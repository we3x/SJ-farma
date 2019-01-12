import os
from views.farm import FarmView
from models.farm import Stall

class FarmController(object):
    def __init__(self, **kwargs):
        self.options = {
            'new_stall': self.new_stall,
            'stall_list': self.stall_list,
            'log_out': ''
        }
        self.farmer = kwargs['user']
        self.farm = self.farmer.farm
        self.view = FarmView(self.farm, self.farmer)
        self.farm_menu()

    def farm_menu(self):
        option = self.view.show_menu()
        while option not in self.options.keys():
            option = self.view.show_menu()
        if option == "log_out":
            return
        self.options[option]()
        self.farm_menu()

    def new_stall(self):
        data = self.view.create_stall()
        stall = Stall(**data)
        self.farm.stalls.append(stall)
        self.farm.save()
        input()

    def stall_list(self):
        self.view.stall_list()
        input()
        