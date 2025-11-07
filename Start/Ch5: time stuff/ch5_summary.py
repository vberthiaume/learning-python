# =================== USING DATE OBJECTS ===================
from datetime import date
# Get today's date from the simple today() method from the date class
today = date.today()
print("today is : ", today)

# print out the date's individual components
print("Date components:", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("today's weekday is ", today.weekday())

# =================== USING DATETIME OBJECTS ===================
from datetime import datetime

# Get today's date from the datetime class
print("now with datetime: ", datetime.now())

# Get the current time
print("and now just the time: ", datetime.time(datetime.now()))
