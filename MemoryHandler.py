

class MemoryHandler:

    def __init__(self):

        self.cars = []
        self.drivers = []
        self.timetables = []

    def save_car(self, car):
        self.cars.append(car)

    def save_driver(self, driver):
        self.drivers.append(driver)

    def save_timetable(self, timetable):
        self.timetables.append(timetable)

    def get_cars(self):
        return self.cars

    def get_drivers(self):
        return self.drivers

    def get_timetables(self):
        return self.timetables

    def get_driver(self, name, surname=None):

        for driver in self.drivers:
            
            if driver.name == name and driver.surname == surname:
                
                return driver

        return None