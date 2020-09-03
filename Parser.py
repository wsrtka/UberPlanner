import sys


from Driver import Driver
from Car import Car


class Parser:
    """
    Uber Planner - an app to manage Your Uber fleet timetable - made by Witold Serwatka
    List of available commands:
        help                shows a list of available commands
        add [Driver | Car]  adds new objects
        exit                closes the program
    """

    def __init__(self, mem_handler):
        self.memory_handler = mem_handler

    def get_user_input(self, var_name, required=True):

        prefix = '(Required)' if required else '(Optional)'
        user_input = input('%s Enter %s:\n' %(prefix, var_name))

        while len(user_input) == 0 and required:
            user_input = input('%s Enter %s:\n' %(prefix, var_name))

        return user_input


    def parse(self, input):

        words = input.split(' ')

        if words[0] == 'help':
            print(self.__doc__)

        elif words[0] == 'exit':
            sys.exit()

        elif words[0] == 'add':

            if words[1] == 'driver':
                
                new_driver = Driver()

                name = self.get_user_input('driver name')
                new_driver.set_name(name)

                surname = self.get_user_input('driver surname')
                new_driver.set_surname(surname)

                self.memory_handler.save_driver(new_driver)

            elif words[1] == 'car':
                
                new_car = Car()

                manufacturer = self.get_user_input('car manufacturer')
                new_car.set_manufacturer(manufacturer)

                model = self.get_user_input('car model')
                new_car.set_model(model)

                color = self.get_user_input('car color')
                new_car.set_color(color)

                plate = self.get_user_input('car license plate')
                new_car.set_plate(plate)

                body = self.get_user_input('car body type', required=False)
                new_car.set_body(body)

                fuel = self.get_user_input('car fuel type', required=False)
                new_car.set_fuel(fuel)

                card = self.get_user_input('car fuel card number', required=False)
                new_car.set_card(card)

                pin = self.get_user_input('car fuel card pin number', required=False)
                new_car.set_pin(pin)

                self.memory_handler.save_car(new_car)

        else:
            print('Could not understand input')

        return None
        