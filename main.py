from mongoengine import *
from mongoengine import signals
from models.user import User
from controllers.main import MainController

def init_db():
    connect('sj-farm')
    signals.pre_save.connect(User.pre_save, sender=User)
    print("init db complate")

def main():
    init_db()
    MainController()

if __name__ == "__main__":
    main()