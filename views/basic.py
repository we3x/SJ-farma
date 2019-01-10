import os
import time

class BasicView(object):

    @staticmethod
    def greeting_message():
        os.system('clear')
        message = """
        Dobrodosli
        """
        print(message)
        time.sleep(1)

    @staticmethod
    def exit_message():
        os.system('clear')
        message = """
        Dovidjenja
        """
        print(message)
        time.sleep(1)

    @staticmethod
    def choice_auth():
        message = """
        1. Prijavljiviti se
        2. Registrovati se
        3. Izlazak iz sistema
        """
        os.system('clear')
        print(message)