

class Car:

    def __init__(self, manufacturer, model, color, plate, body=None, fuel=None, card=None, pin=None):

        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.plate = plate
        
        self.body = body
        self.fuel = fuel
        self.card = card
        self.pin = pin