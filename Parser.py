import sys


from Driver import Driver
from Car import Car
from Timetable import Timetable
from utils import solve


class Parser:
    """
    Uber Planner - an app to manage Your Uber fleet timetable - made by Witold Serwatka
    List of available commands:
        help                shows a list of available commands
        add 
                driver      adds a new driver
                car         adds a new car
                timetable   adds timetable for specified driver
        get
                driver/s    gets a specified driver or all drivers
                car/s       gets a specified car or all cars
                solution    gets a timetable for all drivers
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

        words = input.lower().split(' ')

        if words[0] == 'help':
            print(self.__doc__)

        elif words[0] == 'exit':
            
            self.memory_handler.save_all_data()
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

            elif words[1] == 'timetable':
                
                new_timetable = Timetable()

                owner = self.get_user_input('timetable owner')
                owner = owner.split()

                driver = self.memory_handler.get_driver(owner[0], owner[1])

                if not driver:
                    print('Could not find driver!')
                    return

                for day in range(7):
                    
                    start_time = self.get_user_input('beginning of shift for day ' + day, required=False)
                    
                    if len(start_time):
                        end_time = self.get_user_input('end of shift')

                    new_timetable.set_preferences(day, (start_time, end_time))
                
                driver.set_timetable(new_timetable)

        elif words[0] == 'get':

            if words[1] == 'car':
                
                plate = self.get_user_input('car license plate')

                car = self.memory_handler.get_car_by_plate(plate)

                print(car)

            elif words[1] == 'driver':
                
                surname = self.get_user_input('driver surname and name')
                surname = surname.split()

                if len(surname) == 2:
                    driver = self.memory_handler.get_driver(surname[0], surname[1])
                
                else:
                    driver = self.memory_handler.get_driver(surname[0])

                print(driver)

            elif words[1] == 'cars':
                print(self.memory_handler.get_cars())

            elif words[1] == 'drivers':
                print(self.memory_handler.get_drivers())

            elif words[1] == 'solution':
                
                solve(self.memory_handler)
                
                cars = self.memory_handler.get_cars()
                
                for car in cars:
                    print(car.timetable)

        else:
            print('Could not understand input')
        