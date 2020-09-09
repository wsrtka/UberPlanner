

class MemoryHandler:

    def __init__(self):

        self.cars = []
        self.drivers = []

    def save_car(self, car):
        self.cars.append(car)

    def save_driver(self, driver):

        if driver not in self.drivers:
            self.drivers.append(driver)

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