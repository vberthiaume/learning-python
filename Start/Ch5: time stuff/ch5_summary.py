# =================== DATE OBJECTS TO GET DATE INFORMATION ===================
from datetime import date
# Get today's date from the simple today() method from the date class
today = date.today()
print("the current date is:  ", today)

# print out the date's individual components
print("individual date bits: ", today.day, ", weekday (0-6):", today.weekday(), ", month:", today.month, ", year:", today.year)

# =================== DATETIME OBJECTS TO GET DATE AND TIME INFORMATION ===================
print("======================================")
from datetime import datetime
now = datetime.now()

# Get today's date from the datetime class
print("datetime now has both the date and time:     ", now)
print("to get only the time you make a time object: ", datetime.time(now))

# strftime() and strptime() use these codes to format stuff:
#      https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-format-codes
# this site is also pretty cool for that: https://www.strfti.me/
print(now.strftime("with strftime you can extract individual bits:   %a, %B %d, %Y"))
print(now.strftime("and you can print it in the currrent locale way: %c"))

# =================== CALCULATIONS ARE DONE WITH TIMEDELTA ===================
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import timedelta
print( "3 weeks 2 days 4 hours from now = ", now + timedelta(weeks=3,days=2,hours=4))

# figure out time until april fools
af = date(today.year, month=4, day=1)
diff = af - date(today.year, month=4, day=4)
if diff.days < 0: diff += timedelta(days=365)
print ("only", diff.days, "days until april fools")

# =================== USING CALENDAR ===================
NOW HERE

import calendar

# create a plain text calendar


# create an HTML formatted calendar


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

