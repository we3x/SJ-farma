import os
from views.farmer import FarmerView
class FarmerController(object):
    def __init__(self, **kwargs):
        self.options = {
            'new_stall': 'Kreiranje stale',
            'log_out': 'Odjavljivanje',
            'view_stall': 'Pregled stala'
        }
        self.farmer = kwargs['user']
        self.farm = self.farmer.farm
        self.view = FarmerView(self.farmer)
        option = self.view.farmer_menu()
        while option not in ["new_stall", "log_out"]:
            option = self.farmer_menu()
        print(self.options[option])
        
