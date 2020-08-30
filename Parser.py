import sys


from Driver import Driver
from Car import Car


class Parser:
    """
    List of available commands:
        help                shows a list of available commands
        add [Driver | Car]  adds new objects
        exit                closes the program
    """

    def __init__(self):
        
        pass


    def parse(self, input):

        words = input.split(' ')

        if words[0] == 'help':
            print(self.__doc__)

        elif words[0] == 'exit':
            sys.exit()

        elif words[0] == 'add':

            if words[1] == 'driver':
                
                name = input('Enter driver name:\n')
                surname = input('Enter driver surname:\n')

                return Driver(name, surname)

            elif words[1] == 'car':
                
                manufacturer = input('Enter car manufacturer:\n')
                model = input('Enter car model:\n')
                color = input('Enter car color:\n')
                plate = input('Enter car license plate:\n')

                body = input('(Optional) Enter car body type:\n')
                fuel = input('(Optional) Enter car fuel type:\n')
                card = input('(Optional) Enter car fuel card number:\n')
                pin = input('(Optional) Enter car fuel card pin number:\n')

                return Car(manufacturer, model, color, plate)

        else:
            print('Could not understand input')

        return None
        