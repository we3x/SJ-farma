import os
import time

class BasicView(object):

    @classmethod
    def exit_message(cls):
        os.system('clear')
        message = """
        Dovidjenja
        """
        print(message)
        time.sleep(1)

    @classmethod
    def choice_auth(cls):
        message = """
        1. (login) Prijavljiviti se
        2. (register) Registrovati se
        3. (exit) Izlazak iz sistema
        """
        os.system('clear')
        print(message)
        choice = input(":")
        return choice
