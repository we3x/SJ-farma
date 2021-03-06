from views.register import RegisterView
from models.vet import Vet
from models.farm import Farm
from models.farmer import Farmer

class RegisterController(object):
    def __init__(self):
        create_user = {
            "Vet": self.create_vet,
            "Farmer": self.create_farmer,
        }
        user_type = self.get_user_type()
        self.user = create_user[user_type]()

    def get_user_type(self):
        user_type = RegisterView.choice_user()
        while user_type not in ["Veterinar", "Farmer"]:
            user_type = RegisterView.choice_user()
        if user_type == "Veterinar":
            return "Vet"
        else:
            return "Farmer"

    def create_vet(self):
        data = RegisterView.vet_form()
        user = Vet(**data)
        user.save_user()
        return dict(user=user, user_type="Vet")

    def create_farmer(self):
        data = RegisterView.farmer_form()
        farm_name = data.get('farm_name')
        del data['farm_name']
        farm = Farm(name=farm_name)
        farm.save()
        user = Farmer(farm=farm,**data)
        user.save_user()
        return dict(user=user, user_type="Farmer")

    def get_user(self):
        return self.user
