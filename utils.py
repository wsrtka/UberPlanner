from random import shuffle
from PyQt5.QtWidgets import QPushButton


def solve(memory_handler):

    cars = memory_handler.get_cars()
    cars.sort(key=lambda x: x.rating, reverse=True)

    drivers = memory_handler.get_drivers()
    drivers_with_priority = []

    for driver in drivers:

        if driver.priority:

            drivers_with_priority.append(driver)
            drivers.remove(driver)

    for day in range(7):

        shuffle(drivers_with_priority)

        for driver in drivers_with_priority:
            for car in cars:

                if car.timetable.collides(driver.timetable, day, driver.get_name()):
                    continue
                
                else:
                    car.timetable.set_solution(day, driver.timetable, driver.get_name())

        shuffle(drivers)

        for driver in drivers:
            for car in cars:

                if car.timetable.collides(driver.timetable, day, driver.get_name()):
                    continue
                
                else:
                    car.timetable.set_solution(day, driver.timetable, driver.get_name())


class ButtonFactory:

    def __init__(self):
        pass

    def get_button(self, name, function, parent=None, icon=None):
        button = QPushButton(name, parent=parent)
        button.clicked.connect(function)
        if icon:
            button.setIcon(icon) 
        return button