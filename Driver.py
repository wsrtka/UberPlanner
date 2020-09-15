

class Driver:

    def __init__(self):
        self.priority = False
        self.timetable = None

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_priority(self, priority):
        self.priority = priority

    def set_timetable(self, timetable):
        self.timetable = timetable

    def clear_timetable(self):
        self.timetable = None

    def get_name(self):
        return self.name + self.surname