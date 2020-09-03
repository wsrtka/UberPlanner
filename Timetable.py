

class Timetable:

    def __init__(self):
        self.dispositions = [False * 7]

    def set_owner(self, driver):
        self.owner = driver

    def set_preferences(self, day, times):

        if times[0] >= times[1]:

            if not self.dispositions[day]:
                self.dispositions[day] = (None, times[0])

            else:
                self.dispositions[day] = (self.dispositions[day][0], times[0])

            self.dispositions[(day + 1) % 7] = (times[1], None)

        else:

            self.dispositions[day] = times