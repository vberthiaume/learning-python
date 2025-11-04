# getting user input input 
name = input ("write ya name bro: ")
print("here's ya name bro: ", name)

# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

print ("nom " * 3)      # you can multiply a string with an integer
# print ("nom " + 3)    # but not addition

# Logical and comparison operators 
print (not True)    # the inverse boolean operator is "not", and not "!" lol

# re-declaring a variable works
myint = "myint is actually a string"
print (myint)

# conditional flow on multiple lines
x, y = 10, 100
if x < y:
    print ("smaller x")
elif x > y:
    print ("smaller y")
else:
    print ("same")

# conditional statements on one line (elif not supported here)
print ("x is less than y" if x < y else "x is the same or bigger than y bro")