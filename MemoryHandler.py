import json
import pickle

from Car import Car
from Driver import Driver


class MemoryHandler:


    def __init__(self):

        with open('settings.json', 'r') as file:
            self.settings = json.load(file)

        with open(self.settings['drivers_savefile'], 'rb') as file:
            
            saved_drivers = pickle.load(file)
            self.drivers = []

            for driver in saved_drivers:
                self.drivers.append(Driver(**driver))


        with open(self.settings['cars_savefile'], 'rb') as file:
            
            saved_cars = pickle.load(file)
            self.cars = []

            for car in saved_cars:
                self.cars.append(Car(**car))


    def save_car(self, car):
        self.cars.append(car)


    def save_driver(self, driver):

        if driver.__dict__ not in self.drivers:
            self.drivers.append(driver)


    def save_all_data(self):

        drivers_to_save = []
        cars_to_save = []

        for driver in self.drivers:
            drivers_to_save.append(driver.__dict__)

        for car in self.cars:
            cars_to_save.append(car.__dict__)

        with open(self.settings['drivers_savefile'], 'wb') as file:
            pickle.dump(drivers_to_save, file)

        with open(self.settings['cars_savefile'], 'wb') as file:
            pickle.dump(cars_to_save, file) 


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
                return car

        return None