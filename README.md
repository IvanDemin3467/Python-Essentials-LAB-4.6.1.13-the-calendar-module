# Python-Essentials-LAB-4.6.1.13-the-calendar-module

**Objectives**

•	Improving the student's skills in using the Calendar class.

**Scenario**

During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

•	Create a class called MyCalendar that extends the Calendar class;

•	create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;

•	in your implementation, use the monthdays2calendar method of the Calendar class.

**The following are the expected results:**

*Sample arguments*
```
year=2019, weekday=0
```
*Expected output*
```
52
```

*Sample arguments*
```
year=2000, weekday=6
```
*Expected output*
```
53
```

**Implementation v1** (iterates through days in a week)
```
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
```
**Implementation v2** (gets by index, works faster)
```
    def count_weekday_in_year(self, year, weekday):
        # This method takes a year and a weekday as parameters,
        # and then returns the number of occurrences of a specific weekday in the year.
        counter = 0                                 # init counter to count weekdays in a year
        for iter in range(1, 13):                            # Iterate through weeks in a year
            for week in self.monthdays2calendar(year, iter): # get all weeks in a month
                if week[weekday][0] != 0:                    # If this day is in this month ->
                    counter += 1                             # -> cont it

        return counter                                       # weekdays counted -> return
```
