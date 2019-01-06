from mongoengine import *

def init_db():
    connect('sj-farm')
    print("init db complate")

def main():
    init_db()

if __name__ == "__main__":
    main()