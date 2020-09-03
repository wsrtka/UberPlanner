

class Timetable:

    def __init__(self):
        self.dispositions = [False * 7]

    def set_owner(self, driver):
        self.owner = driver

    def set_preferences(self, day, times):
        self.dispositions[day] = times