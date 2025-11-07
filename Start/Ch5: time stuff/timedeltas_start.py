from datetime import date
from datetime import datetime
from datetime import timedelta

# documentation for timedelta objects: 
# https://docs.python.org/3/library/datetime.html#timedelta-objects

now = datetime.now()
print(f"Today is                           {now}")
print( "3 weeks 2 days 4 hours from now = ", now + timedelta(weeks=3,days=2,hours=4))

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
