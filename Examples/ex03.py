from dateutils import *
import sys
from datetime import date


def main():

    month = int(input("Enter the month: "))

    if month not in range(1, 13):
        print("Invalid month; must be between 1 to 12")
        sys.exit(1)

    year = int(input("Enter the year: "))
    if year < 1900:
        print("Invalid year; must be >= 1900")
        sys.exit(2)

    dt = date(year, month, 1)
    strmonth = dt.strftime("%B")
    print("\n\n{0} {1}".format(strmonth, year))
    print("Su Mo Tu We Th Fr Sa")
    print("---------------------")

    max_days = max_days_in_month(month, year)
    offset = julian_date(1, month, year) % 7
    print("   "*offset, end="")

    for d in range(1, max_days+1):
        print("%2d " % d, end="")
        if (offset + d) % 7 == 0:
            print()


if __name__ == "__main__":
    main()
