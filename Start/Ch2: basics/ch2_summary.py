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

# define a while loop
# answer = input("should I stay or should I go? ")
# while answer != "go":
#     print (answer)
#     answer = input("should I stay or should I go? ")

# define a for loop
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for d in days:
    if d == "thu":
        break
    if d == "tue":
        continue
    print (d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days): #i, d here is a tuple
    print (i,d)

# regular function
def cube(x, greeting=None):
    print(greeting)
    return x * x * x

print (cube(2))                         # uses the default value for greeting
print (cube(2, "brooo"))                # set the greeting normally
print (cube(greeting = "before", x=2))  # set the greeting out of order explicitly

# function with variable number of parameters
def multi_add(*args):   # the * here means an indefinite number of arguments. Doesn't need to be named args
    result = 0
    for x in args:
        result += x
    return result

print (multi_add(1, 2, 3, 4, 5))