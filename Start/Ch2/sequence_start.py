# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
myList = [0, 1, "two", 3.2, False]
# print (myList)
# print (len(myList))

# to access a member of a sequence type, use [], and this can include negative numbers, which start from the end of the list
# print (myList[0])    # print the first item
# print (myList[-1])   # print the last item

myStr = "this is a string"
print (myStr[2])

# add a list to another list
anotherList = [2, "asdf"]
print (myList + anotherList)

# use slices to get parts of a sequence
print (myList[1:4:2])   # print element 1 through 3, by increments of 2, so just elements 1 and 3
print (myList[::2])   # these are all optional lol, default values are 0, -1, and 1. Here we print all even-numbered indices

# you can use slices to reverse a sequence, by setting -1 as the step lol (also works with strings)
print (myList[::-1])


# Tuples are like lists, but they are immutable (just like strings)
# because they are immutable, they are a bit more efficient
myTuple = (0, 1, 2, "trois")
print (myTuple[-1])

# Sets are also sequences, but they contain unique values
mySet = {1, 2, 3, 4, 2, 4, "hey"}
print (mySet)       # when we print this, the second set of 2 and 4 will not be in there
# print (mySet[2])  # sets don't support indexing, so this doesn't run

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print (1 in myList)
print (3 in myTuple)
print (5 in mySet)
