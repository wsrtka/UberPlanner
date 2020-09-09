

class Timetable:

    def __init__(self):
        self.dispositions = [[False] * 24 for i in range(7)]

    def set_preferences(self, day, times):

        if times[0] >= times[1]:

            for i in range(times[0], 24):
                self.dispositions[day][i] = True

            for i in range(0, times[1]):
                self.dispositions[(day + 1) % 7][i] = True

        else:

            for i in range(times[0], times[1]):
                self.dispositions[day][i] = True