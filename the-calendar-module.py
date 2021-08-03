# This is the Python Essentials 2 LAB 4.6.1.13-the-calendar-module
##Your task is to extend its functionality with a new method called count_weekday_in_year,
##which takes a year and a weekday as parameters,
##and then returns the number of occurrences of a specific weekday in the year.

import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        calendar.Calendar.__init__(self)

    def count_weekday_in_year(self, year, weekday):
        counter = 0
        for iter in range(1, 13):
            for week in self.monthdays2calendar(year, iter):
                for day in week:
                    if day[0] != 0 and day [1] == weekday:
                        counter += 1

        return counter
                    


if __name__ == "__main__":
    my_calendar = MyCalendar()
    print(my_calendar.count_weekday_in_year(2019, 0)) # Should return 52
    print(my_calendar.count_weekday_in_year(2000, 6)) # Should return 53
