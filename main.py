from mongoengine import *
from controllers.main import MainController

def init_db():
    connect('sj-farm')
    print("init db complate")

def main():
    init_db()
    MainController()

if __name__ == "__main__":
    main()