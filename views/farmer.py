import os
class FarmerView(object):
    def __init__(self, farmer):
        self.farmer = farmer

    def farmer_menu(self):
        self.init_message(self.farmer.farm.name, self.farmer.email)
        self.show_options()
        option = input(":")
        return option


    def init_message(self, farm_name, email):
        message = """
        Farma: {}
        Korisnik: {}
        """.format(farm_name, email)
        os.system('clear')
        print(message)

    def show_options(self):
        message = """
        1. (new_stall) Kreiranje nove stale
        2. (log_out) Odjavljivanje
        """
        print(message)
    

    