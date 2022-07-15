class Date:
    def __init__(self, day: int, month: int, year: int):
        """

        :param day: the day of the date
        :param month: the month of the date
        :param year: the year of the date
        get a date and manipulate it without using the datetime module
        """
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("date must be int")
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):  # printing like toString
        return f"{self._day}/{self._month}/{self._year}"

    def isvalid(self):
        """
        checks if the date that we send is valid
        :return: if it's not valid we raise an error at the specific point that it failed
        DD/M/YYYY
        """
        days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
            days_in_month[2] = 29
        # if self._day < 1 or self._day > 31: #unsolved , can get the 30/2 as a date.
        if self._day > days_in_month[self._month] or self._day < 1:
            raise TypeError("day is not valid")
        elif self._month < 1 or self._month > 12:
            raise TypeError("month is not valid")
        elif self._year < 1000 or self._year > 9999:
            raise TypeError("year is not valid")
        else:
            return "this is a valid date"

    def getNextDay(self):
        """
        a method to get the next day of a specific date
        :return: the date of the next day from the date we send
        """
        days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
            days_in_month[2] = 29
        if self._day < days_in_month[self._month]:
            return Date(self._day + 1, self._month, self._year)
        if days_in_month[self._month] < self._day + 1 and self._month < 12:
            return Date(1, self._month + 1, self._year)
        else:
            return Date(1, 1, self._year + 1)

    def getNextDays(self, add_days: int):
        """

        :param add_days: a number of days that we want to add
        :return:a new date after we added days to it
        """
        daysToAdd = self.getNextDay()
        for day in range(add_days):
            daysToAdd = daysToAdd.getNextDay()
        return daysToAdd

    def __eq__(self, other):
        if self._day == other._day and self._month == other._month and self._year == other._year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self._year < other._year or self._year == other._year and self._month < other.month or \
                self._year == other._year and self._month == other._month and self._day < other._day:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._year > other._year or self._year == other._year and self._month > other.month or \
                self._year == other._year and self._month == other._month and self._day > other._day:
            return True
        else:
            return False

    def __sub__(self, other):
        """
        a method that do date - date to get the day differences
        :param other: other will be the second date that we send
        :return: date differences in days
        """
        days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
            days_in_month[2] = 29
        first_date = self._day
        second_date = other._day
        year_dif_in_days = (self._year - other._year) * 365
        for month in range(self._month):
            first_date = first_date + days_in_month[month]

        for month in range(other._month):
            second_date = second_date + days_in_month[month]

        return first_date - second_date + year_dif_in_days


d1 = Date(2, 3, 2014)
d2 = Date(11, 12, 2013)
print(f"{d1} -> {d1.isvalid()}")
print(f"{d2} -> {d2.isvalid()}")
print(f"the next day of {d1} is : {d1.getNextDay()}")
print(f"the date after we added days to it is : {d1.getNextDays(98)}")
print("the dates are equal? : ", d1 == d2)
print("the first date is lower than second date? :", d1 < d2)
print("the first date is greater than second date? :", d1 > d2)
print("the date differences in days is : ", d1 - d2)
