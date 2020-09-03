

class MemoryHandler:

    def __init__(self):

        self.cars = []
        self.drivers = []

    def save_driver(self, driver):
        self.drivers.append(driver)

    def save_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars

    def get_drivers(self):
        return self.drivers