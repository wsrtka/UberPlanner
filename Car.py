from Timetable import Timetable


class Car:


    def __init__(self):
        self.rating = 3
        self.reset_timetable()


    def __str__(self):
        return self.manufacturer + ' ' + self.model + ' ' + self.plate\


    def reset_timetable(self):
        self.timetable = Timetable()


    def set_timetable(self, timetable):
        self.timetable = timetable


    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer


    def set_model(self, model):
        self.model = model


    def set_color(self, color):
        self.color = color


    def set_plate(self, plate):
        self.plate = plate


    def set_body(self, body):
        self.body = body


    def set_fuel(self, fuel):
        self.fuel = fuel


    def set_card(self, card):
        self.card = card


    def set_pin(self, pin):
        self.pin = pin


    def set_rating(self, rating):
        self.rating = rating


    __repr__ = __str__