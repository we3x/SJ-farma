from models.vet import Service, Vet
from views.vet import VetView

class VetController(object):
    def __init__(self, **kwargs):
        vet = kwargs['user']
        vet.__class__ = Vet
        self.vet = vet
        self.options = {
            'new_service': self.new_service,
            'service_list': self.service_list
        }
        self.vet_menu()

    def vet_menu(self):
        option = VetView.show_menu(self.vet)
        while option not in self.options.keys():
            option = VetView.show_menu(self.vet)
        if option == "log_out":
            return
        self.options[option]()
        self.vet_menu()

    def new_service(self):
        service_data = VetView.create_service_form()
        service = Service(**service_data)
        self.vet.services.append(service)
        self.vet.save()

    def service_list(self):
        VetView.service_list(self.vet.services)
