

class Driver:

    def __init__(self, name='', surname='', priority=False, timetable=None):
        self.priority = priority
        self.timetable = timetable
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname + ' priority: ' + str(self.priority)

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

    __repr__ = __str__