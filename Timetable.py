import json


class Timetable:


    def __init__(self):
        self.dispositions = [[False] * 24 for i in range(7)]

    
    def __str__(self):
        return str(self.dispositions)


    def collides(self, other, day, driver):
        
        for hour in range(24):
            
            if self.dispositions[day][hour] and other[day][hour] and not self.dispositions[day][hour] == driver:
                return True

            if hour < 12 and self.dispositions[(day + 1) % 7][hour] and other[(day + 1) % 7][hour] and not self.dispositions[(day + 1) % 7][hour] == driver:
                return True

        return False

   
    def set_solution(self, day, preferences, driver):
        
        for hour in range(24):

            if preferences[day][hour]:
                self.dispositions[day][hour] = driver

            if hour < 12 and preferences[(day + 1) % 7][hour]:
                self.dispositions[(day + 1) % 7][hour] = driver


    
    def set_preferences(self, day, times):

        if times[0] >= times[1]:

            for i in range(times[0], 24):
                self.dispositions[day][i] = True

            for i in range(0, times[1]):
                self.dispositions[(day + 1) % 7][i] = True

        else:

            for i in range(times[0], times[1]):
                self.dispositions[day][i] = True


    __repr__ = __str__