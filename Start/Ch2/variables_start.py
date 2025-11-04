import os
if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For macOS and Linux
    os.system('clear')

# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
# print ("nom " * 3)      # this works
# print ("nom " + 3)    # but this doesn't!

# Logical and comparison operators 
print (not True)    # the inverse boolean operator is "not", and not "!" lol

# re-declaring a variable works
myint = "actually a string"
print (myint)