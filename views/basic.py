import os
import time

class BasicView(object):

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
        1. (login) Prijavljiviti se
        2. (register) Registrovati se
        3. (exit) Izlazak iz sistema
        """
        os.system('clear')
        print(message)
        choice = input(":")
        return choice