# This is the Python Essentials 2 LAB 4.6.1.13-the-calendar-module
##Your task is to extend its functionality with a new method called count_weekday_in_year,
##which takes a year and a weekday as parameters,
##and then returns the number of occurrences of a specific weekday in the year.

import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        calendar.Calendar.__init__(self)

    def count_weekday_in_year(self, year, weekday):
        # This method takes a year and a weekday as parameters,
        # and then returns the number of occurrences of a specific weekday in the year.
        counter = 0                                 # init counter to count weekdays in a year
        for iter in range(1, 13):                            # Iterate through weeks in a year
            for week in self.monthdays2calendar(year, iter): # get all weeks in a month
                if week[weekday][0] != 0:                    # If this day is in this month ->
                    counter += 1                             # -> cont it

        return counter                                       # weekdays counted -> return
                    

# main
if __name__ == "__main__":
    my_calendar = MyCalendar()
    print(my_calendar.count_weekday_in_year(2019, 0)) # Should return 52
    print(my_calendar.count_weekday_in_year(2000, 6)) # Should return 53
