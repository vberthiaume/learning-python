#### Date Formatting ####
# strftime() and strptime() use these codes to format stuff:
#      https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-format-codes
# e.g., %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
# this site is also pretty cool for that: https://www.strfti.me/

from datetime import datetime

now = datetime.now()
print(now.strftime("Today is: %a, %B %d, %Y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("Locale date and time: %c"))