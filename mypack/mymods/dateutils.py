"""
module: dateutils
Some common date related operations are found here

Author: Vinod Kumar <vinod@vinod.co>
Find more at: http://vinod.co
"""

__all__ = ["max_days_in_month"]

author = "Vinod Kumar"


def is_leap(year):
    """
    This function will evaluate to True/False based on the year's leapness

    :param year: The year you want to check for leap year
    :return: True if the input year is leap; False otherwise
    """

    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def max_days_in_year(year):
    return 366 if is_leap(year) else 365


def max_days_in_month(month, year):
    if month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 31


def julian_date(day, month, year):

    jd = day

    # from the start of 1900 till the end of (year-1)
    for y in range(1900, year):
        jd += max_days_in_year(y)

    for m in range(1, month):
        jd += max_days_in_month(m, year)

    return jd


if __name__ == "__main__":
    print("Year 2000 is leap? " + str(is_leap(2000)))
    print("Year 1996 is leap? " + str(is_leap(1996)))
    print("Year 2100 is leap? " + str(is_leap(2100)))

    print("Max days in 1996? " + str(max_days_in_year(1996)))
    print("Max days in 2017? " + str(max_days_in_year(2017)))

    print("Max days in 2, 2016? " + str(max_days_in_month(2, 2016)))
    print("Max days in 2, 2017? " + str(max_days_in_month(2, 2017)))
    print("Max days in 1, 2017? " + str(max_days_in_month(1, 2017)))
    print("Max days in 9, 2017? " + str(max_days_in_month(9, 2017)))

    # should be 42792
    print("Julian date for 27/2/2017 is {0}".format(julian_date(27, 2, 2017)))
