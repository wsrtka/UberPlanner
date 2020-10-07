import json
import pickle
from Car import Car


class MemoryHandler:


    def __init__(self):

        with open('settings.json', 'r') as file:
            self.settings = json.load(file)

        with open(self.settings['drivers_savefile'], 'rb') as file:
            self.drivers = pickle.load(file)

        with open(self.settings['cars_savefile'], 'rb') as file:
            self.cars = pickle.load(file)


    def save_car(self, car):
        self.cars.append(car.__dict__)


    def save_driver(self, driver):

        if driver.__dict__ not in self.drivers:
            self.drivers.append(driver.__dict__)


    def save_all_data(self):

        with open(self.settings['drivers_savefile'], 'wb') as file:
            pickle.dump(self.drivers, file)

        with open(self.settings['cars_savefile'], 'wb') as file:
            pickle.dump(self.cars, file) 


    def get_cars(self):
        return self.cars


    def get_drivers(self):
        return self.drivers


    def get_driver(self, surname, name=None):

        results = []

        for driver in self.drivers:
            
            if (driver.name == name and driver.surname == surname) or (not name and driver.surname == surname):
                results.append(driver)

        return results

# TODO: replace the below function with filter class
    def get_car_by_plate(self, plate):
        
        for car in self.cars:

            if car.plate == plate:
                return Car(**car)

        return None